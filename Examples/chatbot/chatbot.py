import streamlit as st
from typing import Any
import requests
import re
import time
from pydantic import BaseModel, Field
from langchain_community.tools import Tool
from langchain_core.tools import StructuredTool
from langchain_core.messages import HumanMessage, AIMessage
from langchain.agents import create_agent
from SpinLLM import SpinChatModel

#Initialize SpiLLI
@st.cache_resource
def load_resources():
    llm=SpinChatModel(
        model_name="Openai_Gpt Oss 20b",
        encryption_path='./SpiLLI_Community.pem',
        temperature=0.8,
        max_tokens=512
    )

    return llm

def internet_search_fn(query: str) -> str:
    """Searches the internet using DuckDuckGo Instant Answer API."""
    try:
        url = "https://api.duckduckgo.com"
        params = {"q": query, "format": "json", "no_redirect": 1}
        response = requests.get(url, params=params, timeout=8).json()

        # Extract best available information
        abstract = response.get("AbstractText") or ""
        related = response.get("RelatedTopics") or []

        if abstract:
            return abstract
        
        # fallback to related links
        results = []
        for item in related[:5]:
            if "Text" in item:
                results.append(f"- {item['Text']}")
        return "\n".join(results) if results else "No useful results found."
    
    except Exception as e:
        return f"[Web search failed: {str(e)}]"
    
class InternetSearchInput(BaseModel):
    query: str = Field(..., description="Search query for internet lookup")

internet_search_tool = StructuredTool(
    name="internet_search",
    func=internet_search_fn,   #Python knows this function
    description="Search the internet for real-time information.",
    args_schema=InternetSearchInput,
)

# 

def clean_agent_output(text: str) -> str:
    """
    Removes model channel tokens and end markers from agent output.
    Works with Groq / OpenAI / OSS-style formats.
    """
    if not text:
        return text

    # Case 1: Harmony / OSS token format
    match = re.search(r"<\|channel\|>final<\|message\|>(.*)", text, re.DOTALL)
    if match:
        text = match.group(1)
    else:
        # Case 2: Plain text channel format
        match = re.search(r"\bfinal\b(.*)", text, re.DOTALL | re.IGNORECASE)
        if match:
            text = match.group(1)
            
    # Remove <|...|> blocks
    text = re.sub(r"<\|.*?\|>", "", text)

    # Remove [EOG] or similar markers
    text = re.sub(r"\[EOG\]", "", text, flags=re.IGNORECASE)

    return text.strip()



# ----------------------------------
# (Optional) utility tool example
# ----------------------------------
def echo_tool_fn(text: str) -> str:
    # """Echoes user input (example utility tool)."""
    return f"You said: {text}"

class InternetSearchInput(BaseModel):
        query: str = Field(..., description="Search query for internet lookup")
      

def stream_text(text: str, delay: float = 0.015):
    placeholder = st.empty()
    output = ""

    for char in text:
        output += char
        placeholder.markdown(output)
        time.sleep(delay)

    return output


# ----------------------------------
# Create Chatbot Agent
# ----------------------------------
def create_chatbot_agent(llm):
    # Optional tools — you can add more later
    echo_tool = Tool.from_function(
        name="echo_tool",
        func=echo_tool_fn,
        description="Echo back user input (debugging / demo tool)"
    )

    internet_search_tool = StructuredTool(
        name="internet_search",
        func=lambda args: internet_search_fn(args.query),
        description="Search the internet for real-time information.",
        args_schema=InternetSearchInput,
    )

    tools = [echo_tool, internet_search_tool]

    system_prompt = (
    "You are a friendly, helpful AI chatbot.\n"
    "You remember earlier messages and use them for context.\n"
    "For queries requiring real-world facts, use the 'internet_search' tool."
    "Do NOT hallucinate real-world facts."
    "DO NOT include analysis, reasoning, analysis, or channel markers."
    "Do NOT include any end markers like [EOG], <EOG>, or channel tags."
    "You MUST respond ONLY with the final answer." 
    )
    
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt,
    )

    return agent

def build_history(messages):
        history = []
        for msg in messages:
            if msg["role"] == "user":
                history.append(HumanMessage(content=msg["content"]))
            else:
                history.append(AIMessage(content=msg["content"]))
        return history

# ----------------------------------
# Streamlit UI
# ----------------------------------
st.set_page_config(page_title="AI Chatbot Assistant", layout="centered")
st.title("💬 AI Chatbot")
st.write("Ask me anything!")

# Sidebar
st.sidebar.header("Example Prompts")
st.sidebar.write(
    """
    - Explain LLMs in simple terms
    - Write a polite email for leave
    - What is RAG architecture?
    - Summarize this text for me
    - Chat with me like a friend
    """
)

# Session state initialization
if "agent" not in st.session_state:
    try:
        with st.spinner("Loading AI model..."):
            llm = load_resources()
            st.session_state.agent = create_chatbot_agent(llm)
    except Exception as e:
        st.error("Failed to initialize agent")
        st.exception(e)
        st.stop()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

# ----------------------------------
# Robust agent output parser
# ----------------------------------
def _parse_agent_result(res: Any) -> str:
    if res is None:
        return "No response from agent."
    if isinstance(res, str):
        return res
    if isinstance(res, dict):
        if "output" in res:
            return res["output"]
        if "result" in res:
            return res["result"]
        if "final_output" in res:
            return res["final_output"]
        if "messages" in res and res["messages"]:
           last = res["messages"][-1]
           if hasattr(last, "content"):
            return last.content
        return str(last)
    return str(res)


# ----------------------------------
# Handle user interaction
# ----------------------------------
if user_input:
    # Show user message
    st.session_state.chat_history.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Build memory
    history = build_history(st.session_state.chat_history[:-1])

    with st.spinner("Thinking..."):
        try:
            result = st.session_state.agent.invoke(
                {"messages": history + [user_input]}
            )
            raw_output = _parse_agent_result(result)
            print("Raw output:", raw_output)
            cleaned = clean_agent_output(raw_output)
            print("Cleaned:",cleaned)
        except Exception as e:
            cleaned = f"Error: {str(e)}"

    # Stream output
    with st.chat_message("assistant"):
        final_text = stream_text(cleaned)
        print("Final text:", final_text)

    # Show assistant response
    st.session_state.chat_history.append(
        {"role": "assistant", "content": final_text}
    )

# Footer
st.markdown("---")
st.caption("Powered by SpiLLI")