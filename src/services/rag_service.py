from sentence_transformers import SentenceTransformer

class RAGService:

    def __init__(self):
        self.embedder = SentenceTransformer(model_name="all-MiniLM-L6-v2")

    def embed_text(self, text: str) -> list[float]:
        return self.embedder.encode(text).tolist()