peso = float(input("¿Cuanto pesas en kilogramos?"))
altura = float(input("¿Cuanto mides en metros?"))

imc = peso / (altura ** 2)
print(f"Tu IMC es {round(imc, 1)}")
if imc < 18.5:
    print("Tienes bajo peso.")
elif imc < 25:
    print("Tienes un peso normal.")
elif imc < 30:
    print("Tienes sobrepeso.")
else:
    print("Tienes obesidad.")

