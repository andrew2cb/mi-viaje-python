import string
import random
# 1. Definimos los conjuntos de caracteres
letras = string.ascii_letters
numeros = string.digits
simbolos = string.punctuation

contrasena_caracteres = int(input("¿Cuántos caracteres quiere que tenga la contraseña? "))
# 2. GARANTIZAMOS los obligatorios (al menos una letra, un número y un símbolo)
password_lista = [
    random.choice(letras),
    random.choice(numeros),
    random.choice(simbolos)
]
# 3. Rellenamos el resto de los caracteres necesarios hasta completar la longitud pedida
caracteres_totales = letras + numeros + simbolos
for i in range(contrasena_caracteres - 3):
    password_lista.append(random.choice(caracteres_totales))
# 4. REVOLVEMOS la lista para que el orden sea totalmente aleatorio (aquí sí funciona shuffle)
random.shuffle(password_lista)
# 5. Convertimos la lista resultante de vuelta a un texto (string)
contrasena = "".join(password_lista)
print(f"Su contraseña generada es: {contrasena}") 
