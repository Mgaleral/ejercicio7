# Ejercicio 7
lista_datos =[]
while True:
    nombre = input("¿Cual es tu nombre?: ")
    if nombre == "fin":
        break
    telefono = input("¿Cual es tu telefono?: ")
    línea = {}
    línea["Nombre"] = nombre
    línea["Telefono"] = telefono
    lista_datos.append(línea)

for linea in lista_datos:
    print("Lista de: ", linea)
