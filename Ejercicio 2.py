Descuento_Estudiante = 15
Descuento_Cliente_Frecuente = 10
print("Bienvenido A H&M")
print("Ingrese el precio del producto:")
Precio_Producto = float(input())

print("Eres estudiante? (si/no)")
Estudiante = input()
while True:
    if Estudiante == "si":
        break
    elif Estudiante == "no":
        break
    else:
        print("Respuesta no valida, por favor ingrese 'si' o 'no'")
        Estudiante = input()
if Estudiante == "si":
    Precio_Estudiante = Precio_Producto - (Precio_Producto * Descuento_Estudiante/100)
else:
    Precio_Estudiante = Precio_Producto


print("Eres cliente frecuente? (si/no)")
Cliente_Frecuente = input()
while True:
    if Cliente_Frecuente == "si":
        break
    elif Cliente_Frecuente == "no":
        break
    else:
        print("Respuesta no valida, por favor ingrese 'si' o 'no'")
        Cliente_Frecuente = input()
if Cliente_Frecuente == "si":
    Precio_Cliente_Frecuente = Precio_Producto - (Precio_Producto * Descuento_Cliente_Frecuente/100) 
else:
    Precio_Cliente_Frecuente = Precio_Producto

print("======RESUMEN DE COMPRA======")

if Estudiante == "si" and Cliente_Frecuente == "si":
    print("Descuento mas alto aplicado: Estudiante")
    Precio_Final = Precio_Estudiante
elif Estudiante == "si" and Cliente_Frecuente == "no":
    print("Descuento aplicado: Estudiante")
    Precio_Final = Precio_Estudiante
elif Estudiante == "no" and Cliente_Frecuente == "si":
    print("Descuento aplicado: Cliente Frecuente")
    Precio_Final = Precio_Cliente_Frecuente
elif Estudiante == "no" and Cliente_Frecuente == "no":
    print("No se aplico ningun descuento")
    Precio_Final = Precio_Producto

print("Precio original: " + str(Precio_Producto))
print("Precio Final: " + str(Precio_Final))
print("Gracias por su compra, vuelva pronto")