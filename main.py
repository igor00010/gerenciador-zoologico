from recinto import Recinto
from animal import Animal
from pessoa import Visitante
from pessoa import Funcionario
from zoologico import Zoologico

zoologico = Zoologico(1000, 50, 200)
while True:
    print("\n0: Sair\n1: Zoologico\n2: Recinto\n3: Visitante\n4: Funcionario")
    opcao = int(input("Opcao: "))
    match(opcao):
        case 1: # Zoologico
            while True:
                print("\n0: Voltar\n1: Adicionar recinto\n2: Remover recinto\n3: Contratar funcionario\n4: Demitir Funcionario\n5: Registrar visitante\n6: Remover visitante")
                opcao = int(input("Opcao: "))
                match(opcao):
                    case 1: # Adiciona um recinto
                        zoologico.adicionar_recinto()
                    case 2: # Remover um recinto
                        zoologico.remover_recinto()
                    case 3: # Contrata um funcionario
                        zoologico.contratar_funcionario()
                    case 4: # Demite um funcionario
                        zoologico.demitir_funcionario()
                    case 5: # Registrar um visitante
                        zoologico.registrar_visitante()
                    case 6: # Remove um visitante
                        zoologico.remover_visitante()
                    case __:
                        break

        case 2: # Recintos
            while True:
                print("\n0: Voltar\n1: Adicionar animal\n2: Remover animal\n3: Exibir animais\n4: Exibir dados de um recinto\n5: Exibir dados de todos os recintos")
                opcao = int(input("Opcao: "))
                match(opcao):
                    case 1: # Adicionar animal a um recinto
                        if len(zoologico.recintos) == 0:
                            print("Zoologico nao tem nenhum recinto")
                        else:
                            id = int(input("Id do recinto: "))
                            indice = zoologico.verificar_id_recinto(id)
                            if indice != None:
                                zoologico.recintos[indice].adicionar_animal()
                                print("Animal adicionado")
                            else:
                                print("Recinto nao existe")

                    case 2: # Remover animal de um recinto
                        if len(zoologico.recintos) <= 0:
                            print("O zoologico nao tem nenhum recinto")
                        else:
                            id = int(input("Id do recinto: "))
                            indice = zoologico.verificar_id_recinto(id)
                            if indice != None:
                                zoologico.recintos[indice].remover_animal()
                                print("Animal removido")
                            else:
                                print("Recinto nao existe")

                    case 3: # Exibir animais de um recinto
                        if len(zoologico.recintos) == 0:
                            print("O zoologico nao tem nenhum recintos")
                        else:
                            id = int(input("Id do recinto: "))
                            indice = zoologico.verificar_id_recinto(id)
                            if indice != None:
                                zoologico.recintos[indice].exibir_animais()
                            else:
                                print("Recinto nao existe")

                    case 4: # Exibir dados de um recinto
                        if len(zoologico.recintos) == 0:
                            print("O zoologic nao tem nenhum recintos")
                        else:
                            zoologico.exibir_dados_recinto()

                    case 5: # Exibir dados de todos os recintos
                        if len(zoologico.recintos) == 0:
                            print("O zoologic nao tem nenhum recintos")
                        else:
                            zoologico.exibir_dados_recintos()

                    case __:
                        break

        case 3: # Visitantes
            while True:
                print("\n0: Voltar\n1: Exibir dados de um visitante\n2: Exibir dados de todos os visitantes")
                opcao = int(input("Opcao: "))
                match(opcao):
                    case 1: # Exibe os dados de um visitante
                        zoologico.exibir_dados_visitante()

                    case 2: # Exibe os dados de todos os visitantes
                        zoologico.exibir_dados_visitantes()

                    case __: # Voltar
                        break

        case 4: # Funcionarios
            while True:
                print("\n0: Voltar\n1: Exibir dados de um funcionario\n2: Exibir dados de todos os funcionarios")
                opcao = int(input("Opcao: "))
                match(opcao):
                    case 1: # Exibe os dados de um funcionario
                        zoologico.exibir_dados_funcionario()

                    case 2: # Exibe os dados de todos os funcionarios
                        zoologico.exibir_dados_funcionarios()

                    case __: # Voltar
                        break

        case __: # Sair
            break