import tkinter as tk

def calcular_media():
    nome = entry_nome.get()
    try:
        notas = []
        for entry in notas_entries:
            if entry.get(): 
                notas.append(float(entry.get()))
        
        if len(notas) != 4:
            resultado_label.config(text="Erro: insira exatamente 4 notas.", fg="black")
            return
        
        
        media = sum(notas) / len(notas)


        media_necessaria = float(entry_media_necessaria.get())
        
        if media >= media_necessaria:
            status = "Aprovado"
            cor = "green"
        else:
            status = "Reprovado"
            cor = "red"
        
        resultado_label.config(text=f"{nome} - Média: {media} - Média necessária: {media_necessaria} - {status}", fg=cor)
    except ValueError:
        resultado_label.config(text="Erro: insira apenas números válidos nas notas.", fg="black")


janela = tk.Tk()
janela.title("Cálculo de Média de Alunos")
janela.geometry("400x500")
janela.config(bg="lightblue")

tk.Label(janela, text="Nome do Aluno:", bg="lightblue", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_nome = tk.Entry(janela, width=30)
entry_nome.grid(row=0, column=1)


notas_entries = []

tk.Label(janela, text="Nota 1:", bg="lightblue", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
nota_entry1 = tk.Entry(janela, width=30)
nota_entry1.grid(row=1, column=1)
notas_entries.append(nota_entry1)

tk.Label(janela, text="Nota 2:", bg="lightblue", font=("Arial", 10)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
nota_entry2 = tk.Entry(janela, width=30)
nota_entry2.grid(row=2, column=1)
notas_entries.append(nota_entry2)

tk.Label(janela, text="Nota 3:", bg="lightblue", font=("Arial", 10)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
nota_entry3 = tk.Entry(janela, width=30)
nota_entry3.grid(row=3, column=1)
notas_entries.append(nota_entry3)

tk.Label(janela, text="Nota 4:", bg="lightblue", font=("Arial", 10)).grid(row=4, column=0, padx=10, pady=5, sticky="e")
nota_entry4 = tk.Entry(janela, width=30)
nota_entry4.grid(row=4, column=1)
notas_entries.append(nota_entry4)

tk.Label(janela, text="Média necessária para aprovação:", bg="lightblue", font=("Arial", 10)).grid(row=5, column=0, padx=10, pady=5, sticky="e")
entry_media_necessaria = tk.Entry(janela, width=30)
entry_media_necessaria.grid(row=5, column=1)

botao = tk.Button(janela, text="Calcular Média", command=calcular_media, bg="lightgreen", font=("Arial", 12))
botao.grid(row=6, column=0, columnspan=2, pady=15)

resultado_label = tk.Label(janela, text="", font=("Arial", 12), bg="lightblue")
resultado_label.grid(row=7, column=0, columnspan=2)

janela.mainloop()