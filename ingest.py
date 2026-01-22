from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

client = QdrantClient(host="localhost", port=6333)
model = SentenceTransformer("all-MiniLM-L6-v2")

COLLECTION = "truthlens"

client.recreate_collection(
    collection_name=COLLECTION,
    vectors_config={"size": 384, "distance": "Cosine"},
)

with open("sample_data/articles.txt", "r") as f:
    texts = f.readlines()

embeddings = model.encode(texts)

points = []
for i, (text, vector) in enumerate(zip(texts, embeddings)):
    points.append({
        "id": i,
        "vector": vector.tolist(),
        "payload": {
            "content": text.strip(),
            "type": "text"
        }
    })

client.upsert(collection_name=COLLECTION, points=points)

print("Ingestion completed successfully.")
