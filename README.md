# Python RAG Assistant

Assistente inteligente para aprendizado de Python utilizando arquitetura RAG (Retrieval-Augmented Generation) integrada ao Amazon Bedrock.

O projeto foi desenvolvido com foco em conceitos modernos de Engenharia de Machine Learning e IA Generativa, incluindo embeddings semânticos, banco vetorial, inferência com LLMs, cache distribuído e arquitetura modular.

---

# Objetivo

O sistema permite que usuários façam perguntas sobre Python, lógica de programação e desenvolvimento backend.

A aplicação:
- recupera contexto semanticamente relevante através de RAG
- utiliza um modelo LLM hospedado no Amazon Bedrock
- gera respostas contextualizadas
- utiliza Redis para cache de inferência
- expõe uma API REST utilizando FastAPI

---

# Arquitetura

```text
Usuário
   ↓
FastAPI API
   ↓
Redis Cache
   ↓
RAG Pipeline
   ↓
ChromaDB
   ↓
Amazon Bedrock (Nova Lite)
   ↓
Resposta gerada
```

---

# Tecnologias Utilizadas

## Backend
- Python 3.11
- FastAPI
- Uvicorn

## IA Generativa
- Amazon Bedrock
- Amazon Nova Lite
- Sentence Transformers

## RAG
- ChromaDB
- Embeddings semânticos
- Busca vetorial

## Infraestrutura
- Docker
- Docker Compose
- Redis

## Observabilidade
- Logging estruturado

---

# Funcionalidades

- API REST para perguntas e respostas
- Busca semântica utilizando embeddings
- Recuperação contextual com RAG
- Integração com Amazon Bedrock
- Cache Redis para otimização de inferência
- Logs estruturados
- Arquitetura modular e escalável

---

# Estrutura do Projeto

```text
python-rag-assistant/
│
├── app/
│   ├── main.py
│   │
│   ├── routes/
│   │   └── ask.py
│   │
│   ├── services/
│   │   ├── rag_service.py
│   │   ├── embedding_service.py
│   │   ├── bedrock_service.py
│   │   └── cache_service.py
│   │
│   ├── database/
│   │   └── chroma_client.py
│   │
│   ├── utils/
│   │   └── logger.py
│   │
│   └── models/
│       └── schemas.py
│
├── documents/
├── chroma_db/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

# Pipeline RAG

O fluxo da aplicação segue as etapas:

1. Usuário envia pergunta
2. API verifica cache Redis
3. Sistema gera embedding da pergunta
4. ChromaDB realiza busca vetorial
5. Contextos relevantes são recuperados
6. Contexto é enviado ao Amazon Bedrock
7. LLM gera resposta contextualizada
8. Resposta é armazenada em cache
9. API retorna resposta ao usuário

---

# Como Executar o Projeto

## 1. Clonar repositório

```bash
git clone https://github.com/igueera/python-rag-assistant.git
```

---

## 2. Entrar na pasta

```bash
cd python-rag-assistant
```

---

## 3. Criar arquivo .env

```env
AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
AWS_REGION=us-east-1
```

---

# Configuração AWS

O projeto utiliza Amazon Bedrock.

É necessário:
- possuir conta AWS
- criar usuário IAM
- habilitar acesso ao Bedrock
- habilitar modelo Amazon Nova Lite

---

# Subir aplicação

```bash
docker compose up --build
```

---

# Acessar documentação Swagger

```text
http://127.0.0.1:8000/docs
```

---

# Endpoint Principal

## POST /ask

### Request

```json
{
  "question": "o que é programação orientada a objetos?"
}
```

---

### Response

```json
{
  "question": "o que é programação orientada a objetos?",
  "answer": "Programação orientada a objetos é um paradigma...",
  "source": "bedrock"
}
```

---

# Exemplo de Cache

Primeira requisição:

```json
{
  "source": "bedrock"
}
```

Requisições posteriores:

```json
{
  "source": "cache"
}
```

---

# Busca Semântica

O sistema utiliza embeddings vetoriais para encontrar conteúdos semanticamente similares.

Isso permite:
- recuperação contextual mais precisa
- independência de palavras exatas
- melhor qualidade nas respostas

---

# Logs

A aplicação possui logging estruturado para:
- monitoramento do fluxo
- troubleshooting
- rastreamento de inferência
- observabilidade

Exemplo:

```text
INFO | Pergunta recebida
INFO | Executando busca semântica
INFO | Gerando resposta via Amazon Bedrock
INFO | Resposta salva no cache Redis
```

---

# Conceitos Aplicados

- Retrieval-Augmented Generation (RAG)
- Engenharia de Prompt
- Embeddings semânticos
- Busca vetorial
- APIs REST
- Cache distribuído
- Inferência com LLMs
- Arquitetura modular
- Microsserviços
- Observabilidade
- Dockerização

---

# Melhorias Futuras

- Upload dinâmico de documentos
- Streaming de respostas
- Histórico de conversas
- Banco vetorial em produção
- Deploy em AWS ECS/EKS
- CI/CD
- Monitoramento avançado
- Autenticação JWT
- Interface frontend

---

# Autor

Igor Gabriel

- LinkedIn: https://www.linkedin.com/in/igor-gabriel-924812220/
- GitHub: github.com/igueera

---

# Licença

Projeto desenvolvido para fins educacionais e demonstração técnica.
