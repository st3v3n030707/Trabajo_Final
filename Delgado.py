# Definimos las secciones y los estudiantes por sección
secciones = ['A', 'B', 'C']
estudiantes_por_seccion = 6
dias = 5

# Creamos un diccionario para almacenar las asistencias por sección
asistencias = {seccion: 0 for seccion in secciones}

# Recorremos cada día de la semana
for dia in range(1, dias + 1):
    print(f"\nDía {dia}:")
    # Para cada sección, registramos la asistencia de cada estudiante
    for seccion in secciones:
        print(f"Sección {seccion}:")
        for estudiante in range(1, estudiantes_por_seccion + 1):
            # Solicitamos al usuario si el estudiante asistió (S/N)
            respuesta = input(f"¿Asistió el estudiante {estudiante}? (S/N): ").strip().upper()
            # Si la respuesta es 'S', sumamos una asistencia
            if respuesta == 'S':
                asistencias[seccion] += 1

# Mostramos el total de asistencias por sección
print("\nResumen de asistencias por sección:")
total_general = 0
for seccion in secciones:
    print(f"Sección {seccion}: {asistencias[seccion]} asistencias")
    total_general += asistencias[seccion]

# Mostramos el total general de asistencias
print(f"\nTotal general de asistencias en la semana: {total_general}")
