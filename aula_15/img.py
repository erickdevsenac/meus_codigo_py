import tkinter as tk

janela = tk.Tk()
janela.title("Sua Janela") # Adicione um título para a janela

logo = tk.PhotoImage(file='aula_15\\images\\logo.png')
logo = logo.subsample(3,3)
lb_logo = tk.Label(janela, image=logo, background='#00513f')    
lb_logo.grid(row=0, column=0)

lb_title = tk.Label(text='Aproveite+', font=('Georgia', 50), background='#00513f', fg='#42f5ef')
lb_title.grid(row=1, column=0)

lb_user = tk.Label(text='Usuário', font=15, background='#00513f', fg='#42f5ef')
lb_user.grid(row=3, column=0, pady=(50, 0))
lb_inputUser = tk.Entry()
lb_inputUser.grid(row=4, column=0, pady=(0,20))

lb_pass = tk.Label(text='Senha', font=15, background='#00513f', fg='#42f5ef')
lb_pass.grid(row=5, column=0)
lb_inputUser = tk.Entry()
lb_inputUser.grid(row=6, column=0, pady=(0,20))

bt1 = tk.Button(text="Enviar", font=("Georgia", 18), bg='#00513f', fg='white', bd=0, highlightthickness=0)
bt1.grid(row=7, column=0, ipadx=700)

window_width = 600
window_height = 400

janela.config(background='#00513f')
janela.geometry('1520x900+0+0')
janela.mainloop()


# import tkinter as tk
# from tkinter import messagebox

# pilha = []

# def empilhar():
#     valor = entrada.get()
#     if valor:
#         pilha.append(valor)
#         entrada.delete(0, tk.END)
#         atualizar_pilha()

# def desempilhar():
#     if not pilha:
#         messagebox.showinfo("Aviso", "A pilha está vazia!")
#     else:
#         item = pilha.pop()
#         messagebox.showinfo("Desempilhado", f"Valor desempilhado: {item}")
#         atualizar_pilha()

# def atualizar_pilha():
#     lista.delete(0, tk.END)
#     for item in reversed(pilha):
#         lista.insert(tk.END, item)

# # Interface gráfica simples
# janela = tk.Tk()
# janela.title("Pilha Simples")

# entrada = tk.Entry(janela)
# entrada.pack()

# tk.Button(janela, text="Empilhar", command=empilhar).pack()
# tk.Button(janela, text="Desempilhar", command=desempilhar).pack()
# lista = tk.Listbox(janela)
# lista.pack()

# logo =tk.PhotoImage(file='aula_15\images\logo2.png')
# logo = logo.subsample(3,3)
# ib_logo = tk.Label(janela, image = logo, bg='#00513f' )
# ib_logo.grid(row = 20, column= 10)

# janela.mainloop()



# import tkinter as tk
# janela = tk.Tk()
 
 
# pilha = []
# entradas = []
 
# def exibir():
#     resultado_label.config(text=pilha)
   
# def empilhar_numeros():
#     for entrada in entradas:
#         numero = int(entrada.get())
#         pilha.append(numero)
       
#     resultado_label.config(text=f"{pilha}")
 
# for i in range(5):
#     label = tk.Label(janela, text=f"Número {i+1}:")
#     label.grid(pady=5)
#     entrada_numero = tk.Entry(janela)
#     entrada_numero.grid(pady=5)
#     entradas.append(entrada_numero)
 
# logo = tk.PhotoImage(file='aula_15\images\logo2.png')
# logo = logo.subsample(5,5)
# lb_logo = tk.Label(janela, image=logo, background='black')    
# lb_logo.grid(row=0, column=0)
 
 
# janela.title("Empilhe 5 Números")
# janela.config(background="Purple")
# janela.geometry("600x400")
# calcular_button = tk.Button(janela, text="Números digitados", command=empilhar_numeros)
# calcular_button.grid(pady=10)
 
# resultado_label = tk.Label(janela, text="")
# resultado_label.grid(pady=10)

# janela.mainloop()