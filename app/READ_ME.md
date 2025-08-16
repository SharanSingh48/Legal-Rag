# Legal RAG App

This folder contains the Streamlit app for the Legal RAG project.

## Overview
This app allows users to interact with the Legal RAG system via a web interface. Users can ask legal questions, and the app will retrieve relevant context from preprocessed legal document chunks and provide answers using a LLaMA model.

## Notes
- The app uses the **Groq API** to run the LLaMA model. This allows the app to function even if LLaMA is **not installed locally**.
- Make sure the Groq API key is correctly set in the script (`Chunk_embedding_and_storage.py`) to enable model inference.


