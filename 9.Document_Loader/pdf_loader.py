from langchain_community.document_loaders import PyMuPDFLoader
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

pdfLoader = PyMuPDFLoader("sample.pdf")

print(pdfLoader.load())

# model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7,max_tokens=250)

# parser = StrOutputParser()