from tkinter import *

janela = Tk()
janela.geometry('500x500')
janela.title("Sets de Cores")
janela.config(background="lightblue")

frame_principal = Frame(janela, background="white")
frame_principal.pack()

frame_secum = Frame(janela, background="white")
frame_secum.pack()



ordem = ""
contador = 0 

def selecionar():
    global ordem, contador
    opcao = opcao_confirmada.get()
    contador += 1  
    numero_atendimento = f"Nº {contador:03d}" 

    match opcao:
        case "1":
            ordem = "Atendimento de Urgência a caminho. 3 minutos no máximo."
        case "2":
            ordem = "Atendimento com medicação intensa encaminhado."
        case "3":
            ordem = "Atendimento com soros antiofídicos encaminhado."
        case "4":
            ordem = "Atendimento entrou na fila de atendimento."
        case "5":
            ordem = "Medicação e Soro Agendado."
        case _:
            ordem = "Opção inválida. Digite um número de 1 a 5."
            contador -= 1  # Não conta erro como atendimento

    resposta.config(text=f"{ordem}\n{numero_atendimento if opcao in ['1','2','3','4','5'] else ''}")

alternativa1 = Label(frame_principal, text="Selecione o Estado de Gravidade:", font=("Arial", 13, "bold"), foreground="black")
alternativa1.grid(row=0, column=1, ipady=5, ipadx=5,  sticky=N, pady=10, padx=30)

alternativa2 = Label(frame_principal, text="Digite 1:", font=("Arial", 12, "bold"), background="lightgreen", pady=15, padx=20)
alternativa2.grid(row=3, column=0, sticky=E, ipady=2)

alternativa22 = Label(frame_principal, text= "Para Sinais de AVC, Ataque Cardíaco, Fraturas Internas ou Externas", font=("Arial", 12,), background="lightgreen", pady=15, padx=20, width=50)
alternativa22.grid(row=3, column=1, sticky=W, ipady=2)

alternativa33 = Label(frame_principal, text="Digite 2:", font=("Arial", 12, "bold"), background="lightgreen", pady=15, padx=20)
alternativa33.grid(row=6, column=0, sticky=E, ipady=2)

alternativa3 = Label(frame_principal, text="Para Sinais de Inflamações e Infecções Profundas", font=("Arial", 12), background="lightgreen", pady=15, padx=20, width=50)
alternativa3.grid(row=6, column=1, sticky=W, ipady=2)

alternativa44 = Label(frame_principal, text="Digite 3:", font=("Arial", 12, "bold"), background="lightgreen", pady=15, padx=20)
alternativa44.grid(row=8, column=0, sticky=E, ipady=2)

alternativa4 = Label(frame_principal, text="Para Ataques de Animais Peçonhentos ou Domésticos", font=("Arial", 12), background="lightgreen", pady=15, padx=20, width=50)
alternativa4.grid(row=8, column=1, sticky=W, ipady=2)

alternativa55 = Label(frame_principal, text="Digite 4:", font=("Arial", 12, "bold"), background="lightgreen", pady=15, padx=20)
alternativa55.grid(row=10, column=0, sticky=E, ipady=2)

alternativa5 = Label(frame_principal, text="Para Náuseas, Dor de Barriga, Dor nas Costas, Etc", font=("Arial", 12), background="lightgreen", pady=15, padx=20, width=50)
alternativa5.grid(row=10, column=1, sticky=W, ipady=2)

alternativa66 = Label(frame_principal, text="Digite 5:", font=("Arial", 12, "bold"), background="lightgreen", pady=15, padx=20)
alternativa66.grid(row=12, column=0, sticky=E, ipady=2)

alternativa6 = Label(frame_principal, text="Para Consulta já Marcada", font=("Arial", 12), background="lightgreen", pady=15, padx=20, width=50)
alternativa6.grid(row=12, column=1, sticky=W, ipady=2)

opcao_confirmada = Entry(frame_secum)
opcao_confirmada.grid(row=14, column=0)

botao_adc = Button(frame_secum, text="Confirmar", command=selecionar, font="Arial")
botao_adc.grid(row=16, column=0)

resposta = Label(frame_secum, text=" ", font="Arial", wraplength=400, justify=LEFT)
resposta.grid(row=18, column=0, sticky=EW)

janela.mainloop()
