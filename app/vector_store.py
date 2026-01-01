import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from app.config import PROCESSED_DIR

VECTOR_DB_PATH = "data/faiss_index"
MODEL_NAME = "all-MiniLM-L6-v2"


def load_documents():
    texts = []
    for file in os.listdir(PROCESSED_DIR):
        if file.endswith(".txt"):
            with open(os.path.join(PROCESSED_DIR, file), "r", encoding="utf-8") as f:
                texts.append(f.read())
    return texts


def create_vector_store():
    texts = load_documents()
    if not texts:
        raise ValueError("No documents found in processed directory")

    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(texts, show_progress_bar=True)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    os.makedirs(VECTOR_DB_PATH, exist_ok=True)

    faiss.write_index(index, os.path.join(VECTOR_DB_PATH, "index.faiss"))
    with open(os.path.join(VECTOR_DB_PATH, "texts.pkl"), "wb") as f:
        pickle.dump(texts, f)


def load_vector_store():
    model = SentenceTransformer(MODEL_NAME)

    index = faiss.read_index(os.path.join(VECTOR_DB_PATH, "index.faiss"))
    with open(os.path.join(VECTOR_DB_PATH, "texts.pkl"), "rb") as f:
        texts = pickle.load(f)

    return index, texts, model
