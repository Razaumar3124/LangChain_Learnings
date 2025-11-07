from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="directory",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

# ------------- Load will try to get all the data at once and display it -------------------------

# docs = loader.load() #Here it will take time bcz it will try to get all the data at once.

# print(len(docs))
# print(docs[0].page_content)

# for document in docs:
#     print(document)

# --------- Lazy load is used when we have larger amount of data it will give data in the form of generator it will give data one at a time ------------------------

docs = loader.lazy_load() #Here it will take time bcz it will try to get all the data at once.

print(len(docs))
print(docs[0].page_content)

for document in docs:
    print(document)