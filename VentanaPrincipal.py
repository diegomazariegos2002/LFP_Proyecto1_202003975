from tkinter import *
from tkinter import ttk
from tkinter import filedialog, Tk
from tkinter import messagebox

#====================================Declarando función para abrir un archivo========================================
def abrirArchivo():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Seleccionar un archivo PXLA",
        initialdir = "./",
        filetypes= (
            ("archivos PXLA", "*.pxla"),
            ("todos los archivos", "*.*")
        )
    )
    if archivo is None:
        print('No se seleccionó ningun archivo\n')
        return None
    else:
        texto = archivo.read()
        archivo.close()
        print('Lectura exitosa\n')
        return texto

#====================================Clase de venta Principal del programa=============================================
class VentanaPrincipal:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('300x200')  # anchura x altura
        
        self.raiz.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Asigna un color de fondo a la ventana. Si se omite
        # esta línea el fondo será gris
        self.raiz.configure(bg = 'beige') 
        
        # Impide que los bordes puedan desplazarse para
        # ampliar o reducir el tamaño de la ventana 'self.raiz':
        self.raiz.resizable(width=False,height=False)   
        
        #Titulo de la ventana
        self.raiz.title('Aplicación')
        
        # Define el widget Text 'self.tinfo ' en el que se
        # pueden introducir varias líneas de texto:
        self.tinfo = Text(self.raiz, width=20, height=10 )

        # Sitúa la caja de texto 'self.tinfo' en la parte
        # superior de la ventana 'self.raiz':
        self.tinfo.pack(side=TOP)

        # Define el widget Button 'self.binfo' que llamará 
        # al metodo 'self.verinfo' cuando sea presionado
        self.binfo = ttk.Button(self.raiz, text='Info', command=self.verinfo)

        # Coloca el botón 'self.binfo' debajo y a la izquierda
        # del widget anterior     
        self.binfo.pack(side=LEFT)
        
        # Define el botón 'self.bsalir'. En este caso
        # cuando sea presionado, el método destruirá o
        # terminará la aplicación-ventana 'self.raíz' con 
        # 'self.raiz.destroy'
        self.bsalir = ttk.Button(self.raiz, text='Salir', command=quit)
                                 
        # Coloca el botón 'self.bsalir' a la derecha del 
        # objeto anterior.                
        self.bsalir.pack(side=RIGHT)
        
        # El foco de la aplicación se sitúa en el botón
        # 'self.binfo' resaltando su borde. Si se presiona
        # la barra espaciadora el botón que tiene el foco
        # será pulsado. El foco puede cambiar de un widget
        # a otro con la tecla tabulador [tab]
        self.binfo.focus_set()
        self.raiz.mainloop()

    def verinfo(self):
        
        # Borra el contenido que tenga en un momento dado
        # la caja de texto
        self.tinfo.delete("1.0", END)
        
        # Obtiene información de la ventana 'self.raiz':
        info1 = self.raiz.winfo_class()
        info2 = self.raiz.winfo_geometry()
        info3 = str(self.raiz.winfo_width())
        info4 = str(self.raiz.winfo_height())
        info5 = str(self.raiz.winfo_rootx())
        info6 = str(self.raiz.winfo_rooty())
        info7 = str(self.raiz.winfo_id())
        info8 = self.raiz.winfo_name()
        info9 = self.raiz.winfo_manager()
        # info10 = abrirArchivo()
        
        # Construye una cadena de texto con toda la
        # información obtenida:
        texto_info = "Clase de 'raiz': " + info1 + "\n"
        texto_info += "Resolución y posición: " + info2 + "\n"
        texto_info += "Anchura ventana: " + info3 + "\n"
        texto_info += "Altura ventana: " + info4 + "\n"
        texto_info += "Pos. Ventana X: " + info5 + "\n"
        texto_info += "Pos. Ventana Y: " + info6 + "\n"
        texto_info += "Id. de 'raiz': " + info7 + "\n"
        texto_info += "Nombre objeto: " + info8 + "\n" 
        texto_info += "Gestor ventanas: " + info9 + "\n"
        # texto_info =  info10
        
        # Inserta la información en la caja de texto:
        
        self.tinfo.insert("1.0", texto_info)
        
        # Inserta la información en la caja de texto:
        # self.tinfo.insert("1.0", texto_info)
        print("TEXTO DEL ARCHIVO")
        print(texto_info)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.raiz.quit()
    
    
if __name__ == "__main__":
    menu = VentanaPrincipal()