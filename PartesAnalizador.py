from tkinter.constants import ANCHOR
import Menu as Menu
import pathlib
import shutil
import os
import math

class Token:
    def __init__(self, token = None, lexema = None, expresion = None, fila = None, columna = None):
        self.token = token
        self.lexema = lexema
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def str(self):
        print(f"Token: {self.token}, Lex: {self.lexema}, Exp: {self.expresion}, F:{self.fila}, C: {self.columna}")

class ErrorLexico:
    def __init__(self, caracter = None, fila = None, columna = None):
        self.caracter = caracter
        self.fila = fila
        self.columna = columna 

    def str(self):
        print(f"ERROR cter: {self.caracter}, F: {self.fila}, C: {self.columna}")

class Imagen:
    def __init__(self, titulo = None, ancho = None, alto = None, filas = None, columnas = None, celdas = None, filtros = None ):
        self.titulo = titulo
        self.ancho = ancho
        self.alto = alto
        self.filas = filas
        self.columnas = columnas
        self.celdas = celdas
        self.filtros = filtros

    def Css_Imagen_Original(self, imagen):
        
        pass

    def generar_Css_Imagen(self):
        for imagen in Menu.listadoImagenes:
            #Se guarda los archivos CSS en una determinada dirección.
            f = open(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{imagen.titulo}.css','w', encoding='utf-8')
            
            #Parte de generación del cuerpo de los archivos CSS
            withPixel = math.floor(int(imagen.ancho)/int(imagen.columnas))
            heightPixel = math.floor(int(imagen.alto)/int(imagen.filas))
            cuerpo = '''body {
                background: #ffffff;      /* Background color de toda la página */
                height: 100vh;            
                display: flex;            /* Define contenedor flexible */
                justify-content: center;  /* Centra horizontalmente el lienzo */
                align-items: center;      /* Centra verticalmente el lienzo */
                }

                .canvas {
                width: '''

            cuerpo += f'''{int(imagen.ancho)}''' 
            cuerpo += '''px;   /* Ancho del lienzo, se asocia al ANCHO de la entrada */
                height:'''
            cuerpo += f'''{int(imagen.alto)}'''
            cuerpo += '''px;  /* Alto del lienzo, se asocia al ALTO de la entrada */
                }

                .pixel {
                width: '''
            cuerpo += f'''{withPixel}'''
            cuerpo += '''px;    /* Ancho de cada pixel, se obtiene al operar ANCHO/COLUMNAS (al hablar de pixeles el resultado de la división debe ser un numero entero) */
                height: '''
            cuerpo += f'''{heightPixel}'''
            cuerpo += '''px;   /* Alto de cada pixel, se obtiene al operar ALTO/FILAS (al hablar de pixeles el resultado de la división debe ser un numero entero) */
                float: left;
                box-shadow: 0px 0px 1px rgb(24, 23, 23); /*Si lo comentan les quita la cuadricula de fondo */
                }'''

            #Parte del llenado de celdas
            for celda in imagen.celdas:
                if celda[2] == "FALSE":
                    pass
                else:
                    cuerpo += '''.pixel:nth-child('''
                    cuerpo += f'''{self.determinar_Celda(int(imagen.filas), int(imagen.columnas), int(celda[1]) + 1, int(celda[0]) + 1)}'''
                    cuerpo += '''){
                                    background:'''
                    cuerpo += f'''{celda[3]}'''
                    cuerpo += '''; /* Todo lo que este agrupado separado por comas antes de esta parte { background:..... } se le va a asignar el color indicado*/
                                    }'''
            f.write(cuerpo)
            f.close
            print(f"Css generado de {imagen.titulo}")

    def generar_Html_Imagen(self):
        for imagen in Menu.listadoImagenes:
            f = open(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{imagen.titulo}.html','w', encoding='utf-8')
            
            cuerpo = f'''<!DOCTYPE html>
                    <html>
                    <head>
                    <!-- Referencias a hojas de estilos, en este caso un CSS -->
                    <link rel="stylesheet" href="{imagen.titulo}.css">
                    </head>
                    <body>

                    <!-- div que representa el lienzo -->
                    <div class="canvas">
                    <!-- div que representan cada pixel, su numeración empieza desde 1 en adelante y se debe linealizar la matriz recorriendo por filas -->
                    <!-- En este caso son 16px x 16px = 256 pixeles -->'''

            for i in range(1, int(imagen.filas)+1):
                for j in range(1, int(imagen.columnas)+1):
                    cuerpo += '''<div class="pixel"></div> '''

            cuerpo += '''</div>
 
                        </body>
                        </html>'''
            f.write(cuerpo)
            f.close()
            print(f"Html generado de {imagen.titulo}")

    # print(self.determinar_Celda(int(imagen.filas), int(imagen.columnas), int(celda[1]) + 1, int(celda[0]) + 1))
    def determinar_Celda(self, filasImagen, columnasImagen, filaActual, columnaActual):
        contadorCeldas = 0
        for i in range(1, filasImagen+1):
            for j in range(1, columnasImagen+1):
                contadorCeldas+=1
                if (filaActual == i) and (columnaActual == j):
                    return contadorCeldas
                
    #Función para generar css y html de imagenes en una carpeta /Imagenes.
    def generar_Archivos(self):
        #Verificacmos si existe el Directorio/Folder
        if not os.path.exists(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes'):
            #Si no existe solo lo creamos
            os.makedirs(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes')
            self.generar_Css_Imagen()
            self.generar_Html_Imagen()
        else:
            #Si existe pues borrarlo y volver a crear uno nuevo
            shutil.rmtree(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes')
            os.makedirs(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes')
            self.generar_Css_Imagen()
            self.generar_Html_Imagen()