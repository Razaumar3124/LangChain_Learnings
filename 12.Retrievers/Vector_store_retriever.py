from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

loader = TextLoader("IPLData.txt", encoding="utf-8")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 0,
    separators=["\n\n", "\n", "_", ""]
)

split_docs = splitter.split_documents(docs)

vector_store = Chroma(
    embedding_function=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2"),
    persist_directory="smaple_data",
    collection_name="chromadb"
)

# vector_store.add_documents(split_docs)

retriever = vector_store.as_retriever(search_kwargs={"k": 3})

query = "who is the best baller of india?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)
