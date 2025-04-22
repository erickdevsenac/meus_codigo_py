'''Exercício 3 - Triângulo de números
🔹 Descrição: O usuário informa um número N, e o programa exibe um triângulo numérico.

Se N = 5, a saída será:

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5'''


# numero_N = int(input('Qual o número: '))
# numero_N = 5

# for i in range(1, numero_N+1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()
    
    
    
'''Exercício 2 - Exibir a tabuada de 1 a 10
🔹 Descrição: O programa deve exibir a tabuada de 1 a 10, no seguinte formato:

1 x 1 = 1
1 x 2 = 2
...
10 x 10 = 100'''

'''
Desafio Extra para os Alunos
📌 Criar um programa que desenhe um losango de asteriscos.

Se N = 5, a saída será:

  *  
 ***
*****
 ***
  *
  
  '''
  
n = 5

for i in range(1, n+1, 2):
    for j in range((n-i) // 2):
        print(' ', end=' ')
    
    for j in range(i):
        print('*', end=' ')
        
    print()
    
for i in range(n-2,0,-2):
    for j in range((n-i) // 2):
        print(' ', end=' ')
    
    for j in range(i):
        print('*', end=' ')
    print()