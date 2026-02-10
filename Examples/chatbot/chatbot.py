import streamlit as st
from typing import Any
import requests
import re
import time
from pydantic import BaseModel, Field
from langchain_community.tools import Tool
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.agents import create_agent
from SpinLLM import SpinChatModel
from ddgs import DDGS

#Initialize SpiLLI
@st.cache_resource
def load_resources():
    llm=SpinChatModel(
        # model_name="Openai_Gpt Oss 20b",
        model_name ="Llama-3-Groq-8B-Tool-Use",
        encryption_path='./SpiLLI_Community.pem',
        temperature=0.8,
        max_tokens=512
    )

    return llm

def internet_search_fn(query: str) -> str:
    """Searches the internet using DuckDuckGo Instant Answer API
    Reliable internet search using DuckDuckGo Search.
    Returns top results with title and snippet.
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query,max_results =5))
        
        if not results:
            return "No results found."
        
        formatted = []
        for r in results:
            title = r.get("title", "")
            body = r.get("body", "")
            link = r.get("href", "")
            formatted.append(f"{title}\n{body}\nSource: {link}")
        
        return "\n\n".join(formatted)
        
    except Exception as e:
        return f"Internet search failed : {str(e)}"
    
class InternetSearchInput(BaseModel):
    query: str = Field(..., description="Search query for internet lookup")


def clean_agent_output(text: str) -> str:
    """
    Removes model channel tokens and end markers from agent output.
    """
    if not text:
        return text

    # Case 1: OSS token format
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

    internet_search_tool = Tool.from_function(
        name="internet_search",
        func=internet_search_fn,
        description="Search the internet for real-time information. Input should be a single search query string.",
    )

    tools = [echo_tool, internet_search_tool]
    
    agent = create_agent(
        model=llm,
        tools=tools,
    )

    return agent

def build_history(messages):
        system_prompt = """
            You are a friendly, helpful AI chatbot.
            Do NOT hallucinate real-world facts.
        """
        history = [SystemMessage(content= system_prompt)]
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
            print("Result:", result)
            raw_output = _parse_agent_result(result)
            print("Raw output:", raw_output)
            cleaned = clean_agent_output(raw_output)
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