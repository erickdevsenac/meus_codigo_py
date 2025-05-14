# Programa que divide dois números
# com tratamento de exceções.
from tkinter import *
from tkinter import simpledialog, messagebox

def divide_numeros():
    entry_n1 = simpledialog.askinteger('Primeiro número', 'Informe o número:')
    entry_n2 = simpledialog.askinteger('Segundo número', 'Informe o número:')
    
    try:
        res = entry_n1 / entry_n2
        messagebox.showinfo('Resultado: ', res)
    except ZeroDivisionError as erro:
        messagebox.showerror('Erro: ', erro)