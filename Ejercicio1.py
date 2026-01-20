nombre = input("Ingrese su nombre: ")
depto = int(input("Ingrese la clave de su departamento: "))
antiguedad = int(input("Ingrese sus años de antiguedad: "))

dias = 0
if depto == 1:
    if antiguedad <= 1:
        dias = 6
    elif antiguedad >= 2 and antiguedad <=6:
        dias = 14
    elif antiguedad >= 7:
        dias = 20
elif depto == 2:
    if antiguedad <= 1:
        dias = 7
    elif antiguedad >= 2 and antiguedad <=6:
        dias = 15
    elif antiguedad >= 7:
        dias = 22
elif depto == 3:
    if antiguedad <= 1:
        dias = 10
    elif antiguedad >= 2 and antiguedad <=6:
        dias = 20
    elif antiguedad >= 7:
        dias = 30
else:
    print("Departamento no válido")

print(f"{nombre} tienes {dias} dias de vacaciones")