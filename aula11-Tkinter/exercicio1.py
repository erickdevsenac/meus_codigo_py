import tkinter as tk

def verificar_restricao():
    restricao = ''
    numero = entrada.get()
    numero = int(numero)
    
    if(numero == 1 or numero == 2):
        restricao = "2ª Feira"
        
    elif(numero == 3 or numero == 4):
        restricao = "3ª Feira"
        
    elif(numero == 5 or numero == 6):
        restricao = "4ª Feira"
        
    elif(numero == 7 or numero == 8):
        restricao = "5ª Feira"
        
    elif(numero == 9 or numero == 0):
        restricao = "6ª Feira"
        
    else:
        restricao = 'Número inválido!'
    
    resultado.config(text=f"Não pode circular na {restricao}")

janela = tk.Tk()
janela.title("Restrição de Tráfego")
janela.config(background="#000",pady=50)
janela.geometry("900x600")
janela.maxsize(width=1200, height=900)
janela.minsize(width=400, height=200)

entrada_label = tk.Label(text="🚗 Digite o último número da placa:", background='#000', font=60, foreground='white')
entrada_label.pack()

entrada = tk.Entry( background='#abc2bc', font=60, foreground='#000', width=20)
entrada.pack(pady=5)

botao = tk.Button(text="Verificar", background='#abc2bc', font=40, command=verificar_restricao)
botao.pack(pady=10)

resultado = tk.Label(text="", background='#000', font=80, foreground='white' )
resultado.pack(pady=5)

janela.mainloop()
