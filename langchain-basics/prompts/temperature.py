from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv("../.env")

llm = ChatOpenAI(
    model="gpt-4.1-nano",
    base_url="https://api.euron.one/api/v1/euri",
    api_key= os.getenv("OPENAI_API_KEY"),
    temperature=0.7
)

response = llm.invoke("who is virat kohili")
print(response.content)