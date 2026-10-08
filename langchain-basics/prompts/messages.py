from langchain_core.messages import HumanMessage, SystemMessage, AIMessage 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv("../.env")

model = ChatOpenAI(
    model="gpt-4.1-nano",
    base_url="https://api.euron.one/api/v1/euri",
    api_key= os.getenv("OPENAI_API_KEY"),
    temperature=0.7
)

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
