from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

# Load env from project root
load_dotenv(dotenv_path="../.env")

llm = OpenAI(
    model="gpt-4.1-nano",          # model shown in your EURI dashboard
    api_key=os.getenv("OPEN_API_KEY"),
    base_url="https://api.euron.one/api/v1/euri"
)

response = llm.invoke("What is the capital of India?")
print(response.content)
