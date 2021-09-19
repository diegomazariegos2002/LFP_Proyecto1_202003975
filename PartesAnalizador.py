from tkinter.constants import ANCHOR
import Menu as Menu
import pathlib
import shutil
import os
import math
import imgkit

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

    def Css_Imagen_MirrorX(self, imagen):
        #Se guarda los archivos CSS en una determinada dirección.
        f = open(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{imagen.titulo}_MirrorX.css','w', encoding='utf-8')
        
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
                cuerpo += f'''{self.determinar_Celda(int(imagen.filas), int(imagen.columnas), int(celda[1]) + 1,  (int(imagen.columnas) + 1) -  (int(celda[0]) + 1))}'''
                cuerpo += '''){
                                background:'''
                cuerpo += f'''{celda[3]}'''
                cuerpo += '''; /* Todo lo que este agrupado separado por comas antes de esta parte { background:..... } se le va a asignar el color indicado*/
                                }'''
        f.write(cuerpo)
        f.close
        print(f"Css generado de {imagen.titulo}_MirrorX")

    def Css_Imagen_MirrorY(self, imagen):
        #Se guarda los archivos CSS en una determinada dirección.
        f = open(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{imagen.titulo}_MirrorY.css','w', encoding='utf-8')
        
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
                cuerpo += f'''{self.determinar_Celda(int(imagen.filas), int(imagen.columnas), (int(imagen.filas) + 1) - (int(celda[1]) + 1), int(celda[0]) + 1)}'''
                cuerpo += '''){
                                background:'''
                cuerpo += f'''{celda[3]}'''
                cuerpo += '''; /* Todo lo que este agrupado separado por comas antes de esta parte { background:..... } se le va a asignar el color indicado*/
                                }'''
        f.write(cuerpo)
        f.close
        print(f"Css generado de {imagen.titulo}_MirrorY")

    def Css_Imagen_DoubleMirror(self, imagen):
        #Se guarda los archivos CSS en una determinada dirección.
        f = open(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{imagen.titulo}_DoubleMirror.css','w', encoding='utf-8')
        
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
                cuerpo += f'''{self.determinar_Celda(int(imagen.filas), int(imagen.columnas),(int(imagen.filas) +1)- (int(celda[1]) + 1), (int(imagen.columnas) + 1) -  (int(celda[0]) + 1))}'''
                cuerpo += '''){
                                background:'''
                cuerpo += f'''{celda[3]}'''
                cuerpo += '''; /* Todo lo que este agrupado separado por comas antes de esta parte { background:..... } se le va a asignar el color indicado*/
                                }'''
        f.write(cuerpo)
        f.close
        print(f"Css generado de {imagen.titulo}_DoubleMirror")

    #Genera los archivos CSS de cada imagen dependiendo tambien de que filtros se solicitaron aunque
    #siempre crea el archivo de la imagen original.
    def generar_Css_Imagen(self):
        for imagen in Menu.listadoImagenes:
            self.Css_Imagen_Original(imagen)
            
            if "MIRRORX" in imagen.filtros:
                self.Css_Imagen_MirrorX(imagen)
            if "MIRRORY" in imagen.filtros:
                self.Css_Imagen_MirrorY(imagen)
            if "DOUBLEMIRROR" in imagen.filtros:
                self.Css_Imagen_DoubleMirror(imagen)

    #Ademas de generar los archivos HTML se generan los archivos JPG de las imagenes Pasando el HTML a JPG
    # Con imgkit.
    def Html_Imagen_Original(self, imagen):
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

        #Generando archivo imagen
        options = {'enable-local-file-access': None, 'width': int(imagen.ancho), 'height': (int(imagen.alto) + 15)}
        css = f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{imagen.titulo}.css'

        imgkit.from_string(cuerpo,f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{imagen.titulo}.jpg',options=options, css = css)

    def Html_Imagen_MirrorX(self, imagen):
        f = open(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{imagen.titulo}_MirrorX.html','w', encoding='utf-8')
        
        cuerpo = f'''<!DOCTYPE html>
                <html>
                <head>
                <!-- Referencias a hojas de estilos, en este caso un CSS -->
                <link rel="stylesheet" href="{imagen.titulo}_MirrorX.css">
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
        print(f"Html generado de {imagen.titulo}_MirrorX")
        #Generando archivo imagen
        options = {'enable-local-file-access': None, 'width': int(imagen.ancho), 'height': (int(imagen.alto) + 15)}
        css = f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{imagen.titulo}_MirrorX.css'

        imgkit.from_string(cuerpo,f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{imagen.titulo}_MirrorX.jpg',options=options, css = css)

    def Html_Imagen_MirrorY(self, imagen):
        f = open(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{imagen.titulo}_MirrorY.html','w', encoding='utf-8')
        
        cuerpo = f'''<!DOCTYPE html>
                <html>
                <head>
                <!-- Referencias a hojas de estilos, en este caso un CSS -->
                <link rel="stylesheet" href="{imagen.titulo}_MirrorY.css">
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
        print(f"Html generado de {imagen.titulo}_MirrorY")
        #Generando archivo imagen
        options = {'enable-local-file-access': None, 'width': int(imagen.ancho), 'height': (int(imagen.alto) + 15)}
        css = f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{imagen.titulo}_MirrorY.css'

        imgkit.from_string(cuerpo,f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{imagen.titulo}_MirrorY.jpg',options=options, css = css)

    def Html_Imagen_DoubleMirror(self, imagen):
        f = open(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{imagen.titulo}_DoubleMirror.html','w', encoding='utf-8')
        
        cuerpo = f'''<!DOCTYPE html>
                <html>
                <head>
                <!-- Referencias a hojas de estilos, en este caso un CSS -->
                <link rel="stylesheet" href="{imagen.titulo}_DoubleMirror.css">
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
        print(f"Html generado de {imagen.titulo}_DoubleMirror")
        #Generando archivo imagen
        options = {'enable-local-file-access': None, 'width': int(imagen.ancho), 'height': (int(imagen.alto) + 15)}
        css = f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{imagen.titulo}_DoubleMirror.css'

        imgkit.from_string(cuerpo,f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{imagen.titulo}_DoubleMirror.jpg',options=options, css = css)

    #Genera los archivos HTML de cada imagen dependiendo tambien de que filtros se solicitaron aunque
    #siempre crea el archivo de la imagen original. Cabe recalcar que estos siempre se generan despues 
    #de los archivos CSS puesto que los archivos HTML extraen las propiedades definidas en los CSS.
    def generar_Html_Imagen(self):
        for imagen in Menu.listadoImagenes:
            self.Html_Imagen_Original(imagen)
            if "MIRRORX" in imagen.filtros:
                self.Html_Imagen_MirrorX(imagen)
            if "MIRRORY" in imagen.filtros:
                self.Html_Imagen_MirrorY(imagen)
            if "DOUBLEMIRROR" in imagen.filtros:
                self.Html_Imagen_DoubleMirror(imagen)

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