print("BIENVENIDO A LA TIENDA VIRTUAL!!!")

catalogo = {"Camiseta": 20,
            "Jeans": 40,
            "Zapatos": 60,
            "Sombrero": 10}
carrito = {}

menu = """\nMenú:
1.Agregar productos al carrito
2.Ver carrito
3.Realizar pago y salir"""

op = None

while True:
    print(menu)
    try:
        op = int(input("Seleccione una opción: "))
        print()

        match op:
            case 1:
                print("Productos disponibles")
                # Muestro todos los productos
                for producto, precio in catalogo.items():
                    print(f"‣{producto} - ${precio}")
                # Ingreso el nombre del producto y lo formateo para que
                # arranque con mayuscula y luego minuscula
                producto = input(
                    "Escribe el nombre del producto que deseas seleccionar: "
                    ).capitalize()
                # Si el producto no existía lo agrego al carrito, si ya existía
                # obtengo la cantidad actual. Le sumo uno a la cantidad
                if producto in catalogo:
                    cantidad_producto = carrito.setdefault(producto, 0)
                    carrito[producto] = cantidad_producto + 1
                    print(f"Producto '{producto}' agregado al carrito")
                else:
                    print("Ese producto no está en el catálogo")

            case 2:
                print("Carrito: ")
                for producto, cantidad in carrito.items():
                    precio_unitario = catalogo[producto]
                    print(f"{cantidad} {producto} - ${precio_unitario} c/u")

            case 3:
                print("Seleccionaste la opción para realizar el pago.")
                total_a_pagar = 0
                # Calculo el total a pagar
                for producto, cantidad in carrito.items():
                    precio_unitario = catalogo[producto]
                    total_a_pagar += cantidad * precio_unitario
                print(f"Total a pagar ${total_a_pagar}")
                # Se calcula el cambio
                try:
                    monto_recibido = float(input(
                        "Ingrese el monto con el que pagará: "))
                    if monto_recibido < total_a_pagar:
                        print("El monto ingresado es insuficiente")
                    elif monto_recibido > total_a_pagar:
                        print("Gracias por su compra, su cambio es "
                              f"${monto_recibido - total_a_pagar}")
                        break
                    elif monto_recibido == total_a_pagar:
                        print("Gracias por su compra. No se requiere cambio")
                        break
                except Exception:
                    print("Monto inválido. Ingrese un monto válido.")
            case _:
                print("Fuera de rango. Por favor ingresa una opción válida.")

    except ValueError:
        print()
        print("Opción no válida. Por favor ingresa una opción válida.")
    except Exception as e:
        print(f"Ocurrio un error: {e}")

input("Presiona cualquier tecla para salir...")
