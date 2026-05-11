import json
import boto3
import os

from dotenv import load_dotenv

load_dotenv()

client = boto3.client(
    service_name="bedrock-runtime",
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

MODEL_ID = "amazon.nova-lite-v1:0"

def generate_response(question: str, context: str):

    prompt = f"""
    Você é um assistente especialista em Python.

    Responda utilizando o contexto abaixo.

    Contexto:
    {context}

    Pergunta:
    {question}
    """

    body = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body)
    )

    response_body = json.loads(
        response["body"].read()
    )

    return response_body["output"]["message"]["content"][0]["text"]