from tkinter import *
# Criar uma lista e exibir os nomes

janela=Tk()
janela.title("Lista Nomes") # Titulo da Janela
janela.geometry("500x500") #Tamanho da Janela
janela.config(bg="lightblue")

listaNomes=["Gabriela", "Tiago", "Vegas", "Rogeria", "Ace"]
#Declarando os valores da lista a serem exibidos

lista_Nomes=Listbox(janela) #Utilizei a listbox para gerar uma lista com todos os itens
#e poder selecionar
for alunos in listaNomes:
    lista_Nomes.insert(END,alunos)
    lista_Nomes.pack() #Usei para executar o insert e fazer a adiação dos alunos
    #no final da lista

janela.mainloop() # Para deixar a janela em andamento
