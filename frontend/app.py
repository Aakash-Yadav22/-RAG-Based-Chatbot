import streamlit as st
import requests

API = "http://localhost:8000"

st.title("📚 RAG Chatbot (Ollama + Llama 3)")

st.subheader("Upload PDF/TXT files")
files = st.file_uploader(
    "Upload documents",
    type=["pdf", "txt"],
    accept_multiple_files=True
)

if st.button("Build Knowledge Base"):
    if files:
        send_files = [("files", (f.name, f.getvalue(), f.type)) for f in files]
        res = requests.post(f"{API}/upload", files=send_files)
        st.success("Index created!")
        st.json(res.json())
    else:
        st.error("Please upload at least one file.")


st.subheader("Ask a Question")
query = st.text_input("Your question:")

if st.button("Send"):
    res = requests.post(f"{API}/query", json={"query": query}).json()
    st.write("### Answer:")
    st.write(res["answer"])
