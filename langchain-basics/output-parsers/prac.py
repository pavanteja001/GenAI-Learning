from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv("../.env")

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.3,
    max_tokens=150,
)

response = llm.invoke("write 5 lines on hyderabad tourism")
print(response.content)
