import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.geometry('900x600+10+10')

frame1 = tk.Frame(janela, background='yellow')
frame1.grid(column=0, row=0)
frame2 = tk.Frame(frame1, background='green')
frame2.grid(column=0, row=1, padx=150, pady=150)
frame3 = tk.Frame(frame2, background='blue')
frame3.grid(column=0, row=2, padx=150, pady=150)

style = ttk.Style()
style.theme_use('alt')  # Temas disponíveis: 'clam', 'alt', 'default', 'classic'
style.configure('TLabel', foreground='white', background='#000', font=('Helvetica', 10))


ttk.Button(frame3, text="ENTRAR").grid(row=2, column=1, columnspan=2, padx=100, pady=100)


janela.mainloop()


# import tkinter as tk

# root = tk.Tk()
# canvas = tk.Canvas(root, width=500, height=400, bg='white')
# canvas.pack()

# canvas.create_rectangle(50, 50, 150, 100, fill='blue')
# canvas.create_oval(200, 50, 300, 100, fill='green')
# canvas.create_line(50, 150, 300, 150, fill='red', width=3)
# root.mainloop()





