#contador = 0

#while contador < 5:
    #print(f"Vuelta número {contador}")
    #contador = contador + 1
import random

secreto = random.randint(1, 100)
intentos = 0 
adivina = 0 # 1. Crear una variable para almacenar la adivinanza del usuario

# 2. El while loop continuará hasta que el usuario adivine el número secreto
while adivina != secreto:
    adivina = int(input("Adivina el número secreto (1-100): "))
    intentos += 1 
    if adivina < secreto:
        print("Muy bajo, intenta mas alto.")
    elif adivina > secreto:
        print("Muy alto, intenta mas bajo.")
    else:
        print(f"¡Felicidades! Ganaste en {intentos} intentos.")
    # 3. Ya no es necesario el break, ya que el while loop se detendrá automáticamente cuando adivina sea igual a secreto.




