from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

document = [
    "Virat kohli is an indian cricketer known for his aggressive batting and leadership.",
    "Ms Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit sharma is known for his elegant batting record-breaking double centuries",
    "Jasprit Bumrah is an indian fast bowler known for his unorthodox action and yorkers.",
]

query = "Tell me about raza?"

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

docs_vector = embedding.embed_documents(document)
query_vector = embedding.embed_query(query)

scores = cosine_similarity([query_vector], docs_vector)[0] #its mandatory to send query_vector in 2 dimension because docs_vector is already in 2 dimensions.

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

if score < 0.35:
    print("Don't know about the one you are asking.")
else:
    print(query)
    print(document[index])
    print("Similarity score is: ", score)