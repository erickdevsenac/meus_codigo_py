from tkinter import *
from datetime import datetime, timedelta, date
 
janela = Tk()
janela.geometry('900x600')
janela.title("Agendamento para Dentista")
janela.config(background= "black")
tarefa = ""
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
    dias_para_prazo_str = entrada_data.get()
    dias_para_prazo_int = int(dias_para_prazo_str)
    hoje = datetime.now()
    hoje_str = hoje.strftime('%d/%m/%Y')
    prazo = (hoje + timedelta(days=dias_para_prazo_int) + timedelta(hours=horas_para_prazo_int) + timedelta(minutes=minutos_para_prazo_int))
    lista.insert(END,f"Procedimento: {tarefa} agendada para {prazo.strftime('%d/%m/%Y %H:%M')}")
   
 
introducao_procedimento = Label(text="Digite uma das opções para saber qual sera procedimento que ira ser realizado: ")
introducao_procedimento.grid()
 
introducao_opcao1 = Label(text="1-Extração Dentária")
introducao_opcao1.grid()
 
introducao_opcao2 = Label(text="2-Limpeza dentaria")
introducao_opcao2.grid()
 
introducao_opcao3 = Label(text="3-Clareamento Dental")
introducao_opcao3.grid()
 
introducao_opcao4 = Label(text="4-Instalação do aparelho")
introducao_opcao4.grid()
 
introducao_opcao5 = Label(text="5-Manutenção do Aparelho")
introducao_opcao5.grid()
 
entrada_procedimento = Entry()
entrada_procedimento.grid()
 
botao_procedimento = Button(text="Confirmar", command=confirmar_procedimento)
botao_procedimento.grid()
 
introducao_data = Label(text="Digite a data para o agendamento: ")
introducao_data.grid()
 
entrada_data = Entry()
entrada_data.grid()
 
introducao_horas = Label(text="Digite as horas do atendimento: ")
introducao_horas.grid()
 
entrada_horas = Entry()
entrada_horas.grid()
 
introducao_minutos = Label(text="Digite os minutos do atendimento: ")
introducao_minutos.grid()
 
entrada_minutos = Entry()
entrada_minutos.grid()
 
botao_data = Button(text="Validar", command=validar_data)
botao_data.grid()
 
resposta = Label(text=" ")
resposta.grid()
 
lista = Listbox()
lista.grid(ipadx=150)
 
janela.mainloop()