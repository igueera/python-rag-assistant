from fastapi import APIRouter

from app.models.schemas import QuestionRequest
from app.services.rag_service import search
from app.services.bedrock_service import generate_response
from app.services.cache_service import (
    get_cache,
    set_cache
)

from app.utils.logger import logger

router = APIRouter()

@router.post("/ask")
def ask_question(request: QuestionRequest):

    logger.info(
        f"Pergunta recebida: {request.question}"
    )

    cached_answer = get_cache(
        request.question
    )

    if cached_answer:

        logger.info(
            "Resposta retornada do cache Redis"
        )

        return {
            "question": request.question,
            "answer": cached_answer,
            "source": "cache"
        }

    logger.info(
        "Executando busca semântica no ChromaDB"
    )

    results = search(request.question)

    context = "\n".join(results)

    logger.info(
        "Gerando resposta via Amazon Bedrock"
    )

    answer = generate_response(
        request.question,
        context
    )

    set_cache(
        request.question,
        answer
    )

    logger.info(
        "Resposta salva no cache Redis"
    )

    return {
        "question": request.question,
        "answer": answer,
        "source": "bedrock"
    }