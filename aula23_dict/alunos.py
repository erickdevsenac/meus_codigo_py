import nome

aprovados = []

alunos = {
    'aluno1': {'notas': [10, 8, 7.5]},
    'aluno2': {'notas': [9.5, 7, 10]},
    'aluno3': {'notas': [5, 4.7, 6]}
}

print(nome.imprime_nome('Erickson'))
print(nome.imprime_nome('Vinicius'))
print(nome.imprime_nome('Erica'))

print("\nResultados:")
for nome, info in alunos.items():
    notas = info['notas']
    media = sum(notas) / len(notas)
    print(f"Aluno: {nome}, Notas: {notas}, Média: {media:.2f}", end=" ")
    if media >= 7:
        print("- 🦉 APROVADO")
    else:
        print("- 🤺 REPROVADO")

print("\nAlunos Aprovados:")
for nome, info in alunos.items():
    if sum(info['notas']) / len(info['notas']) >= 7:
        aprovados.append(nome)
        
if aprovados:
    print(", ".join(aprovados))
else:
    print("Nenhum aluno foi aprovado.")