from fastapi import APIRouter

from app.models.schemas import QuestionRequest
from app.services.rag_service import search
from app.services.bedrock_service import generate_response

router = APIRouter()

@router.post("/ask")
def ask_question(request: QuestionRequest):

    results = search(request.question)

    context = "\n".join(results)

    answer = generate_response(
        request.question,
        context
    )

    return {
        "question": request.question,
        "answer": answer
    }