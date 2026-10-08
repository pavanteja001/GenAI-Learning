from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv("../.env")

llm = ChatOpenAI()


@tool
def multiply(a: int, b: int) -> int:
    "Given 2 numbers a and b this tool returns their product"
    return a * b


llm_with_tool = llm.bind_tools([multiply])
msg1 = llm_with_tool.invoke("Hi how are you")
print(msg1)

msg2 = llm_with_tool.invoke("what is 3 times 4")
print(msg2)
print(msg2.tool_calls)
