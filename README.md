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
```
### 2. Remove app folder if running locally

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Customize the data
### 5. Convert PDFs to JSON
Run the following scripts in order
```bash
python "Pdf to json/convert_to_text.py"
```
```bash
python "Pdf to json/Text_to_json.py"
```
### 6. Generate embeddings and index in Chroma
```bash
python script/Chunk_embedding_and_storage.py
```
### 7. Launch the Streamlit UI (optional)
```bash
streamlit run script/Ui.py
```

## Data
The data/ folder includes sample legal documents to get you started quickly. Feel free to replace with your own. The preprocessing pipeline will handle the rest.

## Evaluation
Due to the absence of an OpenAI API key, RAGAS evaluation was not used. Instead, performance is measured via latency metrics. You can assess system speed using script/evaluation.py.
