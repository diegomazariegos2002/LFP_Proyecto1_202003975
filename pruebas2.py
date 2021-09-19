import tkinter as tk
from tkinter.ttk import Label
from PIL import ImageTk, Image
import pathlib

ventana = tk.Tk()
ventana.title("prueba")
ventana.geometry('400x400')

#Crear los comandos
def imagen():
    img = Image.open(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/Honguito.jpg')
    new_img = img.resize((300, 256))
    render = ImageTk.PhotoImage(new_img)
    img1 = Label(ventana, image=render)
    img1.image = render
    img1.place(x=10, y = 30)

def imagen2():
    img = Image.open(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/Pokeball.jpg')
    new_img = img.resize((300, 256))
    render = ImageTk.PhotoImage(new_img)
    img1 = Label(ventana, image=render)
    img1.image = render
    img1.place(x=10, y = 30)


#Botones
boton = tk.Button(ventana, command=imagen , text = "Abrir imagen", height=2, width=20)
boton.place(x=0,y=300)

boton1 = tk.Button(ventana,command=imagen2, text = "Imagen 2", height=2, width=20)
boton1.place(x=200,y=300)

ventana.mainloop()
    

