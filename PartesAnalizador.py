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
    def __init__(self):
        pass

class Imagen:
    def __init__(self):
        pass