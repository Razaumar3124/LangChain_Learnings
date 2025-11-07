from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional

load_dotenv()

# Schema
class Student(BaseModel):
    name: str = "akhilya"
    age: Optional[int] = None
    cgpa: float = Field(gt=0, lt=10, default=5, description="A decimal value representing the cgpa of the student")
    
new_student = {'name': "shinde", "age": 32, "cgpa": 8}
# new_student = {'name': 32}   #here we will get error because pydantic is expecting str not int
# new_student = {}

student = Student(**new_student)
print(student)
print(type(student))

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)