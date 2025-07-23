from agents.ingestion import IngestionAgent
from agents.retrieval import RetrievalAgent
from agents.llm_response import LLMResponseAgent
from utils.mcp import MCPMessage

class CoordinatorAgent:
    def __init__(self):
        self.ingestion_agent = IngestionAgent()
        self.retrieval_agent = RetrievalAgent()
        self.llm_response_agent = LLMResponseAgent()

    def process_document(self, file):
        ingestion_msg = MCPMessage(
            sender="CoordinatorAgent",
            receiver="IngestionAgent",
            type="DOCUMENT_UPLOAD",
            payload={"file": file}
        )
        parsed_content = self.ingestion_agent.process(ingestion_msg)
        
        retrieval_msg = MCPMessage(
            sender="CoordinatorAgent",
            receiver="RetrievalAgent",
            type="INDEX_DOCUMENT",
            payload={"parsed_content": parsed_content}
        )
        self.retrieval_agent.index_document(retrieval_msg)

    def handle_query(self, query, trace_id):
        retrieval_msg = MCPMessage(
            sender="CoordinatorAgent",
            receiver="RetrievalAgent",
            type="RETRIEVAL_QUERY",
            trace_id=trace_id,
            payload={"query": query}
        )
        retrieved_context = self.retrieval_agent.retrieve(retrieval_msg)

        llm_msg = MCPMessage(
            sender="CoordinatorAgent",
            receiver="LLMResponseAgent",
            type="RETRIEVAL_RESULT",
            trace_id=trace_id,
            payload={"retrieved_context": retrieved_context, "query": query}
        )
        response, sources = self.llm_response_agent.generate_response(llm_msg)
        return response, sources