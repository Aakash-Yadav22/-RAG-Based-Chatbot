# Optional helper engine (not used when PDFs upload from UI)
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class RAGEngine:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.read_index("vectorstore/index.faiss")
        with open("vectorstore/chunks.txt", "r", encoding="utf-8") as f:
            self.chunks = f.readlines()

    def search(self, query, top_k=3):
        q_emb = self.model.encode([query])
        distances, idx = self.index.search(np.array(q_emb), top_k)
        return [self.chunks[i] for i in idx[0]]
