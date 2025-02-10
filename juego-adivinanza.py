# JUEGO DE ADIVINANZA 

import random

numero_secreto = random.randint (0,101)
numero_adivinado = False
cantidad_intentos = 0
cantidad_maxima_intentos = 5

nombre = input ("Ingresa tu nombre: ")
print ("¡Bienvenidx", nombre, "al juego de adivinar el número secreto!")


while not numero_adivinado and cantidad_intentos < cantidad_maxima_intentos:
    numero_ingresado = int ((input ("Ingresá un número del 0 al 101: ")))

    if numero_ingresado == numero_secreto:
        print ("¡Felicitaciones", nombre, "adivinaste el número secreto! ¡Ganaste!")
        numero_adivinado = True

    elif numero_ingresado < numero_secreto:
        print ("El número secreto es mayor al ingresado")

    else:
        print ("El número secreto es menor al ingresado")
    
    cantidad_intentos += 1

if not cantidad_intentos < cantidad_maxima_intentos:
    print (nombre, "perdiste el juego. No pudiste adivinar el número secreto dentro de los intentos permitidos.")
