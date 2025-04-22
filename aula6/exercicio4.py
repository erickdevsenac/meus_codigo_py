#Soma de Números Informados pelo Usuário
# O programa deve pedir 5 números ao usuário e somá-los.

soma = 0
for _ in range(5):
    soma += int(input('Entre com um número números: '))
    
print(soma)