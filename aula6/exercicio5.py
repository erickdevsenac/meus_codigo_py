# # Verificar a Quantidade de Vogais em uma Palavra

# # palavra = input("Entre com uma palavra: ")
# # vogais = 'aeiouAEIOU'
# # vog = 0

# # for letra in palavra:
# #     if letra in vogais:
# #         vog += 1

# # print(vog)

# n = int(input("Quantos números da sequência de Fibonacci deseja ver? "))
# a, b = 0, 1

# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
    
    
    


# num = 1
# for _ in range(3):
#     print(num, end=' ')
    
    
# #2 - Exibir múltiplos de 3 entre 1 e 30

# for i in range(1,31):
#     if i % 3 == 0:
#         print(i)
        
        
# #3 - Soma dos números ímpares entre 1 e 50

# soma_num =0
# for num in range(1, 51, 2):
#     soma_num += num
#     print(soma_num)
    
    
# 4 - Contador de letras em uma frase

palavra = input("Qual a palavra: ")
num_letra = 0
for letra in palavra:
    num_letra += 1
    
print(num_letra)