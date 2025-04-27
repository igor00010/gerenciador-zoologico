from animal import Animal
from pessoa import Funcionario
from pessoa import Visitante
from recinto import Recinto

class Zoologico:
    def __init__(self, capacidade_visitantes: int, capacidade_recintos: int, capacidade_funcionarios: int):

        self.visitantes = [
            Visitante(0, "João Silva", 25, "111.222.333-44", "Rua das Flores, 123 - Centro"),
            Visitante(1, "Maria Oliveira", 30, "222.333.444-55", "Avenida Brasil, 456 - Jardins"),
            Visitante(2, "Pedro Santos", 8, "333.444.555-66", "Travessa dos Passarinhos, 78 - Vila Nova"),
            Visitante(3, "Ana Costa", 65, "444.555.666-77", "Alameda dos Anjos, 90 - Bela Vista"),
            Visitante(4, "Carlos Mendes", 42, "555.666.777-88", "Praça da Liberdade, 12 - Centro"),
            Visitante(5, "Juliana Pereira", 15, "666.777.888-99", "Rua das Acácias, 34 - Parque das Árvores"),
            Visitante(6, "Marcos Ribeiro", 28, "777.888.999-00", "Avenida Paulista, 1001 - Consolação"),
            Visitante(7, "Fernanda Lima", 33, "888.999.000-11", "Rua dos Ipês, 56 - Jardim Botânico"),
            Visitante(8, "Ricardo Alves", 50, "999.000.111-22", "Alameda Santos, 789 - Cerqueira César"),
            Visitante(9, "Patrícia Nunes", 27, "000.111.222-33", "Rua das Orquídeas, 101 - Bosque das Flores"),
            Visitante(10, "Lucas Castro", 10, "111.222.333-44", "Avenida das Nações, 202 - Internacional"),
            Visitante(11, "Isabela Rocha", 70, "222.333.444-55", "Rua da Sabedoria, 303 - Vila Esperança"),
            Visitante(12, "Gustavo Henrique", 5, "333.444.555-66", "Travessa da Alegria, 404 - Parque das Crianças"),
            Visitante(13, "Camila Duarte", 22, "444.555.666-77", "Alameda dos Sonhos, 505 - Nova Era"),
            Visitante(14, "Rafael Martins", 45, "555.666.777-88", "Praça Central, 606 - Centro Histórico")
        ]

        self.recintos = [
            Recinto(0, "Aquário Marinho", 15),          # 5/15 (aquáticos)
            Recinto(1, "Aviário", 20),                  # 7/20 (aves)
            Recinto(2, "Savana Carnívora", 8),              # 5/8 (carnívoros)
            Recinto(3, "Planície Herbívora", 12),            # 8/12 (herbívoros)
            Recinto(4, "Terrário", 10),                      # 5/10 (répteis)
            Recinto(5, "Piscina de Mamíferos Aquáticos", 6), # 2/6 (mamíferos aquáticos)
            Recinto(6, "Caverna de Felinos", 5)  # 4/5 (felinos)
        ]

        self.recintos[0].animais = [  # Aquário Marinho
            Animal(0, 3, "Pinguim-imperador", 35.5, "M"),
            Animal(1, 5, "Tubarão-martelo", 230.0, "F"),
            Animal(2, 2, "Peixe-palhaço", 0.25, "M"),
            Animal(3, 7, "Tartaruga-marinha", 85.0, "F"),
            Animal(4, 1, "Leão-marinho", 90.0, "M")
        ]

        self.recintos[1].animais = [  # Aviário
            Animal(0, 4, "Arara-azul", 1.3, "F"),
            Animal(1, 2, "Coruja-das-neves", 2.1, "M"),
            Animal(2, 1, "Tucano-toco", 0.6, "M"),
            Animal(3, 3, "Águia-careca", 4.5, "F"),
            Animal(4, 5, "Pavão-indiano", 5.0, "M"),
            Animal(5, 2, "Beija-flor", 0.02, "F"),
            Animal(6, 4, "Gavião-real", 3.8, "M")
        ]

        self.recintos[2].animais = [  # Savana Carnívora
            Animal(0, 8, "Leão-africano", 190.0, "M"),
            Animal(1, 6, "Tigre-siberiano", 220.0, "F"),
            Animal(2, 4, "Lobo-cinzento", 45.0, "M"),
            Animal(3, 7, "Onça-pintada", 90.0, "F"),
            Animal(4, 5, "Hiena-malhada", 55.0, "F")
        ]

        self.recintos[3].animais = [  # Planície Herbívora
            Animal(0, 10, "Elefante-africano", 6000.0, "M"),
            Animal(1, 8, "Girafa", 800.0, "F"),
            Animal(2, 5, "Zebra", 350.0, "M"),
            Animal(3, 6, "Rinoceronte-branco", 2300.0, "F"),
            Animal(4, 3, "Búfalo-africano", 700.0, "M"),
            Animal(5, 4, "Antílope", 60.0, "F"),
            Animal(6, 7, "Hipopótamo", 1500.0, "M"),
            Animal(7, 2, "Coala", 10.0, "F")
        ]

        self.recintos[4].animais = [  # Terrário
            Animal(0, 15, "Jabuti-piranga", 8.0, "M"),
            Animal(1, 8, "Crocodilo-do-nilo", 500.0, "F"),
            Animal(2, 12, "Iguana-verde", 4.0, "M"),
            Animal(3, 20, "Píton-reticulada", 75.0, "F"),
            Animal(4, 5, "Camaleão", 0.15, "M")
        ]

        self.recintos[5].animais = [  # Piscina de Mamíferos Aquáticos
            Animal(0, 3, "Pinguim-imperador", 35.5, "M"),
            Animal(1, 1, "Leão-marinho", 90.0, "M")
        ]

        self.recintos[6].animais = [  # Caverna de Felinos
            Animal(0, 8, "Leão-africano", 190.0, "M"),
            Animal(1, 6, "Tigre-siberiano", 220.0, "F"),
            Animal(2, 7, "Onça-pintada", 90.0, "F"),
            Animal(3, 3, "Raposa-vermelha", 6.5, "M")
        ]

        self.funcionarios = [
            Funcionario(0, "Pedro", 10, "000.000.000-11", "Rua AAA", "Alimentador de animais"),
            Funcionario(1, "Maria", 25, "111.111.111-11", "Rua BBB", "Veterinária"),
            Funcionario(2, "João", 32, "222.222.222-11", "Rua CCC", "Tosador"),
            Funcionario(3, "Ana", 28, "333.333.333-11", "Rua DDD", "Atendente"),
            Funcionario(4, "Carlos", 40, "444.444.444-11", "Rua EEE", "Gerente"),
            Funcionario(5, "Julia", 22, "555.555.555-11", "Rua FFF", "Banhista"),
            Funcionario(6, "Marcos", 35, "666.666.666-11", "Rua GGG", "Adestrador"),
            Funcionario(7, "Fernanda", 29, "777.777.777-11", "Rua HHH", "Recepcionista"),
            Funcionario(8, "Ricardo", 45, "888.888.888-11", "Rua III", "Tratador de felinos"),
            Funcionario(9, "Patrícia", 33, "999.999.999-11", "Rua JJJ", "Cuidadora de primatas"),
            Funcionario(10, "Lucas", 27, "010.010.010-11", "Rua KKK", "Tratador de aves"),
            Funcionario(11, "Isabela", 31, "020.020.020-11", "Rua LLL", "Veterinária de répteis"),
            Funcionario(12, "Gustavo", 38, "030.030.030-11", "Rua MMM", "Encarregado dos aquários"),
            Funcionario(13, "Camila", 24, "040.040.040-11", "Rua NNN", "Educadora ambiental"),
            Funcionario(14, "Rafael", 42, "050.050.050-11", "Rua OOO", "Especialista em animais noturnos"),
            Funcionario(15, "Beatriz", 26, "060.060.060-11", "Rua PPP", "Tratadora de herbívoros"),
            Funcionario(16, "Eduardo", 50, "070.070.070-11", "Rua QQQ", "Diretor do zoológico"),
            Funcionario(17, "Larissa", 29, "080.080.080-11", "Rua RRR", "Bióloga de campo"),
            Funcionario(18, "Thiago", 36, "090.090.090-11", "Rua SSS", "Tratador de animais exóticos"),
            Funcionario(19, "Vanessa", 30, "101.101.101-11", "Rua TTT", "Coordenadora de alimentação"),
            Funcionario(20, "Felipe", 41, "121.121.121-11", "Rua UUU", "Especialista em grandes mamíferos")
        ]

        self.capacidade_visitantes = capacidade_visitantes
        self.capacidade_recintos = capacidade_recintos
        self.capacidade_funcionarios = capacidade_funcionarios



# ADICIONAR / REMOVER RECINTO
    # Adiciona um recinto
    def adicionar_recinto(self):
        if len(self.recintos) < self.capacidade_recintos:
            id = int(input("Id do recinto: "))
            if self.verificar_id_recinto(id) == None:
                self.recintos.append(Recinto(id, input("Tipo: "), int(input("Capacidade: "))))
            else:
                print("Recinto ja existe")
        else:
            print("Capacidade maxima atingida")

    # Remove um recinto
    def remover_recinto(self):
        if len(self.recintos) == 0:
            print("O zoologico nao tem nenhum recinto")
        else:
            id = int(input("\nId do recinto: "))
            indice = self.verificar_id_recinto(id)
            if indice != None:
                self.recintos.pop(indice)
                print("Recinto removido")
            else:
                print("Recinto nao encontrado")
#



# CONTRATAR / DEMITIR FUNCIONARIO
    # Contrata um funcionario
    def contratar_funcionario(self):
        if len(self.funcionarios) < self.capacidade_funcionarios:
            id = int(input("Id do funcionario: "))
            if self.verificar_id_funcionario(id) == None:
                self.funcionarios.append(Funcionario(id, input("Nome: "), int(input("Idade: ")), input("Cpf: "), input("Endereço: "), input("Funçao: ")))
                print("Funcionario contratado")
            else:
                print("Funcionario ja existe")
        else:
            print("Capacidade maxima de funcionarios atingida")

    # Demite um funcionario
    def demitir_funcionario(self):
        if len(self.funcionarios) == 0:
            print("O zoologico nao tem funcionarios")
        else:
            id = int(input("Id do funcionario: "))
            indice = self.verificar_id_funcionario(id)
            if indice != None:
                self.funcionarios.pop(indice)
                print("Funcionario demitido")
            else:
                print("Funcionario nao encontrado")
