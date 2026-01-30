from typing import Any, Dict, List, Optional, Union
from langchain.chat_models.base import BaseChatModel
from langchain.messages import AIMessage, HumanMessage, SystemMessage, ToolCall, ToolMessage
from langchain_core.messages import BaseMessage
from langchain_core.outputs.chat_result import ChatResult
from langchain_core.outputs import ChatGeneration
from SpiLLI.SpinLLI import Spin
import json
import re
import asyncio

class SpinChatModel(BaseChatModel):
    """
    Chat-based wrapper for Spin backend, compatible with LangChain agents and tools.
    """

    model_name: str
    temperature: float = 0.7
    max_tokens: int = 2048
    encryption_path: str = ""
    kwargs: Dict[str, Any] = {}
    llm: Any = None
    spin: Any = None

    tools: Optional[List[Any]] = None  # Tool objects or dicts
    tool_choice: Any = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spin = Spin(self.encryption_path)
        self.llm = self.spin.request({"model": self.model_name})

    # -----------------------------
    # LangChain ChatModel interface
    # -----------------------------
    async def _agenerate(
        self, messages: List[BaseMessage], stop: Optional[List[str]] = None, **kwargs
    ) -> ChatResult:
        """
        Converts messages to a prompt, runs Spin, and returns a ChatResult with AIMessage.
        """
        prompt = self._convert_messages_to_prompt(messages)
        response_text = await self._call_spin(prompt)
        # Detect LangChain-style tool call
        action_match = re.search(r"Action:\s*(\w+)", response_text)
        input_match = re.search(r"Action Input:\s*(\{.*\})", response_text, re.DOTALL)
    
        if action_match and input_match:
            tool_name = action_match.group(1)
            try:
                tool_args = json.loads(input_match.group(1))
            except json.JSONDecodeError:
                tool_args = {"input": input_match.group(1)}
    
            tool_call = ToolCall(
                id=f"call_{tool_name}_{hash(response_text) % 10000}",
                name=tool_name,
                args=tool_args,
            )
            msg = AIMessage(content="", tool_calls=[tool_call])
        else:
            msg = AIMessage(content=response_text)
        return ChatResult(generations=[ChatGeneration(message=msg)])
    def _generate(
        self, messages: List[BaseMessage], stop: Optional[List[str]] = None, **kwargs
    ) -> ChatResult:
        """
        Converts messages to a prompt, runs Spin, and returns a ChatResult with AIMessage.
        """
        prompt = self._convert_messages_to_prompt(messages)
        response_text = asyncio.run(self._call_spin(prompt))
        # Detect LangChain-style tool call
        action_match = re.search(r"Action:\s*(\w+)", response_text)
        input_match = re.search(r"Action Input:\s*(\{.*\})", response_text, re.DOTALL)
    
        if action_match and input_match:
            tool_name = action_match.group(1)
            try:
                tool_args = json.loads(input_match.group(1))
            except json.JSONDecodeError:
                tool_args = {"input": input_match.group(1)}
    
            tool_call = ToolCall(
                id=f"call_{tool_name}_{hash(response_text) % 10000}",
                name=tool_name,
                args=tool_args,
            )
            msg = AIMessage(content="", tool_calls=[tool_call])
        else:
            msg = AIMessage(content=response_text)
        return ChatResult(generations=[ChatGeneration(message=msg)])
    async def _call_spin(self, prompt: str) -> str:
        """
        Sends the prompt to Spin backend and returns the response.
        Augments prompt with tools if any are bound.
        """
        payload = {"prompt":"","query": prompt}

        if self.tools:
            tool_text = self._format_tools(self.tools)
            payload["query"] = tool_text + "\n\n" + prompt
        # print('Payload: ',payload)
        return await self.llm.run(payload)

    def _convert_messages_to_prompt(self, messages: list) -> str:
        text = ""
        for m in messages:
            if isinstance(m, SystemMessage):
                text += f"[SYSTEM] {m.content}\n"
            elif isinstance(m, HumanMessage):
                text += f"[USER] {m.content}\n"
            elif isinstance(m, ToolMessage):
                text += f"[TOOL OUTPUT for {m.name}] {m.content}\n"
            elif isinstance(m, AIMessage):
                # AIMessage can have either normal text or tool calls
                if hasattr(m, "tool_calls") and m.tool_calls:
                    for tc in m.tool_calls:
                        text += f"[ASSISTANT CALL] {tc['name']} with {tc['args']}\n"
                else:
                    text += f"[ASSISTANT] {m.content}\n"
            else:
                text += f"[OTHER] {getattr(m, 'content', str(m))}\n"
        return text

    def _format_tools(self, tools: List[Any]) -> str:
        formatted = ["You have access to the following tools:"]
        for tool in tools:
            if isinstance(tool, dict):
                name = tool.get("name", "")
                description = tool.get("description", "")
            else:
                name = getattr(tool, "name", "")
                description = getattr(tool, "description", "")
            formatted.append(f"\nTool name: {name}\nDescription: {description}")
    
        formatted.append(
            "\nWhen you want to use a tool, respond ONLY in this format:\n"
            "Action: <tool name>\n"
            "Action Input: <JSON string of the input>\n"
            "Do not write anything else. If you already know the answer from previous tool outputs or conversation history, dont call any tools and just respond with the answer."
        )
        return "\n".join(formatted)

    # -----------------------------
    # Tool binding
    # -----------------------------
    def bind_tools(self, tools: List[Any], tool_choice=None, **kwargs):
        """
        Returns a cloned instance of the model with tools bound.
        Compatible with LangChain agents.
        """
        new = self.copy()
        new.tools = tools
        new.tool_choice = tool_choice
        # Apply any additional LLM overrides
        for k, v in kwargs.items():
            setattr(new, k, v)
        return new

    # -----------------------------
    # LangChain metadata
    # -----------------------------
    @property
    def _identifying_params(self) -> Dict[str, Any]:
        return {
            "model_name": self.model_name,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }

    @property
    def _llm_type(self) -> str:
        return "spin+" + self.model_name


# -----------------------------
# Usage example
# -----------------------------
if __name__ == "__main__":
    from langchain_community.tools import Tool
    from langchain_community.tools.file_management.read import ReadFileTool

    # Define some example tools
    calculator_tool = Tool.from_function(
        func=lambda x: str(eval(x)), name="Calculator", description="Evaluates math expressions"
    )
    file_read_tool = ReadFileTool()

    tools = [calculator_tool, file_read_tool]

    # Initialize model
    llm = SpinChatModel(model_name="my_custom_model", encryption_path="...")

    # Bind tools
    llm_with_tools = llm.bind_tools(tools)

    # Now llm_with_tools can be used with LangChain agents
    from langchain.agents import create_agent

    agent = create_agent(model=llm_with_tools, tools=tools)

    # Example agent call
    inputs = {"messages": [{"role": "user", "content": "What is 23 + 42?"}]}
    result = agent.invoke(inputs)
    print(result)