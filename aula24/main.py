from tkinter import *
import divide

def main():
    janela = Tk()
    Button(text='Dividir números: ', command=divide.divide_numeros).grid()

    janela.mainloop()

if __name__ == '__main__':
    main()