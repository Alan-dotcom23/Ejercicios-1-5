Lista_Libros = [
    "Tokio blues (Norwegian Wood) - Haruki Murakami",
    "Cien años de soledad - Gabriel García Márquez",
    "El marciano - Andy Weir",
    "La carretera - Cormac McCarthy",
    "El nombre del viento - Patrick Rothfuss",
]

print("¡Bienvenido a la biblioteca digital!")

def mostrar_menu():
    print("===== Menú =====")
    print("Seleccione la opción que desea realizar:")
    print("0. Salir")
    print("1. Ver todos los libros")
    print("2. Buscar libro")
    print("3. Agregar libro")
    print("4. Eliminar libro")
    
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (0-4): ")

    if opcion == "1":
        print("===== Lista de libros disponibles: =====")
        for libro in Lista_Libros:
            print(libro)

    elif opcion == "2":
        nombre = input("Introduce el nombre del libro que deseas buscar: ").strip()
        if nombre in Lista_Libros:
            print("El libro está disponible en la biblioteca.")
        else:
            print("El libro no está disponible en la biblioteca.")

    elif opcion == "3":
        if len(Lista_Libros) >= 10:
            print("Has excedido el límite de la versión gratuita.")
        else:
            nuevo_libro = input("Introduce el nombre del nuevo libro: ").strip()
            if nuevo_libro in Lista_Libros:
                print("Ese libro ya existe en la biblioteca.")
            else:
                Lista_Libros.append(nuevo_libro)
                print(f"Libro '{nuevo_libro}' agregado correctamente.")
                if len(Lista_Libros) == 10:
                    print("Has alcanzado el límite de la versión gratuita (10 libros).")

    elif opcion == "4":
        libro_eliminar = input("Ingrese el nombre del libro que desea eliminar: ").strip()
        if libro_eliminar in Lista_Libros:
            Lista_Libros.remove(libro_eliminar)
            print("El libro ha sido eliminado de la biblioteca.")
        else:
            print("El libro no está disponible en la biblioteca.")

    elif opcion == "0":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida, por favor elija una opción del 0 al 4.")






