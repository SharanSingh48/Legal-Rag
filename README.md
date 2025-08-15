Legal RAG
Project Description

Legal RAG is a Retrieval-Augmented Generation system for legal documents and case laws. It allows users to query legal content stored in PDFs and receive concise, context-aware answers. The system handles conflicting information across documents, cites relevant sections, and can be deployed locally using a Streamlit interface.

Features

Ingests legal PDFs and converts them to structured JSON.

Generates embeddings and stores chunks in a local Chroma database for fast retrieval.

Answers questions based on retrieved context with citation of sections.

Handles conflicting information across multiple documents and clearly mentions context.

Streamlit UI for easy interactive querying.

Evaluation of latency metrics via evaluation.py.

Setup & Installation

Clone the repository:

git clone <your-repo-link>
cd <your-repo-folder>


Install dependencies:

pip install -r requirements.txt


Prepare your data:

Replace the sample PDFs in the data/ folder with your own legal documents if desired.

Convert PDFs to JSON:

python "Pdf to json/convert_to_text.py"
python "Pdf to json/Text_to_json.py"


Generate embeddings and store chunks:

python script/Chunk_embedding_and_storage.py


Launch Streamlit UI (optional):

streamlit run script/Ui.py


Follow the command printed by Streamlit in your terminal to open the app locally.

Data

Sample data is provided for testing and demonstration in the data/ folder.

Users can replace it with their own PDFs to run the system on custom legal documents.

Evaluation

Due to OpenAI API key limitations, RAGAS evaluation was not used.

Latency metrics were calculated and code for evaluation can be found in script/evaluation.py.
