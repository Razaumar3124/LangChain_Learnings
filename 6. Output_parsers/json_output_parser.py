from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me a name, age and city of a fictional person \n {format_instructions}",
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

# -------- 1st approach (hard coding) ----------------

# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)
# print(type(final_result))

# ------------ 2nd approach (ease coding) ---------------

chain = template | model | parser

result = chain.invoke({}) # i have to pass blank dict bcz my template consists input_variable as blank [].

print(result)