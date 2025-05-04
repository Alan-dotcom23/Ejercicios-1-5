def cumple_criterios(cancion, duracion_minutos, genero_musical, año_lanzamiento):
    nombre_obj = cancion.split(" – ")[0]
    duracion_min=2.5
    duracion_max=4.5
    if duracion_minutos >= duracion_min and duracion_minutos <= duracion_max:
        if genero_musical in cancion:
            if año_lanzamiento > 2010:
                return True
Canciones = [
    "Tame Impala – The Less I Know the Better",
    "Shakira – Ojos Así",
    "Daft Punk – Instant Crush (feat. Julian Casablancas)",
    "Vicente Fernández – Volver, Volver",
    "Bad Bunny – La Difícil",
    "Fleetwood Mac – Dreams",
    "Rosalía – MOTOMAMI",
    "Arctic Monkeys – Do I Wanna Know?",
    "Juan Gabriel – Querida",
    "Beyoncé – Love On Top"]
Duracion = [
    3.36, 4.23, 4.00, 3.00, 3.30, 4.10, 3.50, 4.20, 3.45, 4.15]
Género = [
    "Rock", "Pop", "Electronic", "Ranchera", "Reggaeton",
    "Rock", "Flamenco", "Rock", "Pop", "R&B"]
Año = [
    2015, 1998, 2013, 1972, 2018, 1977, 2022, 2013, 1984, 2011]
print("Lista de Canciones:")
for i in range(len(Canciones)):
    print(f"{i + 1}. {Canciones[i]}")


cancion_seleccionada = int(input("Selecciona el número de la canción: "))
while cancion_seleccionada < 1 or cancion_seleccionada > len(Canciones):
    print("Número inválido. Por favor, selecciona un número de la lista.")
    cancion_seleccionada = int(input("Selecciona el número de la canción: "))

if 1 <= cancion_seleccionada <= 10:
    print("=======Cancion seleccionada=======")
    print("Nombre de la cancion:" + Canciones[cancion_seleccionada - 1])
    print("Duración: " + str(Duracion[cancion_seleccionada - 1]) + " minutos")
    print("Género: " + Género[cancion_seleccionada - 1])
    print("Año: " + str(Año[cancion_seleccionada - 1]))
    
    print("=======Criterios:=======")
    print("1. Duración entre 2.5 y 4.5 minutos")
    print("2. Género musical: rock, pop o indie")
    print("3. Año de lanzamiento posterior a 2010")
else:
    print("Número inválido. Por favor, selecciona un número de la lista.")


indice = cancion_seleccionada - 1
print("¿Cumple con los criterios?")
if cumple_criterios(Canciones[indice], Duracion[indice], Género[indice], Año[indice]):
    print("Esta canción cumple con los criterios.")
else:
    print("Esta canción no cumple con los criterios.")