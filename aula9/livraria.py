'''
O programa de fidelidade de uma determinada livraria premia seus
clientes de acordo com o número de livros comprados a cada semestre.

 Os pontos são atribuídos da seguinte forma:
•Se um cliente comprar 0 livros, ele ganhará 0 pontos. ***
•Se um cliente comprar 1 livro, ele ganhará 5 pontos.
•Se um cliente comprar 2 livros, ele ganhará 15 pontos.
•Se um cliente comprar 3 livros, ele ganhará 30 pontos.
•Se um cliente comprar 4 ou mais livros, ele ganhará 60 pontos.

Lista de brindes:
De 20 à 30 pontos o cliente poderá escolher entre: Uma EcoBag OU Caneta personalizada
De 35-60 pontos o cliente poderá escolher entre:
 Um livro (com valor máximo de R$30,00) OU Luminária de cabeceira.
Acima de 65 o cliente poderá escolher entre: 2 livros (com valor máximo de R$100,00) OU Powerbank

Obs: Os pontos são acumulativos, e contado a cada compra realizada pelo cliente.

Ex: Se o cliente na semana 1 comprar 2 livros de uma única vez ele receberá 15 pontos,
 se na semana 2 ele comprar 1 único livro receberá 5 pontos totalizando 20 pontos em duas semanas.

Crie um programa que leia o número de livros comprado por um usuário e exiba o número
de pontos correspondentes e qual brinde ele poderá escolher.
'''


print("Bem-vindo ao Programa de Fidelidade da Livraria!")

total_pontos = 0

while True:
    livros_comprados = int(input("\nDigite o número de livros comprados nesta compra (ou digite 0 para sair): "))
    if livros_comprados < 0:
        print("Por favor, insira um número válido de livros.")
        continue

    if livros_comprados == 0:
        break

    if livros_comprados == 0:
        pontos_adicionais = 0
    elif livros_comprados == 1:
        pontos_adicionais = 5
    elif livros_comprados == 2:
        pontos_adicionais = 15
    elif livros_comprados == 3:
        pontos_adicionais = 30
    elif livros_comprados >= 4:
        pontos_adicionais = 60

    total_pontos += pontos_adicionais

    print(f"\nPontos ganhos nesta compra: {pontos_adicionais}")
    print(f"Total de pontos acumulados: {total_pontos}")

if 20 <= total_pontos <= 30:
    print("Você pode escolher entre: 1- Uma EcoBag OU 2- Caneta personalizada.")
    op = input('Digite a opção desejada: ')
    if op == '1':
        print('Parabéns você ganhou uma EcoBag')
    else:
        print('Parabéns você ganhou uma Caneta personalizada')

elif 35 <= total_pontos <= 60:
    print("Você pode escolher entre: 1- Um livro (com valor máximo de R$30,00) OU 2- Luminária de cabeceira.")
    op = input('Digite a opção desejada: ')
    if op == '1':
        print('Parabéns você ganhou um livro')
    else:
        print('Parabéns você ganhou uma Luminária de cabeceira')

elif total_pontos > 65:
    print("\nVocê pode escolher entre: 1- 2 livros (com valor máximo de R$100,00) OU 2- Powerbank.")
    op = input('Digite a opção desejada: ')
    if op == '1':
        print('Parabéns você ganhou 2 livros')
    else:
        print('Parabéns você ganhou um Powerbank')

else:
    print("Você ainda não tem pontos suficientes para trocar por brindes.")

print("\nFim das compras. Resumo final:")
print(f"Total de pontos acumulados: {total_pontos}")
