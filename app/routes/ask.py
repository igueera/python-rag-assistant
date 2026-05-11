from fastapi import APIRouter

from app.models.schemas import QuestionRequest
from app.services.rag_service import search

router = APIRouter()

# Busca chunks semanticamente relevantes
@router.post("/ask")
def ask_question(request: QuestionRequest):

    results = search(request.question)

    context = "\n".join(results)

    return {
        "question": request.question,
        "context": context
    }