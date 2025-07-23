# Agentic RAG Chatbot with LangChain and Groq

A Retrieval-Augmented Generation (RAG) chatbot using LangChain for document processing and Groq API for LLM, with an agentic architecture and Model Context Protocol (MCP).
## 📹 Demo Video

[Watch the demo video on Google Drive](https://drive.google.com/file/d/1YVAux58NzK5tPI2IZbr6Im1yA9sSaY9r/view?usp=sharing)

## Features
- Supports PDF, PPTX, CSV, DOCX, TXT/Markdown
- Agentic architecture with Ingestion, Retrieval, and LLMResponse agents
- MCP for inter-agent communication
- LangChain for document loading, embeddings, and FAISS vector store
- Streamlit UI for document upload and multi-turn chat

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <https://github.com/Anshad-Aziz/SLRI-Solutions.git>
   cd rag_chatbot
2.Install dependencies & Run the app:
  ```bash
   pip install -r requirements.txt
   streamlit run app.py
