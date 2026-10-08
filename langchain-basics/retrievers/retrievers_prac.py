from langchain_chroma import Chroma
from langchain_community.retrievers import WikipediaRetriever
from langchain_openai import OpenAIEmbeddings

retrievers = WikipediaRetriever(top_k_results=2, lang="en")
query = (
    "the geopolitical history of india and pakistan from the perspective of a chinese"
)

docs = retrievers.invoke(query)
# Print retrieved content
for i, doc in enumerate(docs):
    print(f"\n---- Result {i+1} ")
    print(f"Content :\n {doc.page_content}....")
