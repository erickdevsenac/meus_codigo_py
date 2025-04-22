# Crie uma pilha vazia e permita ao usuário empilhar 
# 5 números digitados. Em seguida,
# exiba o conteúdo da pilha.
import tkinter as tk
janela = tk.Tk()


pilha = [] 
entradas = []


def exibir():
    resultado_label.config(text=pilha)
    
def empilhar_numeros():

    for entrada in entradas:
        numero = int(entrada.get())
        pilha.append(numero)
        
    resultado_label.config(text=f"{pilha}")

for i in range(5):
    label = tk.Label(janela, text=f"Número {i+1}:")
    label.pack(pady=5)
    entrada_numero = tk.Entry(janela)
    entrada_numero.pack(pady=5)
    entradas.append(entrada_numero)



janela.title("Empilhe 5 Números")
janela.config(background="red")
janela.geometry("400x400")
calcular_button = tk.Button(janela, text="Números digitados", command=empilhar_numeros)
calcular_button.pack(pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=10)

janela.mainloop()








# # Crie uma lista com 5 nomes e exiba todos os nomes um por um.
# import tkinter as tk

# def exibir_lista():
#     nomes = []
#     for entrada in entradas:
#         nomes.append(entrada.get())
#     listbox.delete(0, tk.END)
    
#     for nome in nomes:
#         listbox.insert(tk.END,nome)

# janela = tk.Tk()

# janela.title("5 nomes")

# entradas = []

# for i in range(5):
#     label = tk.Label(janela, text=f"Nome {i+1}:")
#     label.pack(padx=5)
#     entrada_nome = tk.Entry(janela)
#     entrada_nome.pack(padx=5)
#     entradas.append(entrada_nome)

# listbox = tk.Listbox()
# listbox.pack()

# botao_mostrar = tk.Button(janela, text="Exibir lista", command=exibir_lista)
# botao_mostrar.pack(pady=10)

# janela.geometry("300x400+20+20")
# janela.mainloop()