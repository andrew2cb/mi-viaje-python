# numeros = [10, 20, 30, 40, 50, 60]

# print(numeros[1:4])    # [20, 30, 40]

# print(numeros[:3])     # [10, 20, 30]  → desde el principio hasta el índice 3 (sin incluirlo)
# print(numeros[3:])     # [40, 50, 60]  → desde el índice 3 hasta el final
# print(numeros[-2:])    # [50, 60]      → los últimos dos

tablero = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "X", "O"]
]

#print(tablero[0])       # ["X", "O", "X"]  → la primera fila completa
print(tablero[0][0])    # "O"  → fila 0, columna 1