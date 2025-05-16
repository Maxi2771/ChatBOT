def marcar_pares(num):
    for i in range(num + 1):
        if i % 2 == 0:
            print(f"{i} PAR")
        else:
            print(i)
num = int(input("Ingrese un número: "))
print(marcar_pares(num))  