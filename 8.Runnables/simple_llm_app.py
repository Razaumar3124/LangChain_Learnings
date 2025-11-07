from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7, max_tokens=150)

prompt = PromptTemplate(
    template="Suggest a catchy blog title about {topic}",
    input_variables=['topic']
)

topic = str(input("Enter a topic: "))

formatted_prompt = prompt.format(topic=topic)

blog_title = model.predict(formatted_prompt)

print("Generate Blog Title: ", blog_title)