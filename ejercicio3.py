# Control de ventas en feria universitaria

# Variables para acumular el total general de toda la feria
total_feria = 0

dia = 1
while dia <= 3:  # 3 días
    print(f"\nDía {dia}")
    total_dia = 0
    stand = 1
    while stand <= 4:  # 4 stands por día
        print(f"  Stand {stand}")
        total_stand = 0
        producto = 1
        while producto <= 3:  # 3 productos por stand
            venta = float(input(f"    Ingrese venta del producto {producto}: $"))
            if venta < 0:
                print("    Venta no puede ser negativa. Se toma como 0.")
                venta = 0
            total_stand += venta
            producto += 1
        print(f"    Total ventas del stand {stand}: ${total_stand}")
        total_dia += total_stand
        stand += 1
    print(f"  Total del día {dia}: ${total_dia}")
    total_feria += total_dia
    dia += 1

print(f"\n💰 Total general de la feria: ${total_feria}")