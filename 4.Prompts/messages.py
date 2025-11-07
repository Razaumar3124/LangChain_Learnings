from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=api_key,
    temperature=0.3,
)

model = ChatHuggingFace(llm=llm)

messages = [
    SystemMessage(content="You are a  helpful assistant"),
    HumanMessage(content="Tell me about langchain"),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages[2])