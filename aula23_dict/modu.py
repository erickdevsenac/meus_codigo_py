import tkinter as tk
from tkinter import simpledialog, messagebox

def mostrar_resultado(resposta):
    if resposta is not None:
        if resposta.strip() == 'entendi':
            messagebox.showinfo('Resultado', 'Muito bem, parabéns!')
        else:
            messagebox.showwarning('Resultado', 'Não, você não entendeu!')

def abrir_dialog():
    pergunta = 'O que entendeu?'
    resposta = simpledialog.askstring('Questão', pergunta)
    mostrar_resultado(resposta)

def criar_interface(root):
    root.title("Exemplo de Diálogo")
    botao = tk.Button(root, text="Abrir Pergunta", command=abrir_dialog)
    botao.pack(pady=20)


