class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def falar(self, mensagem):
        return f"{self.nome} diz: {mensagem}"

    def conversar(self, outra_pessoa):
        # Conversa pré-definida entre as duas pessoas
        print(self.falar(f"Olá, meu nome é {self.nome}. Qual o seu nome?"))
        print(outra_pessoa.falar(f"Olá {self.nome}, meu nome é {outra_pessoa.nome}. Prazer em te conhecer!"))
        print(self.falar(f"{outra_pessoa.nome} ficou feliz."))

# Solicita o nome dos usuários
nome1 = input("Informe o nome do 1º usuário: ")
nome2 = input("Informe o nome do 2º usuário: ")

# Criação de dois objetos da classe Pessoa
pessoa1 = Pessoa(nome1)
pessoa2 = Pessoa(nome2)

# Simulação da conversa
pessoa1.conversar(pessoa2)