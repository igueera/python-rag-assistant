from app.services.rag_service import search

results = search(
    "o que são listas?"
)

print(results)