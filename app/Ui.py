import streamlit as st
from Chunk_embedding_and_storage import retrieve_and_answer

st.title("📚 Legal Assistant")

question = st.text_input("Ask a legal question:")

if st.button("Get Answer") and question:
    answer, scores = retrieve_and_answer(question)

    st.subheader("💡 Answer")
    st.write(answer)
