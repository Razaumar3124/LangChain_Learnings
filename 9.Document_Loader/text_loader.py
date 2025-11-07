from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader("sample.txt", encoding="utf-8")

docs = loader.load()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7,max_tokens=250)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Summarize the following text: \n {text}",
    input_variables=['text']
)

chain = prompt | model | parser

result = chain.invoke({'text': docs[0].page_content})
print(result)