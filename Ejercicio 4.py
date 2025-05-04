
print("=======MENU=======")
print("Seleccione la conversion que desea realizar:")
print("0.Salir")
print("1.Convertir de kilometros a millas")
print("2.Convertir de millas a kilometros")
print("3.Convertir de Grados celsius a Grados Fahrenheit")
print("4.Convertir de Grados Fahrenheit a Grados Celsius")

print("Ingrese el numero de la conversion que desea realizar:")
opcion = int(input())

while True:
    if opcion == 0:
        print("Gracias por usar el convertidor de unidades. ¡Hasta luego!")
        break
    elif opcion == 1:
        print("Ingrese la distancia en kilometros:")
        distancia_km = float(input())
        if distancia_km < 0:
            print("La distancia no puede ser negativa.")
            continue
        distancia_millas = distancia_km * 0.621371
        print(f"{distancia_km} kilometros son {distancia_millas} millas.")
    elif opcion == 2:
        print("Ingrese la distancia en millas:")
        distancia_millas = float(input())
        if distancia_millas < 0:
            print("La distancia no puede ser negativa.")
            continue
        distancia_km = distancia_millas / 0.621371
        print(f"{distancia_millas} millas son {distancia_km} kilometros.")
    elif opcion == 3:
        print("Ingrese la temperatura en grados Celsius:")
        temperatura_celsius = float(input())
        temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
        print(f"{temperatura_celsius} grados Celsius son {temperatura_fahrenheit} grados Fahrenheit.")
        if 15 <= temperatura_celsius <= 25:
            print("La temperatura es normal.")
            if temperatura_celsius < 15:
                print("La temperatura es baja.")
            elif temperatura_celsius > 25:
                print("La temperatura es alta.")
    elif opcion == 4:
        print("Ingrese la temperatura en grados Fahrenheit:")
        temperatura_fahrenheit = float(input())
        temperatura_celsius = (temperatura_fahrenheit - 32) * 5/9
        print(f"{temperatura_fahrenheit} grados Fahrenheit son {temperatura_celsius} grados Celsius.")
        if 59 <= temperatura_fahrenheit <= 77:
            print("La temperatura es normal.")
            if temperatura_fahrenheit < 59:
                print("La temperatura es baja.")
            elif temperatura_fahrenheit > 77:
                print("La temperatura es alta.")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
    
    print("Seleccione otra conversión o ingrese 0 para salir:")
    opcion = int(input())
print("Saliendo del programa...")


