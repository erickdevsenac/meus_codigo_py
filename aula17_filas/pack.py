from tkinter import *
janela = Tk()
janela.geometry('900x600+10+10')

botao = Button(text= 'teste')
botao2 = Button(text= 'teste2')
botao3 = Button(text= 'teste3')
botao4 = Button(text= 'teste4')
botao.pack(side='bottom')
botao2.pack(side='top', expand=True)
botao3.pack(side='left', padx=200, ipadx=50, ipady=20)
botao4.pack(side='right')

janela.mainloop()