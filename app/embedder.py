import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

CHUNK_DIR = "data/chunks"
MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

embeddings = []
metadata = []

for file in os.listdir(CHUNK_DIR):
    if not file.endswith(".txt"):
        continue

    with open(os.path.join(CHUNK_DIR, file), "r", encoding="utf-8") as f:
        content = f.read()

    chunks = content.split("[CHUNK")
    for i, chunk in enumerate(chunks):
        chunk = chunk.strip()
        if len(chunk) < 100:
            continue

        emb = model.encode(chunk)
        embeddings.append(emb)
        metadata.append({
            "paper": file.replace("_chunks.txt", ""),
            "chunk_id": i,
            "text": chunk
        })

# 🔑 CRITICAL FIX: list → numpy array
embeddings = np.array(embeddings).astype("float32")

dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embeddings)

os.makedirs("vectorstore", exist_ok=True)
faiss.write_index(index, "vectorstore/faiss.index")

with open("vectorstore/metadata.pkl", "wb") as f:
    pickle.dump(metadata, f)

print(f"✅ Stored {len(embeddings)} embeddings successfully")



