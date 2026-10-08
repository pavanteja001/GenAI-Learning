from langchain_community import retrievers
from langchain_community.vectorstores import FAISS  # facebook VS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_core.documents import Document

# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(
        page_content="MMR helps you get diverse results when doing similarity search."
    ),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]
load_dotenv("../.env")

embeddings = OpenAIEmbeddings()

vector_store = FAISS.from_documents(documents=docs, embedding=embeddings)

retriever = vector_store.as_retriever(
    search_type="mmr",  # <-- This switches the retriever from plain similarity search to Maximal Marginal Relevance 
    search_kwargs={
        "k": 3,#it's your final result count.
        "lambda_mult": 0.5,
    },  # k = top results, lambda_mult = relevance-diversity balance
)

query = "what is langchain"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)

#1.0 → pure relevance. MMR collapses into ordinary similarity search; diversity is ignored.
#0.0 → pure diversity. Documents are spread as far apart as possible, almost disregarding how well they match the query.
#0.5 → balanced (your setting, and the LangChain default). Each pick weighs "relevant to query" and "different from what I've already chosen" equally.


