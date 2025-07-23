from langchain_community.document_loaders import PyPDFLoader, CSVLoader, UnstructuredPowerPointLoader, Docx2txtLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils.mcp import MCPMessage

class IngestionAgent:
    def process(self, message: MCPMessage):
        if message.type != "DOCUMENT_UPLOAD":
            return None
        file = message.payload["file"]
        file_type = file.name.split('.')[-1].lower()
        
        # Save file temporarily
        with open(f"temp.{file_type}", "wb") as f:
            f.write(file.getvalue())
        
        # Select appropriate loader
        if file_type == "pdf":
            loader = PyPDFLoader(f"temp.{file_type}")
        elif file_type == "pptx":
            loader = UnstructuredPowerPointLoader(f"temp.{file_type}")
        elif file_type == "csv":
            loader = CSVLoader(f"temp.{file_type}")
        elif file_type == "docx":
            loader = Docx2txtLoader(f"temp.{file_type}")
        elif file_type in ["txt", "md"]:
            loader = TextLoader(f"temp.{file_type}")
        else:
            return []

        # Load and split documents
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        split_docs = text_splitter.split_documents(documents)
        
        return split_docs
