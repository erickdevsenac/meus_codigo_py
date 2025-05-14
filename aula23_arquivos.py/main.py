# arquivo = 'relatorio.csv'

# try:
#     file = open(arquivo, 'r')
#     conteudo = file.read()
#     print(conteudo)
#     file.close()
# except FileNotFoundError as erro:
#     print("Arquivo não encontrado. Verifique o nome e o caminho.")
    

####
#Criar e escrever em um .csv
# python
# Copiar
# Editar

produto = input('Informe o produto: ')
quantidade = int(input('Informe a quantidade: '))
preco = float(input('Informe o preço: '))

try:
    with open("relatorio.csv", "w") as arquivo:
        arquivo.write("produto,quantidade,preco\n")
        arquivo.write(f"{produto},{quantidade},{preco}\n")
except:
    print('Falha ao criar arquivo')