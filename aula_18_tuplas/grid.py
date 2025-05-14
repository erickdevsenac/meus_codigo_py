from tkinter import *
janela = Tk()
janela.geometry('900x600')
janela.title("Tupla de Frutas")
janela.config(background= "black")
 
tupla1 = ("nome1","nome2", "nome3")
 
def desempacotamento():
    nome1, nome2, nome3 = tupla1
    resposta.config(text=f"O primeiro nome {nome1} O segundo nome {nome2} e terceiro nome {nome3}")
 
introducao = Label(text="Aperte o botão para o desempacotamento", bg="black", fg="white")
introducao.grid(row=0, column=0, sticky="w")
 
botao = Button(text="Desempacotar", command=desempacotamento)
botao.grid(row=0, column=2,padx=40)
 
resposta = Label(text=" ", bg="black", fg="white")
resposta.grid(row=2, column=0, columnspan=6)
 
janela.mainloop()