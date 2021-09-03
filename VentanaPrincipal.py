from tkinter import *
from tkinter import ttk

class VentanaPrincipal:
    def __init__(self):
        raiz = Tk()
        raiz.geometry('300x200')
        raiz.configure(bg = 'beige')    
        raiz.title('Aplicación')
        ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)
        raiz.mainloop()