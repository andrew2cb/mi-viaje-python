#contador = 0

#while contador < 5:
    #print(f"Vuelta número {contador}")
    #contador = contador + 1
import random

secreto = random.randint(1, 101)
intentos = 0 # 1. Creamos el contador en cero antes del while

while secreto != 0:
    adivina = int(input("Adivina el número secreto (1-100): "))
    intentos += 1 # 2. Sumamos 1 en cada intento por cada vuelta del while
    if adivina < secreto:
        print("Muy bajo, intenta mas alto.")
    elif adivina > secreto:
        print("Muy alto, intenta mas bajo.")
    else:
        print(f"¡Felicidades! Ganaste en {intentos} intentos.")
        break




