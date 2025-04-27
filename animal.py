class Animal:
    def __init__(self, id: int, idade: int, especie: str, peso: float, sexo: str):
        
        self.id = id
        self.idade = idade
        self.especie = especie
        self.peso = peso
        self.sexo = sexo

    def exibir_dados(self):
        print(f"Id: {self.id}, Idade: {self.idade}, Especie: {self.especie}, Peso: {self.peso}, Sexo: {self.sexo}")