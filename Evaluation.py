import json
import time
import ollama
import chromadb


CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "legal_chunks"
EVAL_DATA_PATH = "eval_data.json"


with open(EVAL_DATA_PATH, "r") as f:
    eval_data = json.load(f)


client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_collection(COLLECTION_NAME)


retrieval_latencies = []
generation_latencies = []


for item in eval_data:
    question = item["question"]


    start_retrieval = time.time()
    retrieved = collection.query(query_texts=[question], n_results=3)
    retrieved_docs = [doc for sublist in retrieved["documents"] for doc in sublist]
    context_text = "\n".join(retrieved_docs)
    end_retrieval = time.time()
    retrieval_latencies.append(end_retrieval - start_retrieval)


    prompt = f"""You are a legal assistant. 
Use the provided context to answer the question accurately and concisely.
If the answer is not in the context, say you don't have enough information.

If the context contains conflicting information, state both versions of the information and clearly mention in which part of the context each was found.

Context:
{context_text}

Question: {question}
Answer:"""

    start_generation = time.time()
    response = ollama.chat(
        model="llama3.1:8b",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response["message"]["content"]
    end_generation = time.time()
    generation_latencies.append(end_generation - start_generation)

avg_retrieval_latency = sum(retrieval_latencies) / len(retrieval_latencies)
avg_generation_latency = sum(generation_latencies) / len(generation_latencies)
avg_total_latency = avg_retrieval_latency + avg_generation_latency

print("\n Evaluation Latencies:")
print(f"Average Retrieval Latency: {avg_retrieval_latency:.3f} s/query")
print(f"Average Answer Generation Latency: {avg_generation_latency:.3f} s/query")
print(f"Average Total Latency (retrieval+generation): {avg_total_latency:.3f} s/query")


