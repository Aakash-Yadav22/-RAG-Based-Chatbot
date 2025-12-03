import os
import faiss
from sentence_transformers import SentenceTransformer
from utils import extract_text_from_pdf, extract_text_from_txt, chunk_text

model = SentenceTransformer("all-MiniLM-L6-v2")

docs = "data/docs/"
chunks = []

for file in os.listdir(docs):
    path = docs + file

    if file.endswith(".pdf"):
        text = extract_text_from_pdf(path)
    else:
        text = extract_text_from_txt(path)

    chunks.extend(chunk_text(text))

emb = model.encode(chunks)
index = faiss.IndexFlatL2(emb.shape[1])
index.add(emb)

os.makedirs("vectorstore", exist_ok=True)

faiss.write_index(index, "vectorstore/index.faiss")

with open("vectorstore/chunks.txt", "w", encoding="utf-8") as f:
    f.writelines([c + "\n" for c in chunks])

print("Index created")
