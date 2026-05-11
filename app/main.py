from fastapi import FastAPI

from app.routes.ask import router as ask_router

app = FastAPI()

app.include_router(ask_router)

@app.get("/")
def root():

    return {
        "message": "Python RAG Assistant running"
    }