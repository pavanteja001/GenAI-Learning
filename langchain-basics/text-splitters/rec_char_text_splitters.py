from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    "/Users/pavanteja/Datascience/langchain/text-splitters/dl-curriculum.pdf"
)

text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""

docs = loader.load()

splitter1 = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=25,
)

chunks1 = splitter1.split_documents(docs)
chunks2 = splitter1.split_text(text)

print(f"Total pages loaded {len(docs)}")
print(f"total chunks created {len(chunks1)}")
print(f"\n----sample chunk ---\n {chunks1[0].page_content}")
print(f"\n-- Metadata --\n{chunks1[0].metadata}")
print(f"total chunks created {len(chunks2)}")
print(f"\n----sample chunk ---\n {chunks2[0]}")
