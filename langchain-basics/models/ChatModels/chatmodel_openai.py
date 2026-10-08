from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load env from project root
load_dotenv(dotenv_path="../.env")

llm = ChatOpenAI(
    model="gpt-4.1-nano",          # model shown in your EURI dashboard
    api_key=os.getenv("EURI_API_KEY"),
    base_url="https://api.euron.one/api/v1/euri",
    temperature=2,
    max_completion_tokens = 2000
)

response = llm.invoke(" Who is has most runs in single edition of ipl ")
print(response.content) 
