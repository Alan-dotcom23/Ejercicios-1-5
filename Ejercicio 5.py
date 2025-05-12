Lista_Libros = [
    "Tokio blues (Norwegian Wood)",
    "Cien años de soledad",
    "El marciano",
    "La carretera",
    "El nombre del viento",
]

print("¡Bienvenido a la biblioteca digital!")

def mostrar_menu():
    print("===== Menú =====")
    print("0. Salir")
    print("1. Ver todos los libros")
    print("2. Buscar libro")
    print("3. Agregar libro")
    print("4. Eliminar libro")
    print("5. Mostrar menú")

mostrar_menu()
print("Selecciona una opción (0-5): ")
while True:
    opcion = input()
    
    if opcion == "1":
        print("===== Lista de libros disponibles: =====")
        for libro in Lista_Libros:
            print(libro)
        print("===== Para ver el menu presione 5 ======")

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
    
    elif opcion == "5":
        mostrar_menu()

    elif opcion == "0":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida, por favor elija una opción del 0 al 5.")






