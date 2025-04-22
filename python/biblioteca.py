carros = ["Fusca", "Lamborghini", "Ferrari", "Porshe"]
marcos_internet = [1994, 1997, 2002, 2007]

i = 1


def adiciona_carro(carro):
    carros.append(carro)
    # list.append(x)
    
adiciona_carro("Fiesta")
adiciona_carro("Pegeout")

for carro in carros:
    print(f'{i} - {carro}')
    i+=1