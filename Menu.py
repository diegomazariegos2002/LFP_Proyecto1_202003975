from tkinter import Tk
from tkinter import Menu
from tkinter import filedialog
from typing import Text
from PartesAnalizador import Token, ErrorLexico, Imagen
from tkinter import messagebox
from tkinter import ttk
from tkinter import Button, Label, messagebox
import webbrowser
import imgkit
from PIL import ImageTk, Image
import pathlib


#=================================================Variables globales=================================================
listaTokens = []
listaErrores = []
listadoImagenes = []

estadoError = False

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

#====================================Funciones para el analisis del archivo==========================================
def isLetraMayusculas(caracter):
    cter = ord(caracter)
    if((cter >= 65 and cter <= 90) or (cter ==165)):
        return True
    else:
        return False

def isNumero(caracter):
    cter = ord(caracter)
    if(cter >= 48 and cter <= 57):
        return True
    else:
        return False

def analizarArchivo(entrada):
    global listaTokens
    global listaErrores
    global estadoError
    global listadoImagenes


    listaTokens = []
    listaErrores = []
    listadoImagenes = []
    estadoError = False
    fila = 1
    columna = 0 
    estado = 0
    lexActual = ""
    #IDEA
    titulo = ""
    ancho_Alto_Filas_Columnas = []
    celda = []
    celdas = []
    filtros = []


    #For inicial para ver caracter por caracter
    for c in entrada:
        cter = ord(c)
        # T - "" - A - F - C - # - M - D - @
        if estado == 0:
            if cter == 84:
                lexActual += c
                estado = 1
            elif cter == 44 or cter == 93 or cter == 91 or cter == 125 or cter == 123 or cter == 59 or cter == 61:
                lexActual += c
                estado = 2
            elif (isNumero(c) == True):
                lexActual += c
                estado = 80
                pass
            elif cter == 34:
                lexActual += c
                estado = 3
            #A
            elif cter == 65:
                lexActual += c
                estado = 4
            elif cter == 70:
                lexActual += c
                estado = 5
            elif cter == 67:
                lexActual += c
                estado = 6
            elif cter == 35:
                lexActual += c
                estado = 7
            elif cter == 77:
                lexActual += c
                estado = 8
            elif cter == 68:
                lexActual += c
                estado = 9
            elif cter == 64:
                lexActual += c
                estado = 10
            #~
            elif cter == 126:
                lexActual += c
                estado = 2
            else:
                # Espacio - Salto de línea - TAB
                if cter == 32 or cter == 10 or cter == 9:
                    lexActual = ""
                    estado = 0
                
                else:
                    #Crear error léxico
                    #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                    errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                    listaErrores.append(errorLexico)
                    estadoError = True
                lexActual = ""
                estado = 0
        # I - R 
        elif estado == 1:
            if cter == 73:
                lexActual += c
                estado = 11
            elif cter == 82:
                lexActual += c
                estado = 12
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #T
        elif estado == 11:
            if cter == 84:
                lexActual += c
                estado = 22
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #U
        elif estado == 22:
            if cter == 85:
                lexActual += c
                estado = 32
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #L
        elif estado == 32:
            if cter == 76:
                lexActual += c
                estado = 41
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #O   -> TITULO
        elif estado == 41:
            if cter == 79:
                lexActual += c
                estado = 2
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #U
        elif estado == 12:
            if cter == 85:
                lexActual += c
                estado = 23
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #E   -> TRUE
        elif estado == 23: 
            if cter == 69:
                lexActual += c
                estado = 2
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #palabra   -> "palabra"
        elif estado == 3:
            if cter >= 32 and cter <= 253 and cter != 34:
                lexActual += c
                estado = 3
            elif cter == 34:
                lexActual += c
                estado = 2
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #"
        elif estado == 13:
            estado = 2

        #N - L
        elif estado == 4:
            #N
            if cter == 78:
                lexActual += c
                estado = 14
            #L
            elif cter == 76:
                lexActual += c
                estado = 65
            else: 
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #C
        elif estado == 14:
            if cter == 67:
                lexActual += c
                estado = 24
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #H
        elif estado == 24:
            if cter == 72:
                lexActual += c
                estado = 33
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #O  ->  ANCHO
        elif estado == 33:
            if cter == 79:
                lexActual += c
                estado = 2
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #T
        elif estado == 65:
            if cter == 84:
                lexActual += c
                estado = 66
            else: 
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #O
        elif estado == 66:
            if cter == 79:
                lexActual += c
                estado = 2
            else: 
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #I - A
        elif estado == 5:
            #I
            if cter == 73:
                lexActual += c
                estado = 15
            #A
            elif cter == 65:
                lexActual += c
                estado = 16
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        # L
        elif estado == 15:
            if cter == 76:
                lexActual += c
                estado = 25
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        # A - T
        elif estado == 25:
            #A
            if cter == 65:
                lexActual += c
                estado = 34
            #T
            elif cter == 84:
                lexActual += c
                estado = 35
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #S   ->  FILAS
        elif estado == 34:
            if cter == 83:
                lexActual += c
                estado = 2
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #R
        elif estado == 35:
            if cter == 82:
                lexActual += c
                estado = 42
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #O
        elif estado == 42:
            if cter == 79:
                lexActual += c
                estado = 47
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #S  -> FILTROS
        elif estado == 47:
            if cter == 83:
                lexActual += c
                estado = 2
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #L
        elif estado == 16:
            if cter == 76:
                lexActual += c
                estado = 26
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #S
        elif estado == 26:
            if cter == 83:
                lexActual += c
                estado = 36
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #E -> FALSE
        elif estado == 36:
            if cter == 69:
                lexActual += c
                estado = 2
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #O -E
        elif estado == 6:
            #O
            if cter == 79:
                lexActual += c
                estado = 17
            #E
            elif cter == 69:
                lexActual += c
                estado = 18
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #L
        elif estado == 17:
            if cter == 76:
                lexActual += c
                estado = 27
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #U
        elif estado == 27:
            if cter == 85:
                lexActual += c
                estado = 37
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #M
        elif estado == 37:
            if cter == 77:
                lexActual += c
                estado = 43
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #N
        elif estado == 43:
            if cter == 78:
                lexActual += c
                estado = 48
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #A
        elif estado == 48:
            if cter == 65:
                lexActual+=c
                estado = 51
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #S -> COLUMNAS
        elif estado == 51:
            if cter == 83:
                lexActual += c
                estado = 2
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #L
        elif estado == 18:
            if cter == 76:
                lexActual += c
                estado = 28
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #D
        elif estado == 28:
            if cter == 68:
                lexActual += c
                estado = 38
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #A
        elif estado == 38:
            if cter == 65:
                lexActual += c
                estado = 44
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #S  -> CELDAS
        elif estado == 44:
            if cter == 83:
                lexActual += c
                estado = 2
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #LE - DI
        elif estado == 7: 
            # Letra o digito
            if (isLetraMayusculas(c) == True) or (isNumero(c) == True):
                lexActual += c
                estado = 57
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #LE - DI
        elif estado == 57: 
            # Letra o digito
            if (isLetraMayusculas(c) == True) or (isNumero(c) == True):
                lexActual += c
                estado = 58
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #LE - DI
        elif estado == 58: 
            # Letra o digito
            if (isLetraMayusculas(c) == True) or (isNumero(c) == True):
                lexActual += c
                estado = 59
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #LE - DI
        elif estado == 59: 
            # Letra o digito
            if (isLetraMayusculas(c) == True) or (isNumero(c) == True):
                lexActual += c
                estado = 60
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #LE - DI
        elif estado == 60: 
            # Letra o digito
            if (isLetraMayusculas(c) == True) or (isNumero(c) == True):
                lexActual += c
                estado = 61
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #LE - DI -> #000000
        elif estado == 61: 
            # Letra o digito
            if (isLetraMayusculas(c) == True) or (isNumero(c) == True):
                lexActual += c
                estado = 2
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #I
        elif estado == 8:
            if cter == 73:
                lexActual += c
                estado = 19
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #R
        elif estado == 19:
            if cter == 82:
                lexActual += c
                estado = 29
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #R
        elif estado == 29:
            if cter == 82:
                lexActual += c
                estado = 39
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #O
        elif estado == 39:
            if cter == 79:
                lexActual += c
                estado = 45
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #R
        elif estado == 45:
            if cter == 82:
                lexActual += c
                estado = 49
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        # X - Y
        elif estado == 49: 
            if cter == 88:
                lexActual += c
                estado = 2
            elif cter == 89:
                lexActual += c
                estado = 2
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #O
        elif estado == 9:
            if cter == 79:
                lexActual += c
                estado = 20
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #U
        elif estado == 20:
            if cter == 85:
                lexActual += c
                estado = 30
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #B
        elif estado == 30:
            if cter == 66:
                lexActual += c
                estado = 40
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #L
        elif estado == 40:
            if cter == 76:
                lexActual += c
                estado = 46
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #E
        elif estado == 46:
            if cter == 69:
                lexActual += c
                estado = 50
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #M
        elif estado == 50:
            if cter == 77:
                lexActual += c
                estado = 52
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0
        
        #I
        elif estado == 52:
            if cter == 73:
                lexActual += c
                estado = 53
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #R
        elif estado == 53:
            if cter == 82:
                lexActual += c
                estado = 54
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #R
        elif estado == 54:
            if cter == 82:
                lexActual += c
                estado = 55
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #O
        elif estado == 55:
            if cter == 79:
                lexActual += c
                estado = 56
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #R
        elif estado == 56:
            if cter == 82:
                lexActual += c
                estado = 2
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0

        #@
        elif estado == 10:
            if cter == 64:
                lexActual += c
                estado = 21
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0 

        #@
        elif estado == 21:
            if cter == 64:
                lexActual += c
                estado = 31
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0 

        #@
        elif estado == 31:
            if cter == 64:
                lexActual += c
                estado = 2
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0 

        #Digito
        elif estado == 80:
            if isNumero(c) == True:
                lexActual += c
                estado = 80
            elif cter == 59 or cter == 44:
                lexActual += c
                estado = 2
            else:
                #print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                errorLexico = ErrorLexico(c,fila,(columna-(len(lexActual)-1)))
                listaErrores.append(errorLexico)
                estadoError = True
                lexActual = ""
                estado = 0 
            pass

        #Estado de aceptación
        if estado == 2:
            #Aquí se crearía el objeto token y se añadiría a lista de tokens
            # print(f"Se reconoció el token {lexActual} en la fila {fila} y la columna {(columna-(len(lexActual)-1))}")
            if lexActual == "TITULO":
                token = Token("TITULO", lexActual, "TITULO", fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

            elif lexActual == "=":
                token = Token("Asignación",lexActual,"=",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

            #"palabra"  -> titulo de la imagen
            elif ord(lexActual[0]) == 34:
                token = Token("Cadena",lexActual,f"Le = [A_Z, a_z] -> Palabra = Le+ -> {chr(34)}palabra{chr(34)}",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)
                if estadoError == False:
                    titulo += lexActual[1:-1]

            elif lexActual == "ANCHO":
                token = Token("ANCHO",lexActual,"ANCHO",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

            elif lexActual == "ALTO":
                token = Token("ALTO",lexActual,"ALTO",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

            # Digito;
            elif ord(lexActual[-1]) == 59 and isNumero(lexActual[0]) == True:
                token = Token("Entero",lexActual[0:-1],"Di = [0_9] -> Digito = Di+ -> Digito",fila, (columna-(len(lexActual[0:-1])-1)))
                listaTokens.append(token)
                token = Token("Punto y coma", lexActual[-1], ";", fila, (columna-(len(lexActual[-1])-1)))
                listaTokens.append(token)

                if estadoError == False:
                    ancho_Alto_Filas_Columnas.append(lexActual[0:-1])
            # ;
            elif lexActual == ";":
                token = Token("Punto y coma", lexActual, ";", fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

            elif lexActual == "FILAS":
                token = Token("FILAS",lexActual,"FILAS",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

            elif lexActual == "COLUMNAS":
                token = Token("COLUMNAS",lexActual,"COLUMNAS",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

            elif lexActual == "CELDAS":
                token = Token("CELDAS",lexActual,"CELDAS",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

            elif lexActual == "{":
                token = Token("Llave abre",lexActual,"{",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

            elif lexActual == "}":
                token = Token("Llave cierra",lexActual,"}",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

            elif lexActual == "[":
                token = Token("Corchete abre",lexActual,"[",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

            elif lexActual == "]":
                token = Token("Corchete cierra",lexActual,"]",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

                if estadoError == False:
                    celdas.append(celda)
                    celda = []
            
            # Digito,
            elif ord(lexActual[-1]) == 44 and isNumero(lexActual[0]) == True:
                token = Token("Entero",lexActual[0:-1],"Di = [0_9] -> Digito = Di+ -> Digito",fila, (columna-(len(lexActual[0:-1])-1)))
                listaTokens.append(token)
                token = Token("Coma", lexActual[-1], ",", fila, (columna-(len(lexActual[-1])-1)))
                listaTokens.append(token)

                if estadoError == False:
                    celda.append(lexActual[0:-1])
            # ,
            elif lexActual == ",":
                token = Token("Coma", lexActual, ",", fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

            elif lexActual == "FALSE":
                token = Token("Booleano",lexActual,"FALSE",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

                if estadoError == False:
                    celda.append(lexActual)

            elif lexActual == "TRUE":
                token = Token("Booleano",lexActual,"TRUE",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

                if estadoError == False:
                    celda.append(lexActual)

            elif ord(lexActual[0]) == 35:
                token = Token("Código de color",lexActual,"Le = [A_Z] -> Di = [0_9] -> (#(Di|Le){6}) ",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

                if estadoError == False:
                    celda.append(lexActual)

            elif lexActual == "FILTROS":
                token = Token("FILTROS",lexActual,"FILTROS",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

            elif lexActual == "MIRRORX":
                token = Token("MIRROX",lexActual,"MIRROX",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

                if estadoError == False:
                    filtros.append(lexActual)

            elif lexActual == "MIRRORY":
                token = Token("MIRROY",lexActual,"MIRROY",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

                if estadoError == False:
                    filtros.append(lexActual)

            elif lexActual == "DOUBLEMIRROR":
                token = Token("DOUBLEMIRROR",lexActual,"DOUBLEMIRROR",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)

                if estadoError == False:
                    filtros.append(lexActual)

            elif lexActual == "@@@@":
                token = Token("Separador imágenes",lexActual,"@@@@",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)
                
                #Reiniciar a una nueva imagen
                if estadoError == False:
                    imagen = Imagen(titulo,ancho_Alto_Filas_Columnas[0],ancho_Alto_Filas_Columnas[1],
                    ancho_Alto_Filas_Columnas[2],ancho_Alto_Filas_Columnas[3], celdas, filtros)
                    listadoImagenes.append(imagen)
                    # print(titulo)
                    titulo = ""
                    # print(ancho_Alto_Filas_Columnas)
                    ancho_Alto_Filas_Columnas = []
                    # print(celdas)
                    celdas = []
                    # print(filtros)
                    filtros = []
            
            elif lexActual == "~":
                if estadoError == False:
                    
                    imagen = Imagen(titulo,ancho_Alto_Filas_Columnas[0],ancho_Alto_Filas_Columnas[1],
                    ancho_Alto_Filas_Columnas[2],ancho_Alto_Filas_Columnas[3], celdas, filtros)
                    listadoImagenes.append(imagen)
                    # print(titulo)
                    titulo = ""
                    # print(ancho_Alto_Filas_Columnas)
                    ancho_Alto_Filas_Columnas = []
                    # print(celdas)
                    celdas = []
                    # print(filtros)
                    filtros = []
            
            lexActual = ""
            estado = 0

        #Control de espacios, saltos de línea y Tab's
        if cter == 10:
            columna = 0
            fila += 1
        elif cter == 9:
            columna += 4
        elif cter == 32:
            columna += 1

        columna += 1

class MenuVentana:
    def __init__(self):
        self.txt = None
        self.ventana = Tk()
        self.ventana.title('Menu principal')
        self.ventana.geometry("700x400")
        self.ventana.configure(bg = 'antique white')
        
        # Por medio de esto accedo a lo que sucede al dar click sobre la X para cerrar la ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.on_closing)

        #Se crea el menú de la ventana / el tearoff = 0 es para que no se me cree un submenú al darle click al "----" que me sale en los cascade
        self.miMenu = Menu(self.ventana, tearoff=0)
        self.ventana.configure(menu=self.miMenu)
        
        #Creando una sección/SubMenú esta es la barrita que aparecere arriba en la ventana
        self.menuPrincipal = Menu(self.miMenu)
        self.miMenu.add_command(label="Cargar Archivo", command=self.cargar)
        self.miMenu.add_command(label="Analizar", command=self.analizar)
        self.miMenu.add_command(label="Reportes", command=self.generarReportes)
        self.miMenu.add_command(label="Salir", command=self.on_closing)
        
        #ComboBox
        listadoNombreImagenes = []
        self.myComboBox = ttk.Combobox(self.ventana, state= "readonly", value = listadoNombreImagenes)
        self.myComboBox.bind("<<ComboboxSelected>>", self.comboClick)
        self.myComboBox.place(x=10, y = 10)
        
        #Botones
        self.buttonOriginal = Button(self.ventana, text = "Imagen original", command = self.mostrarOriginal)
        self.buttonOriginal.place(x = 10, y = 100)
        
        self.buttonMirrorX = Button(self.ventana, text = "Filtro Mirror X", command = self.mostrarMirrorX)
        self.buttonMirrorX.place(x = 10, y = 150)
        
        self.buttonMirrorY = Button(self.ventana, text = "Filtro Mirror Y", command = self.mostrarMirrorY)
        self.buttonMirrorY.place(x = 10, y = 200)

        self.buttonDoubleMirror = Button(self.ventana, text = "Filtro DoubleMirror", command = self.mostrarDoubleMirror)
        self.buttonDoubleMirror.place(x = 10, y = 250)

        #Label que manejara las imagenes
        # x = f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/Pokeball.jpg'
        # print(x)
        # img = Image.open(x)
        # img = img.resize((250, 250), Image.ANTIALIAS)
        # img = ImageTk.PhotoImage(img)
        # self.labelImagen = Label(self.ventana, image = img)
        # self.labelImagen.place(x = 200, y = 100)
        
        
        self.ventana.mainloop()

    #====================================Metodos para mostrar las imagenes======================================

    def mostrarOriginal(self):
        try:
            nombreImagen = self.myComboBox.get()
            img = Image.open(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{nombreImagen}.jpg')
            new_img = img.resize((300, 256))
            render = ImageTk.PhotoImage(new_img)
            img1 = Label(self.ventana, image=render)
            img1.image = render
            img1.place(x=200, y = 100)
        except:
            messagebox.showwarning('ADVERTENCIA', 'La opcion actual no ha sido generada.')

    def mostrarMirrorX(self):
        try:
            nombreImagen = self.myComboBox.get()
            img = Image.open(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{nombreImagen}_MirrorX.jpg')
            new_img = img.resize((300, 256))
            render = ImageTk.PhotoImage(new_img)
            img1 = Label(self.ventana, image=render)
            img1.image = render
            img1.place(x=200, y = 100)
        except:
            messagebox.showwarning('ADVERTENCIA', 'El filtro solicitado no existe. Revisar archivo de entrada.')

    def mostrarMirrorY(self):
        try:
            nombreImagen = self.myComboBox.get()
            img = Image.open(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{nombreImagen}_MirrorY.jpg')
            new_img = img.resize((300, 256))
            render = ImageTk.PhotoImage(new_img)
            img1 = Label(self.ventana, image=render)
            img1.image = render
            img1.place(x=200, y = 100)
        except:
            messagebox.showwarning('ADVERTENCIA', 'El filtro solicitado no existe. Revisar archivo de entrada.')

    def mostrarDoubleMirror(self):
        try:
            nombreImagen = self.myComboBox.get()
            img = Image.open(f'{pathlib.Path(__file__).parent.absolute()}/Imagenes/{nombreImagen}_DoubleMirror.jpg')
            new_img = img.resize((300, 256))
            render = ImageTk.PhotoImage(new_img)
            img1 = Label(self.ventana, image=render)
            img1.image = render
            img1.place(x=200, y = 100)
        except:
            messagebox.showwarning('ADVERTENCIA', 'El filtro solicitado no existe. Revisar archivo de entrada.')
    
    
    #===============================Metodos para el funcionamiento básico de la app=======================

    def cargar(self):
        self.txt = abrirArchivo()
        self.txt += "~"
        
    def analizar(self):
        #Si el cargado se hizo correctamente
        if(self.txt != None):
            #Se realiza el proceso de lectura del archivo (analisis)
            analizarArchivo(self.txt)
            #Creando listado de nombres de la imagen.
            listadoNombreImagenes = []
            for i in listadoImagenes:
                listadoNombreImagenes.append(i.titulo)
            #Se agregan los nuevos titulos de imagenes al menu.
            self.myComboBox["value"] = listadoNombreImagenes
            #Se muestra el combo con la posicion 0 de primero.
            self.myComboBox.current(0) 
            #Se generan los archivos de la imagen
            imagenBase = Imagen()
            imagenBase.generar_Archivos()

        else:
            print("No se ha cargado ningun archivo")

    #se manda a llamar cuando se selecciona un item del combo.
    def comboClick(self, event):
        self.mostrarOriginal()
        
    def generarReportes(self):
        if(self.txt != None):
            #abrir o crear el reporte
            f = open('ReporteTokens.html','w', encoding='utf-8')
            #Cuerpo del documento
            cuerpo = '''<!doctype html>
            <html lang="en">

            <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
                integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

            <title>Reporte de Tokens</title>
            </head>

            <body style="background-color: lightseagreen;">
            <div class="container-fluid container p-3 my-3 bg-dark text-white">
                <div class="row">
                <div class="col-12" style="text-align: center; ">
                    <h1>REPORTE DE TOKENS</h1>
                </div>
                </div>
            </div>
            <div class="container-fluid" style="background-color: rgb(255, 255, 255); ">
                
                <div class="row justify-content-md-center">
                <div class="col-md-auto">
                    <h2 style="text-decoration: underline tomato;">Tabla de tokens</h2>
                </div>
                </div>
                <div class="row justify-content-md-center">
                <div class="col-md-auto">
                    <table class="table table-bordered table-striped text-center table-hover table-responsive"
                    style="text-align: center; width: 600px;">
                    <thead>
                        <tr class="table-dark">
                        <th>Token</th>
                        <th>Lexema</th>
                        <th>Patrón</th>
                        <th>Fila</th>
                        <th>Columna</th>
                        </tr>
                    </thead>
                    <tbody>
                    '''  
            for i in listaTokens:
                cuerpo += f'''
                            <tr>
                            <td class="table-success">{i.token}</td>
                            <td class="table-success">{i.lexema}</td>
                            <td class="table-success">{i.expresion}</td>
                            <td class="table-success">{i.fila}</td>
                            <td class="table-success">{i.columna}</td>
                            </tr>
                            '''
    
    
            cuerpo += '''
                </tbody>
                </table>
                </div>
                </div>
                <div class="container-fluid container p-3 my-3 bg-dark text-white">
                <div class="row">
                <div class="col-12" style="text-align: center; ">
                    <h1></h1>
                </div>
                </div>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
                crossorigin="anonymous"></script>
            </body>

            </html>'''

            f.write(cuerpo)
            f.close
            #Aquí se hace la magia de abrirlo automaticamente
            webbrowser.open_new_tab('ReporteTokens.html')
            f = open('ReporteErrores.html','w',encoding='utf-8')
            
            #Cuerpo del documento
            cuerpo = '''<!doctype html>
            <html lang="en">

            <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
                integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

            <title>Reporte de Tokens</title>
            </head>

            <body style="background-color: lightseagreen;">
            <div class="container-fluid container p-3 my-3 bg-dark text-white">
                <div class="row">
                <div class="col-12" style="text-align: center; ">
                    <h1>REPORTE DE ERRORES</h1>
                </div>
                </div>
            </div>
            <div class="container-fluid" style="background-color: rgb(255, 255, 255); ">
                
                <div class="row justify-content-md-center">
                <div class="col-md-auto">
                    <h2 style="text-decoration: underline tomato;">Tabla de errores léxicos</h2>
                </div>
                </div>
                <div class="row justify-content-md-center">
                <div class="col-md-auto">
                    <table class="table table-bordered table-striped text-center table-hover table-responsive"
                    style="text-align: center; width: 600px;">
                    <thead>
                        <tr class="table-dark">
                        <th>Caracter</th>
                        <th>Fila</th>
                        <th>Columna</th>
                        </tr>
                    </thead>
                    <tbody>
                    '''  
            for i in listaErrores:
                cuerpo += f'''
                            <tr>
                            <td class="table-success">{i.caracter}</td>
                            <td class="table-success">{i.fila}</td>
                            <td class="table-success">{i.columna}</td>
                            </tr>
                            '''
    
    
            cuerpo += '''
                </tbody>
                </table>
                </div>
                </div>
                <div class="container-fluid container p-3 my-3 bg-dark text-white">
                <div class="row">
                <div class="col-12" style="text-align: center; ">
                    <h1></h1>
                </div>
                </div>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
                crossorigin="anonymous"></script>
            </body>

            </html>'''

            f.write(cuerpo)
            f.close
            webbrowser.open_new_tab('ReporteErrores.html')
            
        else:
            print("No se ha cargado ningun archivo")
              
    # Metodo para cerrar la ventana 
    def on_closing(self):
        if messagebox.askokcancel("Cerrar Programa", "Seguro que desea Salir?"):
            self.ventana.quit()

