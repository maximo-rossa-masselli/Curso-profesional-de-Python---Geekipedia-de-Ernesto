num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
num3 = int(input("Introduce el tercer numero: "))

if num1 > num2 and num1 > num3:
    may = num1
elif num2 > num3:
    may = num2
else:
    may = num3

print(f"El numero {may} es el mayor")