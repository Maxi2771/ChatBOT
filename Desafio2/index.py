num1 = int(input("Ingresar primer número para la suma: "))
num2 = int(input("Ingresar segundo número para la suma: "))
num3 = int(input("Ingresar tercer número para la suma: "))

suma = num1 + num2 + num3
print(f"La suma de los números es: {suma}")

num1F = float(input("Ingresar primer número para la resta: "))
num2F = float(input("Ingresar segundo número para la resta: "))

resta = num1F - num2F
print(f"La resta de los números es: {resta}")

num1M = int(input("Ingresar primer número para comparar: "))
num2M = int(input("Ingresar segundo número para comparar: "))

if num1M > num2M:
    print(f"{num1M} número es mayor")
elif num2 > num1:
    print(f"{num2M} número es mayor")
else:
    print("Los números son iguales")