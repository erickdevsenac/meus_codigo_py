import tkinter as tk

def troca_valor():
    atualizado = novo_texto.get()
    titulo.config(text=atualizado)

#configuração da JANELA
janela = tk.Tk()

janela.title('Minha janela legal')
janela.config(background="#25b38f")
janela.geometry("900x600")
janela.maxsize(width=1200, height=900)
janela.minsize(width=400, height=200)
# janela.resizable(False, False)

titulo = tk.Label(text="Troca de texto", fg='white',bg='black', font=60)
titulo.pack()

novo_texto = tk.Entry(text='Digite o novo texto')
novo_texto.pack()

novo_botao = tk.Button(text='Enviar', background='green', foreground='white', command=troca_valor)
novo_botao.pack()

janela.mainloop()