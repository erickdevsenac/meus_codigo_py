from tkinter import *
from datetime import datetime, timedelta, date
 
janela = Tk()
janela.geometry('900x600')
janela.title("Agendamento para Dentista")
janela.config(background= "#5ce1e6")
tarefa = ""
frame_principal = Frame(janela,bg="#5ce1e6")
frame_principal.grid()
frame_secundario = Frame(frame_principal, bg="black")
frame_secundario.grid(row=18, column=0)
scrollbar = Scrollbar(frame_secundario)
scrollbar.grid(row=18, column=2, sticky='ns')
lista = Listbox(yscrollcommand=scrollbar.set)

def confirmar_procedimento():
    global tarefa
    opcao = entrada_procedimento.get()
    match opcao:
        case "1":
            tarefa = "Extração Dentária"
        case "2":
            tarefa = "Limpeza dentaria"
        case "3":
            tarefa = "Clareamento Dental"
        case "4":
            tarefa = "Instalação do aparelho"
        case "5":
            tarefa = "Manutenção do Aparelho"

def validar_data():
    minutos_para_prazo_str = entrada_minutos.get()
    minutos_para_prazo_int = int(minutos_para_prazo_str)
    horas_para_prazo_str = entrada_horas.get()
    horas_para_prazo_int = int(horas_para_prazo_str)
    data_base_str = entrada_data.get()
    data_base = datetime.strptime(data_base_str, "%d/%m/%Y")
    prazo = (data_base + timedelta(hours=horas_para_prazo_int, minutes=minutos_para_prazo_int))
    lista.insert(END,f"Procedimento: {tarefa} agendada para {prazo.strftime('%d/%m/%Y %H:%M')}")
    
introducao_procedimento = Label(frame_principal, text="Digite uma das opções para saber qual sera procedimento que ira ser realizado: ", bg="#5ce1e6", fg="white", font=("Arial",15))
introducao_procedimento.grid(row=1, column=0, sticky="w")

introducao_opcao1 = Label(frame_principal ,text="1-Extração Dentária", bg="#5ce1e6", fg="white", font=("Arial",12))
introducao_opcao1.grid(row=2, column=0, sticky="we")

introducao_opcao2 = Label(frame_principal, text="2-Limpeza dentaria", bg="#5ce1e6", fg="white", font=("Arial",12))
introducao_opcao2.grid(row=3, column=0, sticky="we")

introducao_opcao3 = Label(frame_principal, text="3-Clareamento Dental", bg="#5ce1e6", fg="white", font=("Arial",12))
introducao_opcao3.grid(row=4, column=0, sticky="we")

introducao_opcao4 = Label(frame_principal, text="4-Instalação do aparelho", bg="#5ce1e6", fg="white", font=("Arial",12))
introducao_opcao4.grid(row=5, column=0, sticky="we")

introducao_opcao5 = Label(frame_principal, text="5-Manutenção do Aparelho", bg="#5ce1e6", fg="white", font=("Arial",12))
introducao_opcao5.grid(row=6, column=0, sticky="we")

entrada_procedimento = Entry(frame_principal)
entrada_procedimento.grid(row=7, column=0)

botao_procedimento = Button(frame_principal, text="Confirmar", font=("Arial",12, "bold"), command=confirmar_procedimento)
botao_procedimento.grid(row=8, column=0 ,ipadx=12 ,ipady=5, pady=5)

introducao_data = Label(frame_principal, text="Digite a data para o agendamento (DD/MM/AAAA): ", bg="#5ce1e6", fg="white", font=("Arial",12))
introducao_data.grid(row=9, column=0, sticky="ew")

entrada_data = Entry(frame_principal)
entrada_data.grid(row=10, column=0 )

introducao_horas = Label(frame_principal, text="Digite as horas do atendimento: ", bg="#5ce1e6", fg="white", font=("Arial",12))
introducao_horas.grid(row=11, column=0, sticky="ew")

entrada_horas = Entry(frame_principal)
entrada_horas.grid(row=12, column=0 )

introducao_minutos = Label(frame_principal, text="Digite os minutos do atendimento: ", bg="#5ce1e6", fg="white", font=("Arial",12))
introducao_minutos.grid(row=13, column=0, sticky="ew")

entrada_minutos = Entry(frame_principal)
entrada_minutos.grid(row=14, column=0 )

botao_data = Button(frame_principal, text="Validar", font=("Arial",12, "bold"), command=validar_data)
botao_data.grid(row=15, column=0 ,ipadx=12 ,ipady=5, pady=5)

resposta = Label(frame_principal, text=" ", bg="#5ce1e6", fg="white")
resposta.grid(row=16, column=0, sticky="ew")

lista = Listbox(frame_secundario)
lista.grid(row=18, column=0, ipadx=150, ipady=30)
scrollbar.config(command=lista.yview)
janela.grid_columnconfigure(0, weight=1)

janela.mainloop()
