num = int(input("Qué tabla de multiplicar desea ver: "))
print(f"La tabla del {num} es:")

for i in range(11):
    print(f"{num} x {i} = {num*i}")