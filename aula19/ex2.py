from tkinter import *

janela = Tk()
janela.geometry('300x200')

Label(janela, text='teste 1', bg='red').grid(row=0, column=0, sticky="ew")
Label(janela, text='teste 2', bg='green').grid(row=0, column=2, sticky="ew")
Label(janela, text='teste 2', bg='green').grid(row=1, column=1, sticky="ew")

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(2, weight=1)

janela.mainloop()