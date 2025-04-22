import random

alunos = ['Erick', 'Anthony', 'Leileane', 'Erica', 'Giovanni']


def sortear_duplas(lista):
    if len(lista) < 2:
        return "Não há alunos suficientes para sortear."

    vendedores = lista[:] 
    random.shuffle(vendedores) 

    clientes = lista[:]  
    random.shuffle(clientes)  

    duplas = []
    for i in range(len(lista)):
        duplas.append({'vendedor': vendedores[i], 'cliente': clientes[i]})

    return duplas

duplas_sorteadas = sortear_duplas(alunos)

for dupla in duplas_sorteadas:
    print(f"Vendedor: {dupla['vendedor']} - Cliente: {dupla['cliente']}")