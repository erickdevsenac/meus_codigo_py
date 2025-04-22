#Importa as bibliotecas
from tkinter import *
from tkinter import font

#Cria uma instância do tkinter frame
win = Tk()
win.geometry("750x350")
win.title('Font List')

#Cria uma lista de fontes usando o construtor font-family
fonts=list(font.families())
fonts.sort()
def fill_frame(frame):
   for f in fonts:
      #Cria um label para exibir a fonte
      label = Label(frame,text=f,font=(f, 14)).pack()
def onFrameConfigure(canvas):
   canvas.configure(scrollregion=canvas.bbox("all"))

#Cria um canvas
canvas = Canvas(win,bd=1, background="white")

#Cria um frame dentro do canvas
frame = Frame(canvas, background="white")

#Adiciona um scrollbar
scroll_y = Scrollbar(win, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scroll_y.set)
scroll_y.pack(side="right", fill="y")
canvas.pack(side="left", expand=1, fill="both")
canvas.create_window((5,4), window=frame, anchor="n")
frame.bind("<Configure>", lambda e, canvas=canvas: onFrameConfigure(canvas))
fill_frame(frame)

win.mainloop()
