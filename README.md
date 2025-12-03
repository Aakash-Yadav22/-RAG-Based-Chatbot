# RAG Chatbot – FastAPI, FAISS, Streamlit, Ollama

This project implements a Retrieval-Augmented Generation (RAG) chatbot using FAISS for vector search, FastAPI for backend services, and Streamlit for the frontend interface. The chatbot allows users to upload documents (PDF or TXT), processes and chunks them, generates embeddings using Ollama models, and answers queries using retrieved document context.

---

## Features

- Document upload support for PDF and TXT files
- Text extraction and chunking
- Vector embeddings generated using Ollama
- FAISS vector index for similarity search
- Retrieval-Augmented response generation
- REST API built with FastAPI
- Web UI built with Streamlit
- Modular, extensible architecture

---

## Project Structure

```
rag-chatbot/
│
├── backend/
│   ├── main.py
│   ├── utils.py
│   ├── requirements.txt
│   └── data/
│       └── docs/
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│
└── README.md
```

---

## Tech Stack

### Backend
- FastAPI
- FAISS CPU
- NumPy
- Ollama
- PyPDF2
- Python Multipart

### Frontend
- Streamlit
- Requests

---

## Prerequisites

Install the following:

- Python 3.11+
- Ollama installed and running locally
- A model pulled in Ollama (example: llama3)

Pull the model:

```
ollama pull llama3
```

---

## Setup Instructions

### 1. Backend Setup

```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run FastAPI:

```
python -m uvicorn main:app --reload --port 8000
```

Backend URL:

```
http://127.0.0.1:8000
```

---

### 2. Frontend Setup

```
cd frontend
source ../backend/venv/bin/activate
pip install -r requirements.txt
```

Run Streamlit:

```
streamlit run app.py
```

---

## API Endpoints

### POST /upload  
Uploads and indexes documents.

Response:
```
{
  "status": "indexed",
  "chunks": 35
}
```

---

### POST /query  
Queries the indexed data.

Request:
```
{
  "query": "What is the document about?"
}
```

Response:
```
{
  "answer": "Your summarized answer based on retrieved context."
}
```

---

## How It Works

1. User uploads documents via frontend.
2. Backend extracts text, chunks it, and generates embeddings.
3. FAISS index is created.
4. Query text is embedded and matched against document chunks.
5. Retrieved context is passed to the LLM via Ollama.
6. Model returns a context-based answer.

---

## Troubleshooting

### Ollama Port Already in Use
```
ps aux | grep ollama
kill -9 <PID>
```

### FAISS or NumPy Errors  
Ensure compatibility:
```
pip install numpy==1.26.4
pip install faiss-cpu==1.7.4
```

-----

## Future Enhancements

- More file formats
- Multi-user support
- Persistent vector database
- Secured API with authentication
- Docker containerization

---

