from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

template1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="write a 5 lines summary on the following text. /n {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic": "black hole"})

print(result)