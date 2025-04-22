"""temperatura = float(input("Digite a temperatura atual (°C): "))

if temperatura >= 30:
    print("Está muito quente! 🥵")
elif temperatura >= 20:
    print("Temperatura agradável. ☀️")
elif temperatura >= 10:
    print("Está friozinho. 🧥")
else:
    print("Muito frio! ❄️")"""



""" valor_compra = float(input("Qual o valor da compra: "))

# maior ou igual a R$ 500, aplicar 10% de desconto. Se o valor for entre R$ 200 e R$ 499,
# aplicar 5% de desconto

if(valor_compra > 500):
    total_pago = (valor_compra * 0.10) + valor_compra
    print(f'O valor pago foi {total_pago}')
    
elif(valor_compra > 200):
    total_pago = (valor_compra * 0.05) + valor_compra
    print(f'O valor pago foi {total_pago}')

else:
    print(f'O valor pago foi {valor_compra}')"""
    

# 2- A lanchonete GostoSoft vende apenas um tipo de sanduíche, 
# cujo recheio inclui duas fatias de queijo, uma fatia de presunto e uma rodela de hambúrguer.
# Sabendo que cada fatia de queijo ou presunto pesa 50 gramas,
# e que a rodela de hambúrguer pesa 100 gramas, faça um
# algoritmo em que o dono forneça a quantidade de sanduíches a fazer,
# e a máquina informe as quantidades (em quilos) de queijo, presunto 
# e carne necessários para compra.

qtd_sanduiche = int(input("Informe a quantidade de sanduíches a fazer: "))

queijo = (100 * qtd_sanduiche) / 1000
presunto =( 50 * qtd_sanduiche) / 1000
hamburguer = (100 * qtd_sanduiche) / 1000

print(f'A quantidade que deve ser comprada é: ')
print(f'{queijo} kg')
print(f'{presunto} kg')
print(f'{hamburguer} kg')


