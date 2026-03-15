import chromadb
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

class VectorStoreService:
    def __init__(self, persist_directory="../vector_db"):
        self.persist_directory = persist_directory
        self.embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.client = chromadb.PersistentClient(path=self.persist_directory)
        self.collection = self.client.get_or_create_collection(name="documents")

    def add_documents(self, text_list, metadata_list=None):
        """Processes and adds documents to the local ChromaDB."""
        
        # Split text into manageable chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        
        chunks = text_splitter.create_documents(text_list, metadatas=metadata_list)
        
        # Add chunks to collection
        for i, chunk in enumerate(chunks):
            self.collection.add(
                documents=[chunk.page_content],
                metadatas=[chunk.metadata],
                ids=[f"doc_{os.urandom(4).hex()}_{i}"]
            )
        
        return len(chunks)

    def query(self, query_text, n_results=5):
        """Retrieves relevant chunks based on a local query."""
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results
