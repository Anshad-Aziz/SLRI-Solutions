from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from utils.mcp import MCPMessage
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

class LLMResponseAgent:
    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="qwen/qwen3-32b"
        )

        self.prompt = ChatPromptTemplate.from_template(
            """
        You are a helpful AI assistant specialized in answering questions using retrieved document context.

        Use ONLY the information provided in the context below to answer the question. If the answer is not contained in the context, respond with "The answer is not available in the provided documents."

        ---

        Context:
        {context}

        ---

        Question: {query}

        Answer in a clear and concise manner:
        """
        )


    def generate_response(self, message: MCPMessage):
        if message.type != "RETRIEVAL_RESULT":
            return "", []
        context = "\n".join([doc.page_content for doc in message.payload["retrieved_context"]])
        query = message.payload["query"]
        
        chain = self.prompt | self.llm
        response = chain.invoke({"context": context, "query": query}).content
        sources = [doc.page_content[:100] + "..." for doc in message.payload["retrieved_context"]]
        return response, sources