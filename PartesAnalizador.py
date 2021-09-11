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