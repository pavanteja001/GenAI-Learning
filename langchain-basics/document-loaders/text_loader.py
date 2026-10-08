from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv("../.env")

model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.2, max_tokens=150)

parser = StrOutputParser()

loader = TextLoader(
    "/Users/pavanteja/Datascience/langchain/document-loaders/cricket.txt",
    encoding="utf-8",
)
docs = loader.load()

print(docs)
print(docs[0].page_content)  # will show your text once the file isn't empty

print(loader)
