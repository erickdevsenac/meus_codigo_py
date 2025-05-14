from tkinter import *
import modu
import nome

def main():
    janela = Tk()
    lb = Label(text='teste').grid()
    btn = Button(text='dialog', command=modu.abrir_dialog)
    btn.grid()
    janela.mainloop()
    
    a = nome.imprime_nome('Erickson')
    ano_resultado = nome.calcula_ano_nascimento(35)
    print(ano_resultado)
   

if __name__ == "__main__":
    main()