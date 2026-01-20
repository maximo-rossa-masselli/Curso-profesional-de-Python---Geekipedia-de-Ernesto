fruits = {
    "manzanas": 5,
    "peras": 2,
    "naranjas": 4
}

# EJERCICIO 1
print("EJERCICIO 1")
print(fruits)
print(f"La cantidad de manzanas es: {fruits.get("manzanas")}")

print()
# EJERCICIO 2
print("EJERCICIO 2")
print(fruits)
fruits.update({"bananas": 5, "mangos": 6, "uvas": 3})
print("Diccionario actualizado", fruits, sep="\n")

print()
# EJERCICIO 3
print("EJERCICIO 3")
print(fruits)
fruits.pop("peras")
print("Diccionario actualizado", fruits, sep="\n")

# Vuelvo a agregar las peras
fruits.update({"peras": 2})
print()
# EJERCICIO 4
print("EJERCICIO 4")
print(fruits)
claves = list(fruits.keys())
valores = list(fruits.values())
print(claves)

print()
# EJERCICIO 5
print("EJERCICIO 5")
print(fruits)

if "manzanas" in fruits:
    print(True)
else:
    print(False)
