from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"

)
texts = [
    "Hello this is Avinash"
    "Creating few Embeddings from a text"
]



vector = embedding.embed_documents(texts)

print(vector)