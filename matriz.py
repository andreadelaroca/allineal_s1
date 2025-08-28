filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = []

for i in range(filas):
    fila_actual = [] # lista vacía para manejar fila actual
    for j in range(columnas):
        elemento = input(f"Introduzca el elemento {i + 1},{j + 1}: ")
        fila_actual.append(elemento)
    matriz.append(fila_actual)
    
if filas == columnas:
    print(f"La matriz es cuadrada.", end = " ")
else:
    print("La matriz es rectangular.", end = " ")    
       
print(f"Su tamaño es {filas}x{columnas}")

for fila in matriz:
    print(fila)
