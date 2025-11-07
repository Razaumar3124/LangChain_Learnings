from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="Name of the city of the person belongs to")
    
parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of the fictional {place} person \n {format_instructions} ",
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()} 
)

# prompt = template.invoke({"place": "indian"})

# print(prompt)

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)

# ------------- approach 2 ----------------------------
chain = template | model | parser

result = chain.invoke({'place': 'indian'})

print(result)
print(type(result))