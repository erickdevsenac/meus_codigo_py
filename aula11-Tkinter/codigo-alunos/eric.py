# 8) Peça ao usuário para digitar 5 números e, 
# Ao final, mostre a lista ordenada.

import tkinter as tk
# from tkinter import messagebox

def ordenar_numeros():
    try:
        # Obter os números dos campos de entrada
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        num3 = float(entrada3.get())
        num4 = float(entrada4.get())
        num5 = float(entrada5.get())
        
        # Criar lista e ordenar
        numeros = [num1, num2, num3, num4, num5]
        numeros_ordenados = sorted(numeros)
        
        # Mostrar resultado
        tk.messagebox.showinfo("Resultado", f"Lista ordenada: {numeros_ordenados}")
    except ValueError:
        tk.messagebox.showerror("Erro", "Por favor, digite apenas números válidos")

# Criar a janela principal
janela = tk.Tk()
janela.title("Ordenador de Números")
janela.geometry("300x250")
janela.configure(background='#49d6ca')
# Rótulo de instrução
tk.Label(janela, text="Digite 5 números:").pack(pady=10)

# Campos de entrada
entrada1 = tk.Entry(janela)
entrada1.pack(pady=2)
entrada2 = tk.Entry(janela)
entrada2.pack(pady=2)
entrada3 = tk.Entry(janela)
entrada3.pack(pady=2)
entrada4 = tk.Entry(janela)
entrada4.pack(pady=2)
entrada5 = tk.Entry(janela)
entrada5.pack(pady=2)

# Botão para ordenar
botao_ordenar = tk.Button(janela, text="Ordenar", command=ordenar_numeros)
botao_ordenar.pack(pady=10)

# Executar a aplicação
janela.mainloop()