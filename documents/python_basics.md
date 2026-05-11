1. Variáveis e Tipos

Pense em variáveis como etiquetas em caixas. Você guarda um valor e dá um nome a ele.

Inteiros e Floats: Números inteiros ou com casas decimais.

Strings: Textos, sempre entre aspas.

Booleans: Valores de verdadeiro (True) ou falso (False).

Python
idade = 25          # Inteiro
preco = 19.99       # Float
nome = "Gemini"     # String
ligado = True       # Boolean


2. Listas: Guardando Coleções

As listas permitem armazenar vários itens em uma única variável, acessados por um índice (começando do 0).

Python
compras = ["pão", "leite", "café"]
print(compras[0])  # Exibe "pão"
compras.append("açúcar")  # Adiciona ao final


3. Condicionais (if, elif, else)

O programa decide qual caminho seguir baseado em uma condição. Se for verdade, ele executa o bloco recuado.

Python
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


4. Loops (for e while)

Loops servem para repetir tarefas sem precisar escrever o código várias vezes.

For: Ótimo para percorrer listas ou sequências.

While: Executa enquanto uma condição for verdadeira.

Python
# Percorre a lista
for item in compras:
    print(f"Comprar: {item}")

# Repete 5 vezes
for i in range(5):
    print(i)


5. Funções

Funções são "receitas" que você define uma vez com o comando def e usa (chama) quando precisar, evitando repetição de código.

Python
def saudar(usuario):
    return f"Olá, {usuario}! Tudo bem?"

mensagem = saudar("Carlos")
print(mensagem)


6. Entrada de Usuário e Conversão

O comando input() sempre recebe o que o usuário digita como texto (string). Se precisar de um número, você deve converter.

Python
resposta = input("Digite seu ano de nascimento: ")
ano = int(resposta)  # Converte texto para número inteiro


Resumo da Lógica:

O Python executa o código de cima para baixo. Quando ele encontra um dois-pontos (:), ele espera que a próxima linha tenha um espaço (tabulação) para entender que aquele código pertence à função, ao if ou ao loop acima dele.