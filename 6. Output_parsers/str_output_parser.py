from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

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

prompt1 = template1.invoke({'topic': 'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'topic': result.content})

result1 = model.invoke(prompt2)

print(result1.content)