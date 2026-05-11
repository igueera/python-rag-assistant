from app.database.chroma_client import collection
from app.services.embedding_service import generate_embedding

def ingest_document():

    with open(
        "documents/python_basics.md",
        "r",
        encoding="utf-8"
    ) as file:

        text = file.read()

    chunks = text.split("\n\n")

    for index, chunk in enumerate(chunks):

        embedding = generate_embedding(chunk)

        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[str(index)]
        )

    print("Documento ingerido com sucesso")

def search(query: str):

    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results["documents"][0]