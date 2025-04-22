import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

class Funcs():
    def limpa_tela(self):
        self.entrada_cod.delete(0, tk.END)
        self.entrada_nome.delete(0, tk.END)
        self.entrada_telefone.delete(0, tk.END)
        self.entrada_cidade.delete(0, tk.END)

class Application(Funcs):

    def __init__(self):

        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()

        self.janela.mainloop()
    

    def tela(self):

        self.janela.title('Cadastro de clientes')

        self.janela.configure(background='#1e3743')

        self.janela.geometry('700x500')

        self.janela.maxsize(width=900, height=700)

        self.janela.minsize(width=500, height=400)
    

    def frames_da_tela(self):

        self.frame_1 = tk.Frame(self.janela, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fa6', highlightthickness=3)
        self.frame_1.place(relx= 0.02, rely = 0.02, relwidth=0.96, relheight = 0.46)

        self.frame_2 = tk.Frame(self.janela, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fa6', highlightthickness=3)
        self.frame_2.place(relx= 0.02, rely = 0.5, relwidth=0.96, relheight = 0.46)

    def widgets_frame1(self):

        self.lb_cod = tk.Label(text="Código", foreground='#107db2', background='#dfe3ee')
        self.lb_cod.place(relx=0.05, rely=0.05)

        self.entrada_cod = tk.Entry()
        self.entrada_cod.place(relx=0.05, rely=0.10,  relwidth=0.08)

        self.lb_nome = tk.Label(text="Nome", foreground='#107db2', background='#dfe3ee')
        self.lb_nome.place(relx=0.05, rely=0.20)

        self.entrada_nome = tk.Entry()
        self.entrada_nome.place(relx=0.05, rely=0.25,  relwidth=0.8)

        self.entrada_telefone = tk.Label(text="Telefone", foreground='#107db2', background='#dfe3ee')
        self.entrada_telefone.place(relx=0.05, rely=0.30)

        self.entrada_telefone = tk.Entry()
        self.entrada_telefone.place(relx=0.05, rely=0.35,  relwidth=0.4)

        self.lb_cidade = tk.Label(text="Cidade", foreground='#107db2', background='#dfe3ee')
        self.lb_cidade.place(relx=0.5, rely=0.30)

        self.entrada_cidade = tk.Entry()
        self.entrada_cidade.place(relx=0.5, rely=0.35,  relwidth=0.4)

        #Botão limpar
        self.bt_limpar = tk.Button(self.frame_1, text = 'Limpar', bd=2, bg='#107db2', fg='white', font= ('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx = 0.2, rely=0.1, relwidth = 0.1, relheight = 0.15)
        self.bt_buscar = tk.Button(self.frame_1, text = 'Buscar', bd=2, bg='#107db2', fg='white', font= ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx = 0.3, rely=0.1, relwidth = 0.1, relheight = 0.15)
        self.bt_novo = tk.Button(self.frame_1, text = 'Novo', bd=2, bg='#107db2', fg='white', font= ('verdana', 8, 'bold'))
        self.bt_novo.place(relx = 0.6, rely=0.1, relwidth = 0.1, relheight = 0.15)
        self.bt_alterar = tk.Button(self.frame_1, text = 'Alterar', bd=2, bg='#107db2', fg='white', font= ('verdana', 8, 'bold'))
        self.bt_alterar.place(relx = 0.7, rely=0.1, relwidth = 0.1, relheight = 0.15)
        self.bt_apagar = tk.Button(self.frame_1, text = 'Apagar', bd=2, bg='#d25', fg='white', font= ('verdana', 8, 'bold'))
        self.bt_apagar.place(relx = 0.8, rely=0.1, relwidth = 0.1, relheight = 0.15)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height= 3, columns=('col1','col2','col3','col4'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Cod')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Telefone')
        self.listaCli.heading('#4', text='Cidade')

        self.listaCli.column('#0',width=1)
        self.listaCli.column('#1',width=50)
        self.listaCli.column('#2',width=200)
        self.listaCli.column('#3',width=125)
        self.listaCli.column('#4',width=125)

        self.listaCli.place(relx=0.01,rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = tk.Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll = self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

Application()