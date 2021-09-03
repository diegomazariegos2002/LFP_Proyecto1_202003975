from tkinter import filedialog, Tk

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


if __name__ == "__main__":
    while(True):
        print("\nBienvenido Usuario")
        print(''''Menú provisional
        1. Cargar archivo
        2. Analizar archivo
        3. Ver reportes
        4. Seleccionar imagen
        5. Ver imagen
        6. Salir''')
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            print("\nEscogió la opción 1 - Cargar archivo")
            abrirArchivo()

        elif opcion == 2:
            print("\nEscogió la opción 2 - Analizar archivo")
            input("Presione Enter para continuar....")
        elif opcion == 3:
            print("\nEscogió la opción 3 - Ver reportes")
            input("Presione Enter para continuar....")
        elif opcion == 4:
            print("\nEscogió la opción 4 - Seleccionar imagen")
            input("Presione Enter para continuar....")
        elif opcion == 5:
            print("\nEscogió la opción 5 - Ver imagen")
            input("Presione Enter para continuar....")
        elif opcion == 6:
            print("\nEscogió la opción 6 - Salir")
            input("Presione Enter para continuar....")
            break
        else:
            print("\ningrese un digito correcto")
            input("Presione Enter para continuar....")
