import os
import faiss
import numpy as np
from fastapi import FastAPI, UploadFile, File
from utils import extract_text_from_pdf, extract_text_from_txt, chunk_text
import ollama

app = FastAPI()

chunks_list = []
index = None


def embed_text(texts):
    response = ollama.embed(
        model="llama3",
        input=texts
    )
    return np.array(response["embeddings"])


@app.post("/upload")
async def upload_docs(files: list[UploadFile] = File(...)):
    global chunks_list, index

    chunks_list = []
    docs_folder = "data/docs/"
    os.makedirs(docs_folder, exist_ok=True)

    for file in files:
        path = docs_folder + file.filename

        with open(path, "wb") as f:
            f.write(await file.read())

        if file.filename.endswith(".pdf"):
            text = extract_text_from_pdf(path)
        else:
            text = extract_text_from_txt(path)

        chunks_list.extend(chunk_text(text))

    embeddings = embed_text(chunks_list)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return {"status": "indexed", "chunks": len(chunks_list)}


@app.post("/query")
async def query(data: dict):
    global index, chunks_list

    if index is None:
        return {"answer": "⚠ Upload documents first."}

    q = data["query"]
    q_emb = embed_text([q])

    _, idx = index.search(q_emb, 3)

    retrieved_chunks = "\n".join([chunks_list[i] for i in idx[0]])

    prompt = f"""
You are an AI assistant answering ONLY from the provided context.

Context:
{retrieved_chunks}

User question:
{q}

Answer:
"""

    response = ollama.generate(
        model="llama3",
        prompt=prompt
    )

    return {"answer": response["response"]}
