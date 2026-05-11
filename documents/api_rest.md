REST (Representational State Transfer) não é uma linguagem ou um software, mas um estilo de arquitetura. É o padrão que permite que o seu aplicativo de celular peça dados para um servidor na nuvem.


1. A Arquitetura Cliente-Servidor

No modelo REST, temos dois papéis claros: o Cliente (quem pede, ex: seu navegador) e o Servidor (quem guarda os dados e responde). Eles são independentes: você pode mudar o banco de dados do servidor sem precisar atualizar o código do aplicativo.


2. O Coração do REST: Verbos HTTP

Para que a comunicação seja organizada, o REST utiliza os métodos (verbos) do protocolo HTTP. Cada um tem um propósito específico, mapeado para o que chamamos de CRUD (Create, Read, Update, Delete):

GET: "Me dê isso". Usado apenas para ler dados.

POST: "Crie isso". Usado para enviar novos dados.

PUT: "Atualize isso". Substitui uma informação existente.

DELETE: "Apague isso". Remove uma informação.


3. Recursos e Endpoints

No REST, tudo é um Recurso (um usuário, um produto, uma foto). Cada recurso deve ter um endereço único, chamado de URL ou Endpoint.

Exemplos de boas práticas:

GET /usuarios (Lista todos os usuários)

GET /usuarios/42 (Busca apenas o usuário com ID 42)

POST /produtos (Cria um novo produto)


4. O Idioma Universal: JSON

Antigamente, as APIs usavam XML (muito pesado). Hoje, o padrão é o JSON (JavaScript Object Notation). Ele é leve e fácil de ler tanto por humanos quanto por máquinas.

Exemplo de um objeto JSON de resposta:

JSON
{
  "id": 42,
  "nome": "Gemini",
  "cargo": "IA"
}


5. Stateless (A "falta de memória")

Essa é a regra de ouro do REST: o servidor não guarda memória da sua última conversa.
Cada requisição enviada pelo cliente deve conter toda a informação necessária para ser entendida. Se você quer deletar um post, não pode dizer "apague aquele que eu vi antes"; você deve dizer "apague o post de ID 10". Isso torna as APIs muito mais rápidas e escaláveis.

6. Status Codes: O Feedback do Servidor
O servidor sempre responde com um código numérico que diz o que aconteceu. Os mais comuns são:

200 (OK): Tudo certo, aqui estão seus dados.

201 (Created): Sucesso! O novo recurso foi criado.

400 (Bad Request): Você enviou algo errado (erro do cliente).

401 (Unauthorized): Você precisa de uma senha/token para ver isso.

404 (Not Found): Esse recurso não existe.

500 (Internal Server Error): O servidor quebrou (erro do programador).

Por que o mundo usa REST?
Simplicidade: Usa a própria estrutura da internet (HTTP) para funcionar.

Flexibilidade: O servidor pode ser em Java, o banco em SQL, e o cliente em Python. Desde que falem REST/JSON, eles se entendem.

Escalabilidade: Como é stateless, é fácil colocar vários servidores para dividir a carga de trabalho.

Dica: Se você for construir uma API, pense nos seus endpoints como substantivos (/pedidos) e nunca como verbos (/fazerPedido). O "verbo" já é o método HTTP (POST).