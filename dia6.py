frutas = ["manzana", "plátano", "naranja"]
print(frutas[0])   # manzana  (el PRIMERO es el índice 0)
print(frutas[1])   # plátano
print(frutas[2])   # naranja
print(frutas[-1])   # naranja (el último)
print(frutas[-2])   # plátano (el penúltimo)
print(frutas[-3])   # manzana (el antepenúltimo)


frutas = ["manzana", "plátano"]

frutas.append("uva")     # agrega "uva" al final
print(len(frutas))       # 3  → len() dice cuántos elementos hay
print("uva" in frutas)   # True → ¿está "uva" en la lista?