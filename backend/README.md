# Agentic RAG Hub - Backend

This is a 100% local, free, and agentic RAG system built with FastAPI, LangGraph, ChromaDB, and Ollama.

## Prerequisites
1. **Python 3.10+**
2. **Ollama:** [Download here](https://ollama.com/)
3. **Llama 3.1 Model:** Run `ollama pull llama3.1` in your terminal.

## Setup
1. Navigate to this directory: `cd backend`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python main.py`

## API Endpoints
- `POST /upload`: Upload a PDF to index it into the local vector store.
- `GET /query?q=your_question`: Ask a question. The agent will retrieve chunks, grade their relevance, and answer using Llama 3.1.

## Why this is Agentic?
Unlike standard RAG, this system uses a **LangGraph** workflow to:
1. **Retrieve** context.
2. **Grade** the context: It asks the LLM if the retrieved info is actually relevant to the query.
3. **Generate:** Only if the info is relevant does it produce an answer. This significantly reduces hallucinations.
