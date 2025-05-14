from tkinter import *
from tkinter import messagebox

from models.cliente_pf import ClientePF

class ClienteApp:
    def __init__(self, janela):
        self.janela = janela
        janela.geometry('900x600+30+30')
        janela.title('Cadastro de Cliente')
        
        janela.config(bg='#45C4B0')
        
        lb_nome = Label(text='Nome: ')
        lb_email = Label(text='Email: ')
        lb_cpf = Label(text='CPF: ')
        
        entry_nome = Entry()
        entry_email = Entry()
        entry_cpf = Entry()
        
        btn_cadastrar = Button(text='Cadastrar', command=self.salvar_cliente)
        
        lb_nome.grid( row=0, column=0)
        lb_email.grid( row=1, column=0)
        lb_cpf.grid( row=2, column=0)

        entry_nome.grid( row=0, column=1)
        entry_email.grid( row=1, column=1)
        entry_cpf.grid( row=2, column=1)

        btn_cadastrar.grid( row=4, column=0)

    def salvar_cliente(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        cpf = self.entry_cpf.get()
        
        if (not nome or not email or not cpf):
            messagebox.showwarning('Atenção', 'Todos os campos devem estar preenchidos')
            return
        
        cliente = ClientePF(nome, email, cpf)
        self.salvar_cliente(cliente)









# import tkinter as tk
# from tkinter import messagebox
# from models.cliente_pf import ClientePessoaFisica
# from services.persistencia import salvar_cliente

# class ClienteApp:
#     def __init__(self, janela):
#         self.janela = janela
#         janela.title("Cadastro de Cliente")

#         tk.Label(janela, text="Nome:").grid(row=0, column=0)
#         tk.Label(janela, text="Email:").grid(row=1, column=0)
#         tk.Label(janela, text="CPF:").grid(row=2, column=0)

#         self.nome_entry = tk.Entry(janela)
#         self.email_entry = tk.Entry(janela)
#         self.cpf_entry = tk.Entry(janela)

#         self.nome_entry.grid(row=0, column=1)
#         self.email_entry.grid(row=1, column=1)
#         self.cpf_entry.grid(row=2, column=1)

#         self.btn_salvar = tk.Button(janela, text="Salvar", command=self.salvar_cliente)
#         self.btn_salvar.grid(row=3, column=0, columnspan=2)

#     def salvar_cliente(self):
#         nome = self.nome_entry.get()
#         email = self.email_entry.get()
#         cpf = self.cpf_entry.get()

#         if not nome or not email or not cpf:
#             messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos.")
#             return

#         cliente = ClientePessoaFisica(nome, email, cpf)
#         salvar_cliente(cliente)
#         messagebox.showinfo("Sucesso", "Cliente salvo com sucesso!")
#         self.limpar_campos()

#     def limpar_campos(self):
#         self.nome_entry.delete(0, tk.END)
#         self.email_entry.delete(0, tk.END)
#         self.cpf_entry.delete(0, tk.END)
