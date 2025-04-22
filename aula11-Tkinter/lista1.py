# Peça 5 números ao usuário, 
# guarde-os em uma lista e calcule a média.

import tkinter as tk

janela = tk.Tk()
lista_numeros = []

def cadastrar():
    numero_digitado = entrada_user.get()
    lista_numeros.append(int(numero_digitado))
    
    if(numero_digitado):
        lp_lista.insert(tk.END, numero_digitado)
    
    entrada_user.delete(0)
    
def calcula_media():
    acumulador = 0
    for i in range(len(lista_numeros)):
        acumulador = acumulador + lista_numeros[i]
    
    resultado = acumulador / len(lista_numeros)
    
    lb_media.config(text=f'A média é: {resultado}')
    
lb_entrada = tk.Label(text="Digite um número:")
lb_entrada.grid(row=2, column=1, pady=20, padx=20)

entrada_user = tk.Entry()
entrada_user.grid(row=2,column=2)

btn_enviar = tk.Button(text='Cadastrar',command=cadastrar)
btn_enviar.grid(row=2, column=3)

lp_lista= tk.Listbox()
lp_lista.grid(row=3, column=2)

btn_media = tk.Button(text='Calcular média', command=calcula_media)
btn_media.grid(row=4, column=1)

lb_media = tk.Label(text='', font=60)
lb_media.grid(row=5, column=2)

janela.mainloop()