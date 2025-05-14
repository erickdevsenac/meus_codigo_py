import tkinter as tk
from tkinter import simpledialog, messagebox

def janela_ex1():
    contatos = {}
    def adicionar_contato():
        nome = simpledialog.askstring("Contato", "Nome:")
        telefone = simpledialog.askstring("Contato", "Telefone:")
        if nome and telefone:
            contatos[nome] = telefone
            messagebox.showinfo("Sucesso", f"{contatos}")

    janela = tk.Toplevel()
    janela.title("Exercício 1 - Dicionário de Contatos")
    tk.Button(janela, text="Adicionar Contato", command=adicionar_contato).pack(padx=20, pady=20)

def janela_ex2():
    compromissos = {}
    def adicionar_compromisso():
        data = simpledialog.askstring("Compromisso", "Data (DD/MM/AAAA):")
        compromisso = simpledialog.askstring("Compromisso", "Descrição:")
        if data and compromisso:
            compromissos[data] = compromisso
            messagebox.showinfo("Sucesso", f"Compromisso em {data} adicionado!")

    janela = tk.Toplevel()
    janela.title("Exercício 2 - Agenda de Compromissos")
    tk.Button(janela, text="Adicionar Compromisso", command=adicionar_compromisso).pack(padx=20, pady=20)

def janela_ex3():
    produtos = {"Maçã": 3.50, "Banana": 2.00, "Carne": 20.00}
    media = sum(produtos.values()) / len(produtos)
    janela = tk()
    janela.title("Exercício 3 - Valor Médio dos Produtos")
    tk.Label(janela, text=f"Valor médio dos produtos: R${media:.2f}").pack(padx=20, pady=20)

def janela_ex4():
    produtos = {"Sabão": 5.00, "Shampoo": 15.00, "Escova": 8.00, "Toalha": 12.00}
    produtos = {k: v for k, v in produtos.items() if v >= 10}
    janela = tk.Toplevel()
    janela.title("Exercício 4 - Remover Produtos Baratos")
    tk.Label(janela, text="Produtos restantes (>= R$10):").pack()
    for nome, preco in produtos.items():
        tk.Label(janela, text=f"{nome}: R${preco:.2f}").pack()

def janela_ex5():
    dicionario = {"chave1": 10, "chave2": 20}
    chave = simpledialog.askstring("Verificação", "Digite a chave para verificar:")
    resultado = "existe" if chave in dicionario else "não existe"
    messagebox.showinfo("Resultado", f"A chave '{chave}' {resultado} no dicionário.")

def janela_ex6():
    alunos = []
    def cadastrar():
        nome = simpledialog.askstring("Cadastro", "Nome do aluno:")
        nota = float(simpledialog.askstring("Cadastro", "Nota:"))
        status = "Aprovado" if nota >= 6 else "Reprovado"
        alunos.append((nome, nota, status))
        messagebox.showinfo("Cadastrado", f"{nome}: {nota} - {status}")

    janela = tk.Toplevel()
    janela.title("Exercício 6 - Cadastro de Alunos")
    tk.Button(janela, text="Cadastrar Aluno", command=cadastrar).pack(padx=20, pady=20)

def janela_ex7():
    veiculo = {"marca": "Toyota", "modelo": "Corolla", "ano": 2020}
    def atualizar():
        for chave in veiculo:
            novo_valor = simpledialog.askstring("Atualizar", f"{chave.capitalize()} atual: {veiculo[chave]}")
            if novo_valor:
                veiculo[chave] = novo_valor
        messagebox.showinfo("Atualizado", f"Dados atualizados: {veiculo}")

    janela = tk.Toplevel()
    janela.title("Exercício 7 - Atualizar Veículo")
    tk.Button(janela, text="Atualizar Dados", command=atualizar).pack(padx=20, pady=20)

def janela_ex8():
    estoque = {"camiseta": 10, "calça": 5, "tênis": 8}
    total = sum(estoque.values())
    janela = tk.Tk()
    janela.title("Exercício 8 - Soma do Estoque")
    tk.Label(janela, text=f"Total de itens no estoque: {total}").pack(padx=20, pady=20)

def janela_ex9():
    cardapio = {"hamburguer": 15, "batata": 8, "refrigerante": 5}
    def calcular_total():
        total = 0
        for item in cardapio:
            qtd = simpledialog.askinteger("Pedido", f"Quantidade de {item}?")
            if qtd:
                total += cardapio[item] * qtd
        messagebox.showinfo("Total", f"Total da compra: R${total:.2f}")

    janela = tk.Toplevel()
    janela.title("Exercício 9 - Cardápio")
    tk.Button(janela, text="Fazer Pedido", command=calcular_total).pack(padx=20, pady=20)

def janela_ex10():
    boletim = {}
    def adicionar_nota():
        disciplina = simpledialog.askstring("Boletim", "Disciplina:")
        media = float(simpledialog.askstring("Boletim", "Média:"))
        status = "Aprovado" if media >= 6 else "Reprovado"
        boletim[disciplina] = (media, status)
        messagebox.showinfo("Resultado", f"{disciplina}: {media} - {status}")

    janela = tk.Toplevel()
    janela.title("Exercício 10 - Boletim Escolar")
    tk.Button(janela, text="Adicionar Disciplina", command=adicionar_nota).pack(padx=20, pady=20)

root = tk.Tk()
root.title("Exercícios com Dicionários")

funcoes = [
    ("1. Contatos", janela_ex1),
    ("2. Agenda", janela_ex2),
    ("3. Média Produtos", janela_ex3),
    ("4. Remover Produtos", janela_ex4),
    ("5. Verificar Chave", janela_ex5),
    ("6. Cadastro Alunos", janela_ex6),
    ("7. Atualizar Veículo", janela_ex7),
    ("8. Soma Estoque", janela_ex8),
    ("9. Cardápio", janela_ex9),
    ("10. Boletim", janela_ex10),
]

for texto, func in funcoes:
    tk.Button(root, text=texto, width=30, command=func).pack(padx=10, pady=5)

root.mainloop()
