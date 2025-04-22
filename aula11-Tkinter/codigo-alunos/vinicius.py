import tkinter as tk

#declaração da lista

numero_lista = []

#funções

def adicionar():
    numero = entrada.get()
    numero_lista.append(int(numero))
    entrada.delete(0, tk.END)

def calculo():
    acumular = 0
    for i in range(len(numero_lista)):
        acumular = numero_lista[i] + acumular
    resultado = acumular / len(numero_lista)
    resultado_final.config(text=f"A media é: {resultado}")
    espacamento4 = tk.Label(text = " " ,bg= "black", fg="white")
    espacamento4.pack()
    mensagem = tk.Label(text = "OBRIGADO PELA ATENÇÃO" ,bg= "black", fg="white")
    mensagem.pack()
#parte estetica da janela

janela = tk.Tk()

janela.title('Calculo')
janela.config(background="black")

janela.geometry("900x600")

janela.maxsize(width=1200, height=900)

janela.minsize(width=400, height=200)

janela.resizable(True, True)

#parte da entrada e saida de dados

introducao = tk.Label(text = "Digite 5 numeros para o calculo da média: ", background="black",fg="white")
introducao.pack()

entrada = tk.Entry()
entrada.pack()

espacamento = tk.Label(text = " " ,bg= "black", fg="white")
espacamento.pack()

botao = tk.Button(text = "Adicionar" , command=adicionar )
botao.pack()

espacamento2 = tk.Label(text = " " ,bg= "black", fg="white")
espacamento2.pack()

botao_result = tk.Button(text = "Resultado" , command=calculo )
botao_result.pack()

espacamento3 = tk.Label(text = " " ,bg= "black", fg="white")
espacamento3.pack()

resultado_final = tk.Label(text = " " ,bg= "black", fg="white")
resultado_final.pack()
janela.mainloop()