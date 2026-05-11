from pydantic import BaseModel

# Valida o body da requisição.
class QuestionRequest(BaseModel):
    question: str