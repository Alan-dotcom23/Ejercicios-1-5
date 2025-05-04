Nombre_Usuario = "Alan"
Contraseña_Usuario = "28042025"
Pista = Contraseña_Usuario[1]

print("Ingrese su nombre de usuario:")
Nombre_Usuario_Ingresado = input()
while True:
    if Nombre_Usuario_Ingresado == Nombre_Usuario:
        print("Usuario correcto")
        break
    else:
        print("Usuario incorrecto, vuelva a intentarlo")
        print("Ingrese su nombre de usuario:")
        Nombre_Usuario_Ingresado = input()

print("Ingrese su contraseña:")
Contraseña_Usuario_Ingresada = input()
while True:
    if Contraseña_Usuario_Ingresada == Contraseña_Usuario:
        print("Contraseña correcta, Bienvenido al sistema")
        break
    else:
        print("Contraseña incorrecta, vuelva a intentarlo")
        print("Ingrese su contraseña, Segundo caracter : " + Pista)
        Contraseña_Usuario_Ingresada = input()
        