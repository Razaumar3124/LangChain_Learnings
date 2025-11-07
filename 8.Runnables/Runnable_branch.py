from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda, RunnableBranch
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="write a detailed report about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following text \n {text}",
    input_variables=["text"]
)

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7,max_tokens=250)

parser = StrOutputParser()

report_gene_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 100, prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = report_gene_chain | branch_chain

result = final_chain.invoke({'topic': 'black hole'})

print(result)