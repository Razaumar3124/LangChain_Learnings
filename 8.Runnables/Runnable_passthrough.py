from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate tweet about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a linkedin post about {topic}",
    input_variables=["topic"]
)

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7,max_tokens=250)

parser = StrOutputParser()

joke_gene_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    "explanation": RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gene_chain, parallel_chain)
result = final_chain.invoke({'topic': 'black hole'})
print(result)