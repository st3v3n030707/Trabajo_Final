# Cada día tiene 3 turnos: mañana, tarde y noche

# Lista de nombres de turnos
turnos = ["mañana", "tarde", "noche"]

# Iniciamos el número de edificio desde 1 hasta 4
edificio = 1

while edificio <= 4:
    print("\n--- Registro para el Edificio", edificio, "---")
    
    # Variables para acumular el consumo total del edificio
    consumo_total = 0
    dia = 1  # Día de la semana

    while dia <= 7:
        print("\nDía", dia)
        
        # Consumir energía en los 3 turnos
        turno = 0  # 0 = mañana, 1 = tarde, 2 = noche
        while turno < 3:
            entrada = input("Ingrese consumo en kWh para el turno " + turnos[turno] + ": ")

            # Intentamos convertir la entrada a número decimal
            try:
                consumo = float(entrada)

                # Verificamos que el consumo no sea negativo
                if consumo < 0:
                    print("El consumo no puede ser negativo. Intente de nuevo.")
                else:
                    consumo_total = consumo_total + consumo  # Acumulamos el consumo
                    turno = turno + 1  # Pasamos al siguiente turno

            except:
                print("Entrada inválida. Debe ingresar un número.")

        dia = dia + 1  # Pasamos al siguiente día

    # Al terminar los 7 días, calculamos el promedio diario
    promedio = consumo_total / 7

    # Mostramos resultados del edificio actual
    print("\n>>> Resultados del Edificio", edificio)
    print("Consumo total semanal:", round(consumo_total, 2), "kWh")
    print("Promedio diario:", round(promedio, 2), "kWh")

    edificio = edificio + 1  # Pasamos al siguiente edificio