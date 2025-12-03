# 📚 RAG Chatbot (Llama 3 + FAISS + FastAPI + Streamlit)

This is a fully functional Retrieval-Augmented Generation (RAG) chatbot that:

✔ Accepts PDF/TXT uploads  
✔ Automatically extracts text  
✔ Builds FAISS vector index  
✔ Answers questions using Llama 3  
✔ Provides a Streamlit interface  

---

## 🚀 How to Run

### 1. Start Backend

cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

shell
Copy code

### 2. Start Frontend

cd frontend
pip install -r requirements.txt
streamlit run app.py

yaml
Copy code

---

## 📂 Features

- PDF + TXT Upload
- Auto Indexing
- FAISS Similarity Search
- Llama 3 Local LLM
- Real Chat UI

---

## 🧩 Tech Stack

- Python  
- FastAPI  
- Streamlit  
- FAISS  
- Sentence Transformers  
- llama-cpp-python  