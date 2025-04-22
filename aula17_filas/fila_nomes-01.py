# Crie uma fila com 5 nomes. 
# Mostre a fila e depois remova 
# o primeiro nome (simulando atendimento).

from tkinter import *
janela = Tk()
janela.geometry('900x600+10+10')

nome = []

for i in range(5):
    lb_nome = Label(text = 'teste').pack(side='left')
    entry_nome = Entry()
    entry_nome.pack(side='left')
    lb = Label().pack()

janela.mainloop()