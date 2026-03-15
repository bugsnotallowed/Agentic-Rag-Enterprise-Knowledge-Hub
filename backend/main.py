from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import shutil

from utils.parser import PDFParser
from services.vector_store import VectorStoreService
from services.agent_service import RAGAgent

app = FastAPI(title="Agentic RAG Hub")

# Initialize Services
vector_service = VectorStoreService()
agent = RAGAgent()

# CORS setup for Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Agentic RAG Backend is Running"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    # Create data directory if not exists
    data_dir = "../data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    file_path = os.path.join(data_dir, file.filename)
    
    # Save file locally
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        # Step 1: Parse PDF
        parsed_content = PDFParser.extract_text(file_path)
        
        # Step 2: Prepare for Vector Store
        texts = [page["content"] for page in parsed_content]
        metadatas = [{"filename": file.filename, "page": page["page"]} for page in parsed_content]
        
        # Step 3: Add to Vector Store
        num_chunks = vector_service.add_documents(texts, metadatas)
        
        return {
            "filename": file.filename, 
            "status": "Processed and Indexed",
            "chunks_created": num_chunks
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/query")
async def query_rag(q: str):
    try:
        # Phase 2: Use Agentic Search
        result = await agent.run(q)
        
        # If no answer was generated due to lack of relevance
        if "answer" not in result:
            return {
                "query": q,
                "answer": "I'm sorry, I couldn't find any relevant information in the uploaded documents to answer your question.",
                "sources": []
            }

        return {
            "query": q,
            "answer": result["answer"],
            "relevance_status": result["relevance_grade"],
            "docs_found": len(result["documents"])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
