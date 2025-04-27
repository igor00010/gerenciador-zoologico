from animal import Animal

class Recinto:
    def __init__(self, id: int, tipo: str, capacidade: int):
        
        self.id = id
        self.tipo = tipo
        self.capacidade = capacidade
        self.animais = []



# ANIMAL
    # Adiciona um animal a um recinto
    def adicionar_animal(self):
        if len(self.animais) < self.capacidade:
            id = int(input("Id do animal: "))
            indice = self.verificar_id_animal(id)
            if indice == None:
                animal = Animal(id, int(input("Idade: ")), input("Especie: "), float(input("Peso: ")), input("Sexo: "))
                self.animais.append(animal)
            else:
                print("Animal ja existe")
        else:
            print("Capacidade maxima atingida")

    # Remove um animal de um recinto
    def remover_animal(self):
        if len(self.animais) <= 0:
            print("Sem animais")
        else:
            id = int(input("Id do animal: "))
            indice = self.verificar_id_animal(id)
            if indice != None:
                    self.animais.pop(indice)
                    print("Animal removido com sucesso")
            else:
                print("Animal nao existe")
    
    # Exibe apenas um animal de um recinto
    def exibir_animal(self):
        if len(self.animais) == 0:
            print("O recinto nao tem nenhum animail")
        else:
            id = int(input("Id: "))
            indice = self.verificar_id_animal(id)
            if indice != None:
                self.animais[indice].exibir_dados()
            else:
                print("Animal nao encontrado")

    # Exibe todos os animais de um recinto
    def exibir_animais(self):
        if len(self.animais) == 0:
            print("O recinto nao tem nenhum animail")
        else:
            for animal in self.animais:
                    animal.exibir_dados()
#



# VERIFICAR IDs
    def verificar_id_animal(self,  id: int):
        for i, animal in enumerate(self.animais):
            if animal.id == id:
                return i
        return None
#



# RECINTO
    # Exibe os dados do recinto
    def exibir_dados(self):
        print(f"Id: {self.id}, Tipo: {self.tipo}, Capacidade: {self.capacidade}, Animais: {len(self.animais)}")
#