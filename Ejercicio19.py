tupla = (("Eduardo", 26), ("María", 30), ("Gerardo", 10), ("Valentina", 22))

may_edad = 0
may_nom = None
men_edad = 999
men_nom = None
for nombre, edad in tupla:
    if edad > may_edad:
        may_edad = edad
        may_nom = nombre
    if edad < men_edad:
        men_edad = edad
        men_nom = nombre

print(f"El mayor es {may_nom} con {may_edad}")
print(f"El menor es {men_nom} con {men_edad}")
