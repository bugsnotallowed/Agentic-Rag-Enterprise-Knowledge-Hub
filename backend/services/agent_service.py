from typing import List, TypedDict
from langgraph.graph import StateGraph, END
from services.vector_store import VectorStoreService
from services.ollama_service import OllamaService

class AgentState(TypedDict):
    """Represents the state of our RAG agent."""
    query: str
    documents: List[str]
    answer: str
    relevance_grade: str

class RAGAgent:
    def __init__(self):
        self.vector_service = VectorStoreService()
        self.ollama = OllamaService()
        
        # Define the Graph
        workflow = StateGraph(AgentState)
        
        # Add Nodes
        workflow.add_node("retrieve", self.retrieve)
        workflow.add_node("grade_documents", self.grade_documents)
        workflow.add_node("generate", self.generate)
        
        # Build Edges
        workflow.set_entry_point("retrieve")
        workflow.add_edge("retrieve", "grade_documents")
        
        # Conditional Edge: If documents are relevant, generate. Otherwise, we could re-try or exit.
        workflow.add_conditional_edges(
            "grade_documents",
            self.decide_to_generate,
            {
                "relevant": "generate",
                "not_relevant": END # In a more complex version, we'd go to a 'rewrite' node
            }
        )
        workflow.add_edge("generate", END)
        
        self.app = workflow.compile()

    def retrieve(self, state: AgentState):
        """Node 1: Retrieve chunks from local DB."""
        print(f"--- RETRIEVING for: {state['query']} ---")
        results = self.vector_service.query(state['query'], n_results=4)
        return {"documents": results['documents'][0]}

    def grade_documents(self, state: AgentState):
        """Node 2: Grade retrieval relevance using Ollama."""
        print("--- GRADING RELEVANCE ---")
        docs = state['documents']
        query = state['query']
        
        # Simple agent logic: Is at least one document relevant?
        is_relevant = self.ollama.analyze_relevance(query, docs[0]) # Grading the top hit
        
        return {"relevance_grade": "relevant" if is_relevant else "not_relevant"}

    def decide_to_generate(self, state: AgentState):
        """Routing function."""
        return state["relevance_grade"]

    def generate(self, state: AgentState):
        """Node 3: Final Generation."""
        print("--- GENERATING ANSWER ---")
        context = "\n---\n".join(state['documents'])
        prompt = f"""
        Use the context below to answer the user query.
        Context: {context}
        Query: {state['query']}
        """
        response = self.ollama.generate_response(prompt)
        return {"answer": response}

    async def run(self, query: str):
        """Entry point to run the agent graph."""
        inputs = {"query": query}
        result = await self.app.ainvoke(inputs)
        return result
