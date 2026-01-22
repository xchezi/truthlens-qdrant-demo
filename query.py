from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

client = QdrantClient(host="localhost", port=6333)
model = SentenceTransformer("all-MiniLM-L6-v2")

query = input("Enter claim to verify: ")

query_vector = model.encode(query).tolist()

results = client.search(
    collection_name="truthlens",
    query_vector=query_vector,
    limit=3
)

print("\nRetrieved Evidence:\n")
for r in results:
    print("-", r.payload["content"])
