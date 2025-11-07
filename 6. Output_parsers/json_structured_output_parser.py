from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

schema = [
    ResponseSchema(name="fact_1", description="fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give 3 Facts about {topic} \n {format_instructions}",
    input_variables=['topic'],
    partial_variables={"format_instructions": parser.get_format_instructions()} 
)

# ------------ approach 1 ------------------------
# prompt = template.invoke({'topic': 'black hole'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)



# ------------ approach 2 ------------------------
chain = template | model | parser

result = chain.invoke({'topic': 'black hole'})

print(result)