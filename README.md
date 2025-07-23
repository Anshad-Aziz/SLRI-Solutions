# Agentic RAG Chatbot with LangChain and Groq

A Retrieval-Augmented Generation (RAG) chatbot using LangChain for document processing and Groq API for LLM, with an agentic architecture and Model Context Protocol (MCP).

## Features
- Supports PDF, PPTX, CSV, DOCX, TXT/Markdown
- Agentic architecture with Ingestion, Retrieval, and LLMResponse agents
- MCP for inter-agent communication
- LangChain for document loading, embeddings, and FAISS vector store
- Streamlit UI for document upload and multi-turn chat

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd rag_chatbot