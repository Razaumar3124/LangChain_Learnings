from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="industry.csv")

docs = loader.load()

print(docs[0])
