# Exibir nomes na ordem inversa por linha
# 🔹Solicitar ao usuário a entrada de 5 nomes,
# e que exiba a lista desses nomes na tela.
# Após exibir essa lista, o programa deve mostrar também os nomes na ordem
# inversa em que o usuário os digitou, um por linha.

nomes = []

for i in range(5):
    nome = input('Digite o nome: ')
    nomes.append(nome)

print(nomes)

nomes.reverse()
for nome in nomes:  
    print(nome)

