from app.vector_store import load_vector_store
from app.config import TOP_K
import numpy as np


class Retriever:
    def __init__(self):
        self.index, self.texts, self.model = load_vector_store()

    def get_relevant_docs(self, query):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, TOP_K)

        results = []
        for idx in indices[0]:
            results.append(self.texts[idx])

        return results



