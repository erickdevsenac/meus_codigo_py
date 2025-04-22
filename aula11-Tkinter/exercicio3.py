# Peça 5 palavras ao usuário e exiba
# a maior (em número de letras).

import tkinter as tk
janela = tk.Tk()
janela.geometry("400x300+10+10")

lista_palavras = []

def cadastra_palavra():
    nova_palavra = entry_palavra.get()
    lista_palavras.append(nova_palavra)
    # verifica_maior()
    
def verifica_maior():
    maior_palavra = ''
    for i in range(len(lista_palavras)):
        if len(lista_palavras[i]) > len(maior_palavra):
            maior_palavra = lista_palavras[i]
    lb_maior.config(text=maior_palavra)

lb_instrucao = tk.Label(text='Informe uma palavra: ').pack()
entry_palavra = tk.Entry()
entry_palavra.pack()
bt_enviar = tk.Button(text='Enviar', command=cadastra_palavra ).pack()
bt_maior = tk.Button(text='Maior', command=verifica_maior)
bt_maior.pack()
lb_maior = tk.Label(text='')
lb_maior.pack()

janela.mainloop()