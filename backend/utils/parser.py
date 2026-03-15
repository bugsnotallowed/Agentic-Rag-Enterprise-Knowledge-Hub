import fitz  # PyMuPDF
import os

class PDFParser:
    """Utility to extract text from PDFs locally."""
    
    @staticmethod
    def extract_text(file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        text_content = []
        doc = fitz.open(file_path)
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text()
            text_content.append({
                "page": page_num + 1,
                "content": text
            })
            
        doc.close()
        return text_content
