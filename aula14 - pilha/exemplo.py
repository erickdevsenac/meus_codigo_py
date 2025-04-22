pilha = []

while True:
    print("S\nMenu:")
    print("1 - Empilhar")
    print("2 - Desempilhar")
    print("3 - Ver pilha")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item para empilhar: ")
        pilha.append(item)
        print(f"{item} foi empilhado.")
    elif opcao == "2":
        if pilha:
            removido = pilha.pop()
            print(f"{removido} foi desempilhado.")
        else:
            print("Pilha vazia!")
    elif opcao == "3":
        print("Pilha atual:", pilha)
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")