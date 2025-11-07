from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain.retrievers.multi_query import MultiQueryRetriever
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader("Multi_query.txt", encoding="utf-8")

docs = loader.load()

spliter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separators=["\n\n", "\n", "_", ""]
)
  
split_docs = spliter.split_documents(docs)

vector_store = FAISS.from_documents(documents=split_docs, embedding=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2"))

similarity_retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})

multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vector_store.as_retriever(search_kwargs={"k": 5}),
    llm=ChatGroq(model="llama-3.1-8b-instant")
)

query = "How to improve energy levels and maintain balance?"

similarity_result = similarity_retriever.invoke(query)
multiquery_result = multiquery_retriever.invoke(query)

for i, doc in enumerate(similarity_result):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)
    
print("*"*150)

for i, doc in enumerate(multiquery_result):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)