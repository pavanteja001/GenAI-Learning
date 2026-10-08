from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2b-it",
    task="text-generation",
    max_new_tokens=128,
)

result = llm.invoke("What is the capital of India?")
print(result)