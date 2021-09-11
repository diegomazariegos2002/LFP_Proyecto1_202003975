from tkinter import filedialog, Tk
from tkinter import *
from tkinter import ttk
from VentanaPrincipal import VentanaPrincipal
from Menu import MenuVentana
from PartesAnalizador import Token, ErrorLexico, Imagen


listaTokens = []

def main():
    ventanaPrincipal = VentanaPrincipal()
    return

def menu():
    menuVentana = MenuVentana()
    return

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
    fila = 1
    columna = 0 
    estado = 0
    lexActual = ""

    #For inicial para ver caracter por caracter
    for c in entrada:
        cter = ord(c)
        # T - "" - A - F - C - # - M - D - @
        if estado == 0:
            if cter == 84:
                lexActual += c
                estado = 1
            elif (isNumero(c) == True) or cter == 44 or cter == 93 or cter == 91 or cter == 125 or cter == 123 or cter == 59 or cter == 61:
                lexActual += c
                estado = 2
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
            else:
                if cter == 32 or cter == 10 or cter == 9:
                    lexActual = ""
                    estado = 0
                else:
                    #Crear error léxico
                    print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
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
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #T
        elif estado == 11:
            if cter == 84:
                lexActual += c
                estado = 22
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #U
        elif estado == 22:
            if cter == 85:
                lexActual += c
                estado = 32
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #L
        elif estado == 32:
            if cter == 76:
                lexActual += c
                estado = 41
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #O   -> TITULO
        elif estado == 41:
            if cter == 79:
                lexActual += c
                estado = 2
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #U
        elif estado == 12:
            if cter == 85:
                lexActual += c
                estado = 23
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #E   -> TRUE
        elif estado == 23: 
            if cter == 69:
                lexActual += c
                estado = 2
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
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
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #"
        elif estado == 13:
            estado = 2

        #N
        elif estado == 4:
            #N
            if cter == 78:
                lexActual += c
                estado = 14
            else: 
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #C
        elif estado == 14:
            if cter == 67:
                lexActual += c
                estado = 24
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #H
        elif estado == 24:
            if cter == 72:
                lexActual += c
                estado = 33
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #O  ->  ANCHO
        elif estado == 33:
            if cter == 79:
                lexActual += c
                estado = 2
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
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
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        # L
        elif estado == 15:
            if cter == 76:
                lexActual += c
                estado = 25
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
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
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #S   ->  FILAS
        elif estado == 34:
            if cter == 83:
                lexActual += c
                estado = 2
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #R
        elif estado == 35:
            if cter == 82:
                lexActual += c
                estado = 42
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #O
        elif estado == 42:
            if cter == 79:
                lexActual += c
                estado = 47
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #S  -> FILTROS
        elif estado == 47:
            if cter == 83:
                lexActual += c
                estado = 2
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #L
        elif estado == 16:
            if cter == 76:
                lexActual += c
                estado = 26
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #S
        elif estado == 26:
            if cter == 83:
                lexActual += c
                estado = 36
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #E -> FALSE
        elif estado == 36:
            if cter == 69:
                lexActual += c
                estado = 2
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
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
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #L
        elif estado == 17:
            if cter == 76:
                lexActual += c
                estado = 27
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #U
        elif estado == 27:
            if cter == 85:
                lexActual += c
                estado = 37
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #M
        elif estado == 37:
            if cter == 77:
                lexActual += c
                estado = 43
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #N
        elif estado == 43:
            if cter == 79:
                lexActual += c
                estado = 48
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #A
        elif estado == 48:
            if cter == 65:
                lexActual+=c
                estado = 51
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #S -> COLUMNAS
        elif estado == 51:
            if cter == 83:
                lexActual += c
                estado = 2
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #L
        elif estado == 18:
            if cter == 76:
                lexActual += c
                estado = 28
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #D
        elif estado == 28:
            if cter == 68:
                lexActual += c
                estado = 38
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #A
        elif estado == 38:
            if cter == 65:
                lexActual += c
                estado = 44
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #S  -> CELDAS
        elif estado == 44:
            if cter == 83:
                lexActual += c
                estado = 2
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #LE - DI
        elif estado == 7: 
            # Letra o digito
            if (isLetraMayusculas(c) == True) or (isNumero(c) == True):
                lexActual += c
                estado = 57
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #LE - DI
        elif estado == 57: 
            # Letra o digito
            if (isLetraMayusculas(c) == True) or (isNumero(c) == True):
                lexActual += c
                estado = 58
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #LE - DI
        elif estado == 58: 
            # Letra o digito
            if (isLetraMayusculas(c) == True) or (isNumero(c) == True):
                lexActual += c
                estado = 59
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #LE - DI
        elif estado == 59: 
            # Letra o digito
            if (isLetraMayusculas(c) == True) or (isNumero(c) == True):
                lexActual += c
                estado = 60
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #LE - DI
        elif estado == 60: 
            # Letra o digito
            if (isLetraMayusculas(c) == True) or (isNumero(c) == True):
                lexActual += c
                estado = 61
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #LE - DI -> #000000
        elif estado == 61: 
            # Letra o digito
            if (isLetraMayusculas(c) == True) or (isNumero(c) == True):
                lexActual += c
                estado = 2
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #I
        elif estado == 8:
            if cter == 73:
                lexActual += c
                estado = 19
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #R
        elif estado == 19:
            if cter == 82:
                lexActual += c
                estado = 29
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #R
        elif estado == 29:
            if cter == 82:
                lexActual += c
                estado = 39
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #O
        elif estado == 39:
            if cter == 79:
                lexActual += c
                estado = 45
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #R
        elif estado == 45:
            if cter == 82:
                lexActual += c
                estado = 49
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
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
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #O
        elif estado == 9:
            if cter == 79:
                lexActual += c
                estado = 20
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #U
        elif estado == 20:
            if cter == 85:
                lexActual += c
                estado = 30
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #B
        elif estado == 30:
            if cter == 66:
                lexActual += c
                estado = 40
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #L
        elif estado == 40:
            if cter == 76:
                lexActual += c
                estado = 46
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #E
        elif estado == 46:
            if cter == 69:
                lexActual += c
                estado = 50
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #M
        elif estado == 50:
            if cter == 77:
                lexActual += c
                estado = 52
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0
        
        #I
        elif estado == 52:
            if cter == 73:
                lexActual += c
                estado = 53
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #R
        elif estado == 53:
            if cter == 82:
                lexActual += c
                estado = 54
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #R
        elif estado == 54:
            if cter == 82:
                lexActual += c
                estado = 55
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #O
        elif estado == 55:
            if cter == 79:
                lexActual += c
                estado = 56
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #R
        elif estado == 56:
            if cter == 82:
                lexActual += c
                estado = 2
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0

        #@
        elif estado == 10:
            if cter == 64:
                lexActual += c
                estado = 21
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0 

        #@
        elif estado == 21:
            if cter == 64:
                lexActual += c
                estado = 31
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0 

        #@
        elif estado == 31:
            if cter == 64:
                lexActual += c
                estado = 2
            else:
                print(f"Error léxico, caracter invalido {c} en la fila {fila} y columna {(columna-(len(lexActual)-1))}")
                lexActual = ""
                estado = 0 

        #Estado de aceptación
        if estado == 2:
            #Aquí se crearía el objeto token y se añadiría a lista de tokens
            print(f"Se reconoció el token {lexActual} en la fila {fila} y la columna {(columna-(len(lexActual)-1))}")
            if lexActual == "TITULO":
                token = Token("TITULO", lexActual, "TITULO", fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)
            elif lexActual == "=":
                token = Token("=",lexActual,"=",fila, (columna-(len(lexActual)-1)))
                listaTokens.append(token)
            
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

def error():
    pass
        
if __name__ == "__main__":
    txt = abrirArchivo()
    analizarArchivo(txt) 
    print(listaTokens)