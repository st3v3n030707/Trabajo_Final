# Contadores
ocupadas_lab1 = 0
libres_lab1 = 0
ocupadas_lab2 = 0
libres_lab2 = 0

# LABORATORIO 1
print("Laboratorio 1")
contador = 1
while contador <= 20:
    estado = int(input("¿Computadora " + str(contador) + " ocupada (1) o libre (0)? "))
    if estado == 1:
        ocupadas_lab1 += 1
    else:
        libres_lab1 += 1
    contador += 1

# LABORATORIO 2
print("\nLaboratorio 2")
contador = 1
while contador <= 20:
    estado = int(input("¿Computadora " + str(contador) + " ocupada (1) o libre (0)? "))
    if estado == 1:
        ocupadas_lab2 += 1
    else:
        libres_lab2 += 1
    contador += 1

# RESULTADOS
print("\nResumen:")
print("Laboratorio 1 - Ocupadas:", ocupadas_lab1, "Libres:", libres_lab1)
print("Laboratorio 2 - Ocupadas:", ocupadas_lab2, "Libres:", libres_lab2)
