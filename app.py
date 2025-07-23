import streamlit as st
from agents.coordinator import CoordinatorAgent
import uuid
import os

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(page_title="Agentic RAG Chatbot", page_icon="🤖", layout="centered")

# ---------------------- HEADER ----------------------
st.markdown("""
    <h1 style='text-align: center;'>📚 Agentic RAG Chatbot</h1>
    <p style='text-align: center;'>Upload documents in various formats and ask questions based on the content.</p>
    <hr>
""", unsafe_allow_html=True)

# ---------------------- INIT COORDINATOR ----------------------
if "coordinator" not in st.session_state:
    st.session_state.coordinator = CoordinatorAgent()

# ---------------------- FILE UPLOAD ----------------------
with st.expander("📂 Upload Documents", expanded=True):
    uploaded_files = st.file_uploader(
        "Upload supported files (PDF, DOCX, PPTX, TXT, CSV, Markdown):",
        type=["pdf", "pptx", "csv", "docx", "txt", "md"],
        accept_multiple_files=True
    )
    if uploaded_files:
        for file in uploaded_files:
            st.session_state.coordinator.process_document(file)
        st.success(f"✅ {len(uploaded_files)} document(s) processed successfully!")

# ---------------------- CHAT UI ----------------------
st.markdown("### 💬 Chat with Your Documents")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sources" in message and message["sources"]:
            with st.expander("📌 Sources"):
                for source in message["sources"]:
                    st.markdown(f"- {source}")

# Chat input
if prompt := st.chat_input("Ask a question based on the uploaded documents..."):
    # Show user's message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Show assistant's response
    with st.chat_message("assistant"):
        response, sources = st.session_state.coordinator.handle_query(prompt, str(uuid.uuid4()))
        st.markdown(response)
        if sources:
            with st.expander("📌 Sources"):
                for source in sources:
                    st.markdown(f"- {source}")
        st.session_state.messages.append({"role": "assistant", "content": response, "sources": sources})
