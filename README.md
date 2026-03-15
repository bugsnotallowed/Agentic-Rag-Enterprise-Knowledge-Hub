# Agentic RAG Enterprise Knowledge Hub (Production-Level RAG)

A 100% local, free, and agentic RAG (Retrieval-Augmented Generation) system built for professional knowledge intelligence. This project demonstrates high-performance AI engineering by moving beyond "naive" RAG into **Agentic Workflows** using **LangGraph** and **Ollama**.

---

## 🚀 Key Features

- **Agentic Retrieval:** Uses a stateful LangGraph workflow to retrieve documents and **grade their relevance** using an LLM before generating an answer. This significantly reduces hallucinations.
- **100% Local & Private:** No data leaves your machine. Powered by **Ollama (Llama 3.1)** and local **HuggingFace Embeddings**.
- **Production-Level Tech Stack:**
  - **Backend:** FastAPI (Async processing)
  - **AI Orchestration:** LangGraph (Stateful Agent workflows)
  - **Vector Database:** ChromaDB (Local persistence)
  - **LLM:** Ollama (Llama 3.1 8B)
  - **Embeddings:** HuggingFace `all-MiniLM-L6-v2`
  - **Frontend:** Next.js 14, Tailwind CSS, Lucide Icons
- **Real-Time Insights:** The UI shows the agent's "Relevance Status" for every response.

---

## 📂 Project Structure

- `/backend`: FastAPI server, agentic logic, and vector store services.
- `/frontend`: Next.js 14 dashboard for uploading documents and chatting.
- `/data`: Local directory for uploaded PDF documents.
- `/vector_db`: Persistent local storage for the ChromaDB vector database.

---

## 🛠️ Setup Instructions

### Prerequisites
1. **Python 3.11+**
2. **Node.js 18+**
3. **Ollama:** [Download and Install Ollama](https://ollama.com/)
   - After installing, run: `ollama pull llama3.1`

### Backend Setup
1. Navigate to the backend folder:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the server:
   ```bash
   python main.py
   ```
   The backend will be live at `http://localhost:8000`.

### Frontend Setup
1. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
   The frontend will be live at `http://localhost:3000`.

---

## 🧠 Why this is an "Impactful" Resume Project

1. **System Design:** Demonstrates knowledge of asynchronous ingestion and persistent vector storage.
2. **Agentic Reasoning:** Shows experience with sophisticated AI workflows (LangGraph) rather than just simple API calls.
3. **Data Quality:** Includes a relevance grading step, a core requirement for real-world production AI systems.
4. **Full-Stack Proficiency:** Bridging high-performance Python backends with modern React/Next.js frontends.

---

## 🛡️ Use Case Examples

- **Internal Knowledge Base:** Upload years of corporate PDFs and ask questions about company policy.
- **Academic Research:** Ingest multiple research papers and ask for a cross-referenced summary.
- **Legal/Compliance:** Search through long contracts for specific clauses or contradictions.

---
Built by [Adarsh] - 2026
