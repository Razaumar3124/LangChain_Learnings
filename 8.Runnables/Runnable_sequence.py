from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="write a joke about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="explain the following joke {text}",
    input_variables=["text"]
)

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7,max_tokens=250)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result = chain.invoke({"topic": "AI"})

print(result)