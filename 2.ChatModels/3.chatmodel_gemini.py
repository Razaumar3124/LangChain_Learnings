from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="models/gemini-2.5-pro")

result = model.invoke("what is the largest animal in india?")

print(result.content)
