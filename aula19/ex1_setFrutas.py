from tkinter import *

janela = Tk()
janela.geometry('300x200')
frame = Frame(janela, background='black', width=150)
frame.grid(row=0, column=0)

set_frutas = {'ameixa', 'goiaba', 'pera', 'jamelão', 'jaca'}
Label(janela, text='frutas').grid(row=4, column=1,)
# scrollbar = Scrollbar()
# scrollbar.grid(row=0, column=1, sticky='ns')
# listbox_frutas = Listbox(yscrollcommand=scrollbar.set)

# def add_fruta():
#     fruta = entry_fruta.get()
#     if fruta:
#         set_frutas.add(fruta.lower())
#         listbox_frutas.delete(0, END)
#         for f in set_frutas:
#             listbox_frutas.insert(END, f.upper())
#         entry_fruta.delete(0, END)

# for fruta in set_frutas:
#     listbox_frutas.insert(END, fruta.upper())
    
# listbox_frutas.grid(row=0, column=0, sticky='nsew') 
# scrollbar.config(command=listbox_frutas.yview)

for i, f in enumerate(set_frutas):
    Label(frame, text=f).grid(row=i, column=0, padx=5, pady=2, sticky='w')

entry_fruta = Entry()
entry_fruta.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

# btn_add = Button(text='Adicionar Fruta', command=add_fruta)
# btn_add.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='ew') 

janela.grid_rowconfigure(0, weight=1)   # A linha do Listbox pode se expandir verticalmente
janela.grid_columnconfigure(0, weight=1) # A coluna do Listbox pode se expandir horizontalmente

janela.mainloop()