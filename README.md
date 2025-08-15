#  Legal RAG

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Available-orange)](https://streamlit.io/)

##  Project Description
**Legal RAG** is a **Retrieval-Augmented Generation (RAG)** system designed for legal documents. It allows users to load multiple PDFs (contracts, case laws, statutes), perform semantic search, and get **concise, context-aware answers**. The system can:

- **Cite specific sections** from documents  
- **Handle conflicting information** by presenting all relevant perspectives  
- Be easily **deployed locally via Streamlit UI**

---

##  Features

| Feature | Description |
|----------|-------------|
| PDF Ingestion | Converts legal PDFs into structured JSON |
| Embeddings + Retrieval | Breaks content into chunks, embeds using SentenceTransformers, and indexes them in **ChromaDB** |
| Legal Q&A | Answers queries using retrieved context, with accurate citations |
| Conflict Resolution | Detects conflicting statements across documents and highlights them |
| Streamlit UI | Provides a user-friendly interface for interaction |
| Evaluation | Measures **latency** via `evaluation.py` |

---

##  Setup & Installation

### 1. Clone the repository
```bash
git clone <repository_url>
cd legal_rag_project

