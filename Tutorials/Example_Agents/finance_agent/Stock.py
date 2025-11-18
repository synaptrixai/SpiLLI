import streamlit as st
import yfinance as yf
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from langchain_community.tools import Tool
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_agent
from typing import Dict, List, Any
from SpinLLM import SpinChatModel

def clean_and_format_output(text: str) -> str:
    
    if not text:
        return "No output generated."

    # ----------- Basic text cleanup -----------
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)       # Fix merged words: NetIncomewas → Net Income was
    text = re.sub(r"([0-9])([A-Za-z])", r"\1 \2", text)    # 281.72billion → 281.72 billion
    text = re.sub(r"([A-Za-z])([0-9])", r"\1 \2", text)
    text = re.sub(r"\s+", " ", text).strip()               # Normalize spaces

    # Detect financial section
    financial_keywords = ["revenue", "net income", "operating income", "financial"]
    is_financial = any(k in text.lower() for k in financial_keywords)

    # --- If not financial, return raw cleaned text ---
    if not is_financial:
        return f"### 📝 Summary\n• {text}"

    # --- Extract values using regex ---
    # Example match: "Revenue was 281.72 billion"
    pattern = r"(Revenue|Net Income|Operating Income)[^\d]*([\d.,]+)\s*billion"
    matches = re.findall(pattern, text, flags=re.IGNORECASE)

    # Build dictionary: {"Revenue": [198.27, 281.72], ...}
    metrics_dict = {}

    for label, value in matches:
        label = label.title()
        value = float(value.replace(",", ""))
        metrics_dict.setdefault(label, []).append(value)
        
    # If no metrics detected → fallback
    if not metrics_dict:
        return f"### 📈 Financial Metrics\n• {text}"
    
    # ----------- Generate narrative bullet points -----------
    bullets = []

    for metric, values in metrics_dict.items():
        if len(values) >= 2:
            start_val = values[0]
            end_val = values[-1]
            bullets.append(
                f"• {metric} increased from {start_val} billion to {end_val} billion."
            )
        else:
            bullets.append(f"• {metric}: {values[0]} billion.")
    
    # ----------- Return formatted output -----------
    return "### 📈 Financial Metrics\n" + "\n".join(bullets)

#Initialize SpiLLI
@st.cache_resource
def load_model():
    llm=SpinChatModel(
       model_name="llama3-groq-tool-use:8b",
       encryption_path='./SpiLLI.pem',
       temperature=0.8,
       max_tokens=512
    )
    return llm

#Custom tools for the agent
def _get_info_from_yf(ticker: str) -> dict:
    """Helper to safely fetch info from yfinance."""
    ticker = ticker.strip().upper()
    stock = yf.Ticker(ticker)
    try:
        return stock.info or {}
    except Exception:
        return {}

def get_stock_price_fn(ticker: str) -> dict[str, Any]:
    """Returns live stock price, previous close, volume, and 52-week data."""
    info = _get_info_from_yf(ticker)
    return {
        "ticker": ticker,
        "currentPrice": info.get("currentPrice"),
        "previousClose": info.get("previousClose"),
        "open": info.get("open"),
        "dayHigh": info.get("dayHigh"),
        "dayLow": info.get("dayLow"),
        "volume": info.get("volume"),
        "marketCap": info.get("marketCap"),
        "fiftyTwoWeekHigh": info.get("fiftyTwoWeekHigh"),
        "fiftyTwoWeekLow": info.get("fiftyTwoWeekLow"),
    }

def get_stock_financials_fn(ticker: str) -> dict[str, Any]:
    """Returns revenue, net income, and operating income."""
    ticker = ticker.strip().upper()
    stock = yf.Ticker(ticker)
    try:
        financials = stock.financials
        return{
            "Revenue": financials.loc["Total Revenue"].to_dict() if "Total Revenue" in financials.index else{},
            "Net Income": financials.loc["Net Income"].to_dict() if "Net Income" in financials.index else{},
            "Operating Income": financials.loc["Operating Income"].to_dict() if "Operating Income" in financials.index else{},
        }
    except Exception:
        return{"error": "Unable to fetch financial data or financial table missing."}

def get_company_profile_fn(ticker: str) -> dict[str, Any]:
    """Returns company name, sector, industry, website, and business summary."""
    info = _get_info_from_yf(ticker)
    return {
        "ticker": ticker.strip().upper(),
        "name": info.get("longName"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "website": info.get("website"),
        "summary": info.get("longBusinessSummary"),
    }

class AutoFormattingAgentWrapper:
    """Wraps a LangChain agent and automatically formats output."""

    def __init__(self, agent):
        self.agent = agent

    def invoke(self, inputs):
        try:
            result = self.agent.invoke(inputs)
        except Exception as e:
            return {"formatted": f"⚠️ Agent Error: {str(e)}"}

        # Extract LLM text
        output =""

        if isinstance(result, dict):
            msg = result.get("messages", [])
            if msg and hasattr(msg[-1], "content"):
                output = msg[-1].content
            else:
                output = result.get("output", "")
        else:
            output = str(result)
        
        if output is None:
            output =""

        # Auto-format
        formatted = clean_and_format_output(output)

        # Return in LangChain format
        return {"formatted": formatted}

#Create the agent
def create_stock_agent(llm):
    # Wrap functions as Tools for LangGraph
    get_stock_price = Tool.from_function(name="get_stock_price", func=get_stock_price_fn, description="Get live stock price and intraday summary for a ticker")
    get_stock_financials = Tool.from_function(name="get_stock_financials", func=get_stock_financials_fn, description="Return key financial statement rows for a ticker")
    get_company_profile = Tool.from_function(name="get_company_profile", func=get_company_profile_fn, description="Get company profile information (sector, industry, summary)")
    
    tools = [get_stock_price, get_stock_financials, get_company_profile]

    agent = create_agent(
        model=llm,
        tools=tools,
    )
    # Wrap with auto-formatter
    return AutoFormattingAgentWrapper(agent)

#Streamlit UI
st.set_page_config(page_title="AI Stock Research Assistant", layout="wide")
st.title('AI Stock Research Assisstant')
st.write('Ask me anything about stocks! 📈')

#Initialize session state
if 'agent' not in st.session_state:
    with st.spinner('Loading AI model...'):
        llm = load_model()
        st.session_state.agent = create_stock_agent(llm)

#User input
user_question = st.text_input(" ", key="user_query")  

if user_question:
    with st.spinner('Analyzing...'):
        try:
            result = st.session_state.agent.invoke({"messages": user_question})
            formatted_output = result.get("formatted", "No output produced.")
            print(result)
            st.subheader("Result")
            st.markdown(formatted_output)
        except Exception as e:
            st.error(f"Error: {str(e)}")

st.caption("Powered by SpiLLI")

#Example questions
st.sidebar.header("Sample Queries ")
st.sidebar.write("""
- Stock Price: What's the current stock price of AAPL?
- Stock Financial: What are the key financial metrics for MSFT?
- Comapny Profile: Provide a company profile for NVDA.
- Compare the fundamentals of AMD vs INTC.
""")
