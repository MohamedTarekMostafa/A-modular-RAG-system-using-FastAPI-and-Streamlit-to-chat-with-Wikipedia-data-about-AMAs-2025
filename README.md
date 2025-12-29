#  RAG Wikipedia Assistant (AMAs 2025 Edition)
(![WhatsApp Image 2025-12-29 at 2 03 45 AM](https://github.com/user-attachments/assets/d3434113-dfc7-4fff-8916-c7ccaf600585))


A full-stack **RAG (Retrieval-Augmented Generation)** application designed to fetch, process, and answer questions about the **American Music Awards 2025** using real-time data from Wikipedia.

## 🚀 Overview
This project demonstrates a modular AI architecture that retrieves specific knowledge from Wikipedia to supplement an LLM's knowledge. 
- **Use Case:** Answering detailed questions about the **American Music Awards 2025** (nominees, highlights, and dates).
- **Backend (FastAPI):** Orchestrates the AI logic and serves the API endpoints.
- **Frontend (Streamlit):** A clean interface for user interaction.
- **RAG Engine (LangChain):** Manages document loading, vector storage, and the LLM chain.

## 🛠️ Tech Stack
* **Python 3.9+**
* **FastAPI:** High-performance web framework for the API.
* **Streamlit:** Fast UI development for data scripts.
* **LangChain:** Framework for developing LLM-powered applications.
* **ChromaDB:** Vector database for persistent document storage.
* **HuggingFace:** Sentence embeddings (Model: `BAAI/bge-small-en-v1.5`).
* **Groq Cloud:** High-speed inference for `Llama-3.3-70b`.

## 📁 Project Structure
```text
├── main.py          # FastAPI server and API endpoints
├── engine.py        # RAG logic (Chain, Retriever, and LLM setup)
├── processor.py     # Data ingestion (Specifically for AMAs 2025 Wikipedia data)
├── ui.py            # Streamlit frontend interface
├── .env             # Environment variables (API Keys)

└── requirements.txt  # Project dependencies


