import tkinter as tk
 
janela = tk.Tk()
janela.title("Verificar nomes")
janela.geometry("400x400")
nomes = []
lista_nomes = []
 
def verificar_nomes():
    lista_nomes = entry_nomes.get()
    for i in range (7):
        nome = input('Digite os nomes: ')
        nomes.append(nome)
        tk.Label('Lista de nomes: ', nomes)
 
def pedir_nome_e_verificar (lista_de_nomes):
    nome = entry_nomes.get()
    nome_para_verificar = tk.Label ("Verificar Nome", "Digite o nome que você quer verificar:")
    if nome_para_verificar:
        resultado = verificar_nomes (lista_de_nomes, nome_para_verificar)
        tk.Label ("Resultado", {resultado})
 
 
 
botao_iniciar = tk.Button (text="Escreva os nomes", command=pedir_nome_e_verificar)
entry_nomes = tk.Entry ()
botao_iniciar.pack (padx=20, pady=20)
entry_nomes.pack ()
otao_enviar = tk.Button (text= 'Enviar', command= verificar_nomes ).pack ()
 
janela.mainloop()
