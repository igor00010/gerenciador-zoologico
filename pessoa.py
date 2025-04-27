class Pessoa:
    def __init__(self, id: int, nome: str, idade: int, cpf: str, endereco: str):
        
        self.id = id
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco

    def exibir_dados(self):
        print(f"Id: {self.id}, Nome: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}, Endereco: {self.endereco}")

class Funcionario(Pessoa):
    def __init__(self, id: int, nome: str, idade: int, cpf: str, endereco: str, funcao: str):
        super().__init__(id, nome, idade, cpf, endereco)
        self.funcao = funcao

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Funcao: {self.funcao}")

class Visitante(Pessoa):
    def __init__(self, id: int, nome: str, idade: int, cpf: str, endereco: str):
        super().__init__(id, nome, idade, cpf, endereco)