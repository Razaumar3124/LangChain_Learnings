import os
import requests
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv()

search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
    """
    This function fetches the current weather data for a given city
    """
    url = f"https://api.weatherstack.com/current?access_key=5d34b961c11e7bcce02ef5a4b1878308&query={city}"
    
    response = requests.get(url)
    return response.json()

llm = ChatGroq(model="llama-3.1-8b-instant")
# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True,
)

response = agent_executor.invoke({"input": "Find the capital of maharashtra, then find it's current weather condition"})

print(response)
print(response['output'])