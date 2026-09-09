import random

# equipo = ["Ana", "Daniel", "Carlos", "María", "Jorge", "Lucía", "Pedro", "Sofía"]

# elegido = random.choice(equipo)  # elige un elemento al azar
# print(f"El líder de turno elegido es: {elegido}")

lista_de_numeros = [10, 7, 5, 3, 8, 2]
numero_aleatorio = random.choice(lista_de_numeros)  # elige un elemento al azar
if numero_aleatorio % 2 == 0:
    print(f"El número elegido ({numero_aleatorio}) es par.")
else:
    print(f"El número elegido ({numero_aleatorio}) es impar.")

    