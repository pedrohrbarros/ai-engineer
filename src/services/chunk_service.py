class ChunkService:

    def __init__(self):
        self.chunk_size = 100
        self.chunk_overlap = 20

    def chunk_text(self, text: str) -> list[str]:
        chunks = []
        current_chunk = ""
        for paragraph in self._split_paragraphs(text):
            if len(current_chunk) + len(paragraph) + 1 > self.chunk_size:
                chunks.append(current_chunk)
                current_chunk = ""
            current_chunk += paragraph + "\n"
        if current_chunk:
            chunks.append(current_chunk)
        return chunks

    def _split_paragraphs(self, text: str) -> list[str]:
        width = self.chunk_size - self.chunk_overlap
        return [text[i:i+width] for i in range(0, len(text), width)]