Lista_Libros = [
    "Tokio blues (Norwegian Wood) - Haruki Murakami",
    "Cien años de soledad - Gabriel García Márquez",
    "El marciano - Andy Weir",
    "La carretera - Cormac McCarthy",
    "El nombre del viento - Patrick Rothfuss",
]
print("=====Bienvenido a la biblioteca=====")
print("Seleccione la opción que desea realizar:")
print("0. Salir")
print("1. Ver todos los libros")
print("2. Buscar libro")
print("3. Agregar libro")
print("4. Eliminar libro")
opcion = int(input())
if opcion == 0:
    print("Gracias por usar la biblioteca. ¡Hasta luego!")
elif opcion == 1:
    print("Lista de libros disponibles:")
    for libro in Lista_Libros:
        print(libro)
    
elif opcion == 2:
    print("Ingrese el nombre del libro que desea buscar:")
    libro_buscado = input()
    if libro_buscado in Lista_Libros:
        print("El libro está disponible en la biblioteca.")
    else:
        print("El libro no está disponible en la biblioteca.")
elif opcion == 3:
    print("Ingrese el nombre del libro que desea agregar:")
    libro_nuevo = input()
    Lista_Libros.append(libro_nuevo)
    if libro_nuevo in Lista_Libros:
        print("El libro ya está en la biblioteca.")
    if Lista_Libros.count(libro_nuevo) > 10:
        print("Has alcanzado el límite de libros en la biblioteca.")
    print("El libro ha sido agregado a la biblioteca.")
elif opcion == 4:
    print("Ingrese el nombre del libro que desea eliminar:")
    libro_eliminar = input()
    if libro_eliminar in Lista_Libros:
        Lista_Libros.remove(libro_eliminar)
        print("El libro ha sido eliminado de la biblioteca.")
    else:
        print("El libro no está disponible en la biblioteca.")
else:
    print("Opción inválida. Por favor, seleccione una opción válida.")

