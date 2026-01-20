print(
    """
    CALCULADORA

    1.Suma
    2.Resta
    3.Multiplicacion
    4.División
    5.División entera
    6.Exponente
    7.Módulo
"""
)

num = int(input("Introduce la opción deseada: "))

match num:
    case 1:
        print(f"Elegiste suma")
        num = int(input("Introduce el primer número: "))
        num += int(input("Introduce el segundo número: "))
        print(f"Resultado: {num}")
    case 2:
        print(f"Elegiste resta")
        num = int(input("Introduce el primer número: "))
        num -= int(input("Introduce el segundo número: "))
        print(f"Resultado: {num}")
    case 3:
        print(f"Elegiste multiplicación")
        num = int(input("Introduce el primer número: "))
        num *= int(input("Introduce el segundo número: "))
        print(f"Resultado: {num}")
    case 4:
        print(f"Elegiste división")
        num = int(input("Introduce el primer número: "))
        num /= int(input("Introduce el segundo número: "))
        print(f"Resultado: {num}")
    case 5:
        print(f"Elegiste división entera")
        num = int(input("Introduce el primer número: "))
        num //= int(input("Introduce el segundo número: "))
        print(f"Resultado: {num}")
    case 6:
        print(f"Elegiste exponenciación")
        num = int(input("Introduce el primer número: "))
        num **= int(input("Introduce el segundo número: "))
        print(f"Resultado: {num}")
    case 7:
        print(f"Elegiste módulo")
        num = int(input("Introduce el primer número: "))
        num %= int(input("Introduce el segundo número: "))
        print(f"Resultado: {num}")
    case _:
        print("Opción no válida")