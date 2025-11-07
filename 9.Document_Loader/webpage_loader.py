from langchain_community.document_loaders import WebBaseLoader

url = "https://medium.com/@adevnadia/react-state-management-in-2025-what-you-actually-need-a138da90dbec"

loader = WebBaseLoader(url)
# loader = WebBaseLoader([url,url,url]) # Here we can pass list of url also for multiple different pages data

docs = loader.load()

print(docs)