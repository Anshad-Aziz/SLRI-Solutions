from utils.vector_store import VectorStore
from utils.mcp import MCPMessage

class RetrievalAgent:
    def __init__(self):
        self.vector_store = VectorStore()

    def index_document(self, message: MCPMessage):
        if message.type != "INDEX_DOCUMENT":
            return
        documents = message.payload["parsed_content"]
        self.vector_store.add_documents(documents)

    def retrieve(self, message: MCPMessage):
        if message.type != "RETRIEVAL_QUERY":
            return []
        query = message.payload["query"]
        return self.vector_store.search(query)
