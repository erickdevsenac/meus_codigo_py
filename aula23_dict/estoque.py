from tkinter import *

janela = Tk()
janela.geometry('900x600+10+10')

janela.grid_columnconfigure(0, weight=1)
janela.grid_rowconfigure(0, weight=1)

frame_container = Frame(janela) 
frame_container.grid(row=0, column=0)

frame_principal = Frame(frame_container, bg='black')
frame_principal.pack(expand=False, ipadx=150) 


estoque = {}

def validar_dados(nome_produto, qtd_produto):
    if nome_produto.strip():
        print(f"Nome do produto: {nome_produto}")
        return True, None
    else:
        mensagem = 'Informe um produto válido'
        print(mensagem)
        return False, mensagem

    try:
        int(qtd_produto)
        print(f"Quantidade do produto: {qtd_produto}")
        return True, None
    except ValueError:
        mensagem = 'Informe uma quantidade válida (número inteiro)'
        print(mensagem)
        return False, mensagem

def adiciona_produto():
    nome_produto = entry_nome.get()
    qtd_produto_str = entry_qdt.get()
    valido, mensagem = validar_dados(nome_produto, qtd_produto_str)
    if valido:
        estoque[nome_produto] = qtd_produto_str
        print(f"Produto '{nome_produto}' adicionado ao estoque com quantidade: {qtd_produto_str}")
    else:
        print(f"Erro ao adicionar produto: {mensagem}")

def atualiza_produto():
    nome_produto = entry_nome.get()
    qtd_produto_str = entry_qdt.get()
    valido, mensagem = validar_dados(nome_produto, qtd_produto_str)
    if valido:
        if nome_produto in estoque:
            estoque[nome_produto] = qtd_produto_str 
            print(f"Estoque de '{nome_produto}' atualizado para: {qtd_produto_str}")
        else:
            print(f"Produto '{nome_produto}' não encontrado no estoque.")
    else:
        print(f"Erro ao atualizar produto: {mensagem}")

lb_nome = Label(frame_principal, text='Nome do produto: ', fg='white', bg='black').grid(row=0, column=0, padx=5, pady=5, sticky='w')
entry_nome = Entry(frame_principal)
entry_nome.grid(row=0, column=1, padx=5, pady=5)
lb_qtd = Label(frame_principal,text='Quantidade do produto: ', fg='white', bg='black').grid(row=1, column=0, padx=5, pady=5, sticky='w')
entry_qdt = Entry(frame_principal,)
entry_qdt.grid(row=1, column=1, padx=5, pady=5)
Button(frame_principal,text='Adicionar', command=adiciona_produto).grid(row=2, column=0, columnspan=2, pady=5)
Button(frame_principal,text='Atualizar', command=atualiza_produto).grid(row=3, column=0, columnspan=2, pady=5)

frame_principal.columnconfigure(1, weight=1)
frame_principal.rowconfigure(1, weight=0) 

janela.mainloop()