from fastapi import FastAPI

from src.schemas.rag_schema import EmbeddingRequest
from src.services.llm_service import LLMService

from src.constants.knowledge_base import KNOWLEDGE_BASE

app = FastAPI()

@app.post(
    "/query",
    status_code=200
)
async def query(
    request: EmbeddingRequest
):
    llm_service = LLMService()
    response = llm_service.generate_response(request.text)

    return {
        "message": response
    }