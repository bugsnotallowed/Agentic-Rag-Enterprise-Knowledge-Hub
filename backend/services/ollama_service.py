from langchain_ollama import OllamaLLM
import json

class OllamaService:
    """Handles interaction with the local Ollama LLM (Llama 3.1)."""
    
    def __init__(self, model_name="llama3.1"):
        self.llm = OllamaLLM(model=model_name)
        
    def generate_response(self, prompt: str):
        """Generates a response from the local model."""
        try:
            return self.llm.invoke(prompt)
        except Exception as e:
            return f"Error connecting to Ollama: {str(e)}"

    def analyze_relevance(self, query: str, context: str):
        """Uses the LLM to grade retrieval relevance (Agentic step)."""
        prompt = f"""
        Analyze if the following context is relevant to the user query.
        Answer with only 'yes' or 'no'.
        
        Query: {query}
        Context: {context}
        """
        response = self.llm.invoke(prompt).strip().lower()
        return "yes" in response
