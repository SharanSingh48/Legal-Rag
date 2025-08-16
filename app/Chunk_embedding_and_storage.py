__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import json
import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv
import os

# Load .env API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("Missing GROQ_API_KEY in .env file")

# Groq client
groq_client = Groq(api_key=api_key)

# Paths and configs
BASE_DIR = os.path.dirname(__file__)
CHUNKS_FILE = os.path.join(BASE_DIR, "processed_chunks.jsonl")
CHROMA_DB_DIR = "chroma_db"
EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
TOP_K = 7

# Embedding model
embedder = SentenceTransformer(EMBED_MODEL_NAME)

# Vector DB
client = chromadb.PersistentClient(path=CHROMA_DB_DIR)

collection = client.get_or_create_collection(
    name="legal_chunks",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBED_MODEL_NAME
    )
)

# Load chunks into DB if empty
if collection.count() == 0:
    with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            data = json.loads(line)
            chunk_id = f"chunk_{i}"
            collection.add(
                ids=[chunk_id],
                documents=[data["text"]],
                metadatas=[{"source": data["source"]}]
            )


def retrieve_and_answer(question):
    print(f"\n Question: {question}")

    # Retrieve docs
    results = collection.query(
        query_texts=[question],
        n_results=TOP_K
    )

    retrieved_docs = results["documents"][0]
    scores = results["distances"][0] if "distances" in results else []
    context = "\n\n".join(retrieved_docs)

    # Prompt for Groq
    prompt = f"""You are a legal assistant. 
Use the provided context to answer the question accurately and concisely.
Also cite specific sections from the context.
If the answer is not in the context, say you don't have enough information.
If the context contains conflicting information, state both versions of the information and clearly mention in which part of the context each was found.

Context:
{context}

Question: {question}
Answer:
"""

    # Call Groq API
    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Fast Groq model
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content

    print("\n Answer:", answer)
    return answer, scores


if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (or 'exit'): ")
        if q.lower() == "exit":
            break
        retrieve_and_answer(q)





