laboratorios = 2
filas = 5
columnas =4

estado_labs = []

for lab in range(laboratorios):
    laboratorio = []
    print(f"Ingrese datos para el Laboratorio {lab + 1}")
    for fila in range(filas):
        fila_computadoras = []
        for col in range(columnas):
            estado = input(f"fila {fila + 1}, Computadora {col + 1} (1 = ocupada, 0 = libre): ")
            while estado not in ['0' , '1']:
                estado = input(" Solo se permite 0 o 1. Intente de nuevo: ")
            fila_computadoras.append(int(estado))
        laboratorio.append(fila_computadoras)
    estado_labs.append(laboratorio)

for i, laboratorio in enumerate(estado_labs):
    ocupadas = 0
    libres = 0
    print(f"Laboratorio {i + 1}")
    for fila in laboratorio:
        for compu in fila:
            if compu == 1:
                ocupadas += 1
            else: 
                libres += 1
    print(f"Computadoras ocupadas: {ocupadas}")
    print(f"Computadoras libres: {libres}") 

#Línea 1: Se define que hay 2 laboratorios.
#Línea 2: Se define que cada laboratorio tiene 5 filas.
#Línea 3: Se define que cada fila tiene 4 computadoras.

#Línea 5: Se crea una lista vacía para guardar todos los laboratorios.

#Línea 7: Inicia un bucle para recorrer los 2 laboratorios.
#Línea 8: Se crea una lista temporal para guardar los datos de un laboratorio.
#Línea 9: Se muestra un mensaje indicando al usuario que debe ingresar datos del laboratorio.
#Línea 10: Se inicia un bucle para recorrer las filas del laboratorio.
#Línea 11: Se crea una lista temporal para guardar el estado de cada computadora de esa fila.
#Línea 12: Se inicia un bucle para recorrer las 4 computadoras de la fila.
#Línea 13: Se pide al usuario que ingrese si la computadora está ocupada (1) o libre (0).
#Línea 14: Se valida que la entrada solo sea '0' o '1'.
#Línea 15: Si no es válida, se vuelve a pedir el dato al usuario.
#Línea 16: Se convierte el dato a entero y se guarda en la lista de la fila.
#Línea 17: Al terminar la fila, se agrega a la lista del laboratorio.
#Línea 18: Al terminar todas las filas, se agrega el laboratorio completo a la lista general.

#Línea 20: Se recorre cada laboratorio ya lleno para mostrar el resumen.
#Línea 21: Se inicializa el contador de computadoras ocupadas.
#Línea 22: Se inicializa el contador de computadoras libres.
#Línea 23: Se imprime el número del laboratorio actual.
#Línea 24: Se recorre cada fila del laboratorio.
#Línea 25: Se recorre cada computadora de la fila.
#Línea 26: Si la computadora está ocupada (valor 1), se suma al contador de ocupadas.
#Línea 28: Si la computadora está libre (valor 0), se suma al contador de libres.
#Línea 29: Se imprime el total de computadoras ocupadas en ese laboratorio.
#Línea 30: Se imprime el total de computadoras libres en ese laboratorio.



  




