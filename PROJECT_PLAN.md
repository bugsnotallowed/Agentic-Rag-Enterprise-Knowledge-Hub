# Project Plan: Agentic Enterprise Knowledge Hub (Production-Level RAG)

This project aims to build a scalable, high-performance, and verifiable RAG system that uses an **Agentic Workflow** to process complex queries across diverse datasets (PDFs, Markdown, CSVs).

---

## 1. Architectural Overview
A standard "Naive RAG" (Retrieve -> Generate) is insufficient for production. We will implement:
- **Asynchronous Ingestion Pipeline:** Process large documents in the background without blocking the UI.
- **Hybrid Retrieval:** Combine Vector Search (semantic) with Keyword Search (BM25) for high precision.
- **Agentic Re-ranking:** Use a Cross-Encoder to ensure the most relevant chunks are sent to the LLM.
- **Self-Correction (CRAG):** The agent evaluates retrieved chunks and decides if it needs to search the web or re-try retrieval.
- **Systematic Evaluation:** Using **RAGAS** to measure "Faithfulness," "Answer Relevancy," and "Context Precision."

---

## 2. 100% Free & Local Tech Stack
| Layer | Technology | Why? |
| :--- | :--- | :--- |
| **Orchestration** | **LangGraph** | Stateful, cyclic agent workflows (Open Source). |
| **Brain (LLM)** | **Ollama (Llama 3.1)** | Local inference. Zero cost. No API keys. |
| **Vector DB** | **ChromaDB** | Simple, local-only vector storage (saves to your disk). |
| **Embeddings** | **HuggingFace (Local)** | Models like `all-MiniLM-L6-v2` run on your CPU. |
| **Parsing** | **PyMuPDF / Marker** | Local libraries for high-quality PDF extraction. |
| **Backend** | **FastAPI** | High performance, async Python framework. |
| **Re-ranking** | **FlashRank** | Local, lightweight CPU-based re-ranking. |
| **Frontend** | **Next.js** | Modern React framework for the dashboard. |

---

## 3. Implementation Roadmap (Step-by-Step)

### Phase 1: Environment & Ingestion Pipeline
1. **Initialize Project:** Set up Python virtual environment and Poetry/Pip for dependency management.
2. **FastAPI Scaffolding:** Create basic API routes for document upload and status tracking.
3. **Unstructured Parser:** Implement a service to convert complex PDFs into clean Markdown/Chunks.
4. **Qdrant Integration:** Set up the vector database and implement a "Upsert" service with metadata filtering.

### Phase 2: The Agentic RAG Engine
1. **Hybrid Search:** Implement dense (Vector) and sparse (BM25) search logic.
2. **LangGraph Workflow:** Build the "Self-RAG" graph:
   - Node 1: Retrieve context.
   - Node 2: Grade retrieval quality (Is this relevant?).
   - Node 3: If irrelevant, rewrite query or trigger Web Search (optional).
   - Node 4: Generate answer.
3. **Cohere Re-ranker:** Add a re-ranking step to refine the top-K retrieved chunks before generation.

### Phase 3: Evaluation & Optimization
1. **Synthetic Data Generation:** Use an LLM to generate 50+ (Question, Context, Answer) pairs from your data.
2. **RAGAS Benchmarking:** Run evaluation and generate a report on the current system performance.
3. **Iterative Tuning:** Adjust chunk sizes, overlap, and prompts based on the evaluation metrics.

### Phase 4: Production Features & UI
1. **Streaming Responses:** Use FastAPI `StreamingResponse` and WebSockets for real-time AI typing.
2. **Chat History:** Persistent storage using PostgreSQL (with PGVector for potential future-proofing).
3. **Frontend (Next.js):** Build a professional dashboard with document management and chat interface.

### Phase 5: Deployment
1. **Dockerization:** Create a multi-stage `Dockerfile` for the backend.
2. **CI/CD:** Automate linting and evaluation runs on every push to GitHub.