#



# REGISTRAR / REMOVER VISITANTE
    # Registra um visitante
    def registrar_visitante(self):
        if len(self.visitantes) < self.capacidade_visitantes:
            id = int(input("Id do visitante: "))
            if self.verificar_id_visitante(id) == None:
                self.visitantes.append(Visitante(id, input("Nome: "), int(input("Idade: ")), input("Cpf: "), input("Endereço: ")))
                print("Visitante registrado")
            else:
                print("Visitante ja esta registrado")
        else:
            print("Capacidade maxima de visitantes atingida")

    # Remove um visitante
    def remover_visitante(self):
        if len(self.visitantes) == 0:
            print("O zoologico nao tem nenhum visitante")
        else:
            id = int(input("Id do visitante: "))
            indice = self.verificar_id_visitante(id)
            if indice != None:
                self.visitantes.pop(indice)
                print("Visitante removido")
            else:
                print("Visitante nao foi encontrado")
#


# EXIBIR RECINTO(S)
    # Exibe dados de um recinto
    def exibir_dados_recinto(self):
        if len(self.recintos) == 0:
            print("O zoologico nao tem nenhum recinto")
        else:
            id = int(input("Id: "))
            indice = self.verificar_id_recinto(id)

            if indice != None:
                self.recintos[indice].exibir_dados()
            else:
                print("Nenhum recinto encontrado")

    # Exibe dados de todos os recintos
    def exibir_dados_recintos(self):
        if len(self.recintos) == 0:
            print("O zoologico nao tem nenhum recinto")
        else:
            encontrado = 0
            for recinto in self.recintos:
                recinto.exibir_dados()
                encontrado = 1
        if(encontrado == 0):
                print("Nenhum recinto encontrado")
#



# EXIBIR FUNCIONARIO(S)
    # Exibe dados de um funcionario
    def exibir_dados_funcionario(self):
        if len(self.funcionarios) == 0:
            print("O zoologico nao tem nenhum funcionario")
        else:
            id = int(input("Id do funcionario: "))
            indice = self.verificar_id_funcionario(id)
            if indice != None:
                self.funcionarios[indice].exibir_dados()
            else:
                print("Funcionario nao foi encontrado")

    # Exibe dados de todos os funcionarios
    def exibir_dados_funcionarios(self):
        if len(self.funcionarios) > 0:
            for funcionario in self.funcionarios:
                funcionario.exibir_dados()
        else:
            print("O zoologico nao tem nenhum funcionarios")
#



# EXIBIR VISITANTE(S)
    # Exibe os dados de um visitante
    def exibir_dados_visitante(self):
        if len(self.visitantes) == 0:
            print("O zoologico nao tem nenhum visitante")
        else:
            id = int(input("Id do visitante: "))
            indice = self.verificar_id_visitante(id)
            if indice != None:
                self.visitantes[indice].exibir_dados()
            else:
                print("Visitante nao foi encontrado")

    # Exibe os dados de todos os visitantes
    def exibir_dados_visitantes(self):
        if len(self.visitantes) > 0:
            for visitante in self.visitantes:
                visitante.exibir_dados()
        else:
            print("O zoologico nao tem nenhum visitante")
#



# VERIFICAR O INDICE PELO ID
    def verificar_id_visitante(self, id: int):
        for i, visitante in enumerate(self.visitantes):
            if visitante.id == id:
                return i
        return None

    def verificar_id_funcionario(self, id: int):
        for i, funcionario in enumerate(self.funcionarios):
            if funcionario.id == id:
                return i
        return None

    def verificar_id_recinto(self, id: int):
        for i, recinto in enumerate(self.recintos):
            if recinto.id == id:
                return i
        return None
#