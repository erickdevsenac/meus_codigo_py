fila = [] # criando lista

while True: # laço de repetição
    print("\n1 - Adicionar cliente")
    print("2 - Atender cliente")
    print("3 - Ver fila")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do cliente: ")
        fila.append(nome)
        print(f"{nome} entrou na fila.")
    elif opcao == "2":
        if fila:
            atendido = fila.pop(0)
            print(f"{atendido} foi atendido.")
        else:
            print("Fila vazia!")
    elif opcao == "3":
        print("Fila atual:", fila)
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")