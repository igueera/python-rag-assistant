1. O Conceito: Classe vs. Objeto

Imagine uma planta de arquitetura. A planta não é a casa, mas o desenho que diz como a casa deve ser.

Classe: É a planta (o molde).

Objeto: É a casa construída (a instância).

Python
class Cachorro:
    pass  # Uma classe vazia por enquanto

meu_dog = Cachorro() # Aqui criamos o objeto 'meu_dog'


2. O Construtor e o famoso self

Para dar características ao objeto assim que ele nasce, usamos o método __init__. O self é a forma do objeto se referir a si mesmo (como dizer "meu nome", "minha idade").

Python
class Gato:
    def __init__(self, nome, cor):
        self.nome = nome  # Atributo
        self.cor = cor    # Atributo

tom = Gato("Tom", "Cinza")
print(tom.nome) # Saída: Tom


3. Métodos: O que o objeto faz

Métodos são funções que pertencem à classe. Eles definem o comportamento do objeto.

Python
class Lampada:
    def __init__(self):
        self.ligada = False

    def interruptor(self):
        self.ligada = not self.ligada
        estado = "acesa" if self.ligada else "apagada"
        print(f"A lâmpada está {estado}")

quarto = Lampada()
quarto.interruptor() # A lâmpada está acesa


4. Os Pilares da POO

A. Herança
Permite que uma classe "filha" herde tudo de uma classe "pai", evitando repetição de código.

Python
class Animal:
    def fazer_som(self):
        print("Som genérico")

class Lobo(Animal): # Lobo herda de Animal
    def uivar(self):
        print("Auuuuuu!")

billy = Lobo()
billy.fazer_som() # Ele tem isso porque herdou do pai

B. Encapsulamento
Serve para esconder detalhes internos e proteger dados. No Python, usamos um ou dois underscores (_ ou __) para indicar que algo é "privado".

Público: self.nome (Todos acessam)

Protegido/Privado: self.__saldo (Apenas a classe mexe)

Python
class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo # Privado

    def ver_saldo(self):
        return f"Saldo atual: R$ {self.__saldo}"

minha_conta = Conta(1000)
# print(minha_conta.__saldo)  # Isso daria erro!
print(minha_conta.ver_saldo()) # O jeito certo de acessar

C. Polimorfismo
"Poli" (muitos) + "morfismo" (formas). É a capacidade de diferentes classes terem métodos com o mesmo nome, mas comportamentos diferentes.

Python
class Passaro:
    def voar(self):
        print("Voando alto...")

class Pinguim(Passaro):
    def voar(self): # Mesma função, comportamento diferente
        print("Eu não voo, eu nado!")

def decolar(ave):
    ave.voar()

decolar(Passaro()) # Voando alto...
decolar(Pinguim()) # Eu não voo, eu nado!

D. Abstração
É focar apenas no que é essencial para o usuário, escondendo a complexidade desnecessária. Quando você usa o controle remoto, você não precisa saber como o circuito eletrônico funciona, apenas que o botão "Power" liga a TV.

Por que usar POO?
Organização: O código fica dividido em peças lógicas (como Legos).

Reutilização: Com a Herança, você escreve menos código.

Manutenção: Se houver um erro no "Caminhão", você mexe na classe Caminhao sem quebrar o resto do sistema.

Dica: Comece simples. Tente modelar coisas do seu dia a dia (um Celular, um Livro, um Personagem de Jogo) antes de tentar criar sistemas complexos. O self parece estranho no começo, mas depois de dez minutos ele vira seu melhor amigo.