from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="write a joke about {topic}",
    input_variables=["topic"]
)

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7,max_tokens=250)

parser = StrOutputParser()

joke_gene_chain = RunnableSequence(prompt1, model, parser)

def word_count(text):
    return len(text.split())

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'length': RunnableLambda(word_count),
    # 'length': RunnableLambda(lambda x: len(x.split())) alternate way for finding length
})

final_chain = RunnableSequence(joke_gene_chain, parallel_chain)

result = final_chain.invoke({'topic': 'black hole'})
print(result)