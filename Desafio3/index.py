diccionario = {}

print("Ingresa nombres y edades para el diccionario (presioná Enter sin ingresar un nombre para terminar)")
while True:
    nombre = input("Ingresa el nombre: ")
    if nombre.lower() == '':
        break
    edad = input(f"Ingresa la edad de {nombre}: ")
    diccionario[nombre] = edad

print("\nContenido del diccionario:")
for nombre, edad in diccionario.items():
    print(f"Nombre: {nombre}, Edad: {edad}")

nombre_buscar = input("\nIngresa el nombre que quieres buscar: ")

if nombre_buscar in diccionario:
    edad_encontrada = diccionario[nombre_buscar]
    print(f"La edad de {nombre_buscar} es: {edad_encontrada}")
else:
    print(f"El nombre '{nombre_buscar}' no se encontró en el diccionario.")