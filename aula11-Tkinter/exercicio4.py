import tkinter as tk

def mostrar_pares():
    numeros = []
    for entrada in entradas:
        numero = int(entrada.get())
        numeros.append(numero)

    for num in numeros:
        if num % 2 == 0:
            pares = [num for num in numeros if num % 2 == 0]
            resultado_label.config(text=f"Números pares: {pares}")

janela = tk.Tk()
janela.title("Mostrar Números Pares")

entradas = []

for i in range(10):
    label = tk.Label(janela, text=f"Número {i+1}:")
    label.pack(pady=5)
    entrada_teste = tk.Entry(janela)
    entrada_teste.pack(pady=2)
    entradas.append(entrada_teste)

botao_mostrar = tk.Button(janela, text="Mostrar Pares", command=mostrar_pares)
botao_mostrar.pack(pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=10)

janela.geometry("300x400+20+20")
janela.mainloop()