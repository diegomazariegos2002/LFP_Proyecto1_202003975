import math
#============================================== Parte de base cualquiera a decimal =============================================

def base_Decimal(numero, factor, contador, posicion_Actual):
    if contador == (len(numero)-1):
        return valor_Posicion_Actual(numero[contador], factor, posicion_Actual)
    else:
        return base_Decimal(numero, factor, contador + 1, posicion_Actual - 1 ) + valor_Posicion_Actual(numero[contador], factor, posicion_Actual)

def valor_Posicion_Actual(caracter, factor, posicion_Actual):
    if caracter == "A":
        caracter = 10
    elif caracter == "B":
        caracter = 11
    elif caracter == "C":
        caracter = 12
    elif caracter == "D":
        caracter = 13
    elif caracter == "E":
        caracter = 14
    elif caracter == "F":
        caracter = 15
    else:
        caracter = int(caracter)
    return caracter * (factor**posicion_Actual)

#============================================== Parte de decimal a base cualquiera ==============================================
def decimal_Base(numero, factor):
    if numero<factor:
        return caracter(numero)
    else:
        return decimal_Base(math.floor(numero/factor), factor) + caracter(numero%factor)

def caracter(residuo):
    if residuo==10:
        return "A"
    elif residuo ==11:
        return "B"
    elif residuo ==12:
        return "C"
    elif residuo ==13:
        return "D"
    elif residuo ==14:
        return "E"
    elif residuo ==15:
        return "F"
    else:
        return str(residuo)
        



if __name__ == "__main__":
    numero = "145B"
    factorOrigen = 14
    factorDestino = 6
    print(base_Decimal(numero, factorOrigen, 0, len(numero) - 1))
    print(decimal_Base(base_Decimal(numero, factorOrigen, 0, len(numero) - 1), factorDestino))