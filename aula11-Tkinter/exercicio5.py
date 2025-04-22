# Peça ao usuário 5 produtos e
# adicione em uma lista. Depois,
# remova um produto informado
# pelo usuário

import tkinter as tk

def remover_produto():
    ...

janela = tk.Tk()
janela.title("Mostrar Números Pares")

entradas = []

for i in range(5):
    label = tk.Label(janela, text=f"Produto {i+1}:")
    label.pack(side=tk.LEFT, padx=5)
    entrada_teste = tk.Entry(janela)
    entrada_teste.pack(side=tk.LEFT, padx=5)
    entradas.append(entrada_teste)

listbox = tk.Listbox()
listbox.pack()

botao_mostrar = tk.Button(janela, text="Remover", command=remover_produto)
botao_mostrar.pack(pady=10)

janela.geometry("300x400+20+20")
janela.mainloop()