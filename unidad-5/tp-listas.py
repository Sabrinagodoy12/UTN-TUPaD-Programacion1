# 1) Crear una lista con las notas de 10 estudiantes. 
# • Mostrar la lista completa. 
# • Calcular y mostrar el promedio. 
# • Indicar la nota más alta y la más baja. 

notas = [8, 5, 7, 9, 8, 9, 9, 8, 7, 3]

for i in range(len(notas)):
    print(notas[i])

#Calculo el promedio de las notas del array
promedio = sum(notas) / len(notas)
print(f"El promedio de las notas es: {promedio}")

#Calculo las nota más alta y más baja
maximo = max(notas)
minimo = min(notas)
print(f"La nota más alta es {maximo} y la nota más baja es {minimo}")


# 2) Pedir al usuario que cargue 5 productos en una lista. 
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

for i in range(5):
    producto = input("Ingrese un producto: ")
    i += 1
    productos.append(producto)

#Lista en orden alfabético
print(sorted(productos))

#El usuario ingresa qué producto desea eliminar, en el caso de existir muestra la lista sin ese producto, sino muestra un mensaje de error
producto_eliminado = input("Ingrese qué producto desea eliminar: ")
if producto_eliminado in productos:
    productos.remove(producto_eliminado)
    print(sorted(productos))
else:
    print(f"El producto: {producto_eliminado} no se encuentra en la lista de productos")


# 3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
# • Crear una lista con los pares y otra con los impares. 
# • Mostrar cuántos números tiene cada lista.

import random 

lista = []
num_par = []
num_impar = []

#Genero los 15 números aleatorios
for i in range(15):
    numero_aleatorio = random.randint(1, 100+1)
    lista.append(numero_aleatorio)

    #Si es par el número aleatorio se suma en un array de números pares, sino en uno de números impares
    if numero_aleatorio % 2 == 0:
        num_par.append(numero_aleatorio)
    else:
        num_impar.append(numero_aleatorio)
    i += 1

print(f"La lista con los 15 números al azar es: {lista}")
print(f"La lista de números pares es: {num_par} \nLa lista de números impares es: {num_impar}")


# 4) Dada una lista con valores repetidos: datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos. 
# • Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []

#Recorro el array y voy guardando los números en uno nuevo, si se repite, no se guarda
for i in datos:
    if i not in sin_repetidos:
        sin_repetidos.append(i)

print(f"La lista original es: {datos}")
print(f"La lista sin repetir números es: {sin_repetidos}")


# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
# • Mostrar la lista final actualizada. 

estudiantes = ["Pedro", "Paula", "Andrea", "Nicolas", "Victoria", "Celeste", "Luciano", "Ignacio"]

for i in estudiantes:
    print(i, end=", ")

#Le pregunto al usuario que opción quiere realizar
opcion = input("\n(A)¿Desea agregar un nuevo estudiante a la lista de presentes? \n(B)¿Desea eliminar un alumno de la lista?").upper()

#Agrego un item a la lista
if opcion == "A":
    nuevo_estudiante = input("Ingrese el nombre del estudiante que desea agregar: ").title()
    estudiantes.append(nuevo_estudiante)

#Elimino un item de la lista
elif opcion == "B":
    eliminar_estudiante = input("Ingrese el estudiante que desea eliminar de la lista: ").title()
    if eliminar_estudiante in estudiantes:
        estudiantes.remove(eliminar_estudiante)
    else:
        print(f"{eliminar_estudiante} no se encuentra dentro de la lista de presentes.")
else:
    print("Opción inválida")

print(f"Los estudiantes presentes son: {estudiantes}")


# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
# último pasa a ser el primero).

numeros = [1, 2, 3, 4, 5, 6, 7]

#cambio de posición el primer número y muevo el resto uno a la derecha
ultimo_num = numeros[-1]
resto_nums = numeros[:-1]
numeros_rotados = [ultimo_num] + resto_nums

print(f"La lista original es: {numeros} \nLa lista rotada es: {numeros_rotados}")


# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
# semana. 
# • Calcular el promedio de las mínimas y el de las máximas. 
# • Mostrar en qué día se registró la mayor amplitud térmica. 

temperaturas = [
    [12, 23],
    [20, 27],
    [23, 29],
    [30, 36],
    [29, 32],
    [25, 29],
    [20, 24]
]
print(temperaturas)

#Muestro la temperatura mínima y máxima
minima = [fila[0] for fila in temperaturas] 
maxima = [fila[1] for fila in temperaturas] 

#Muestro su promedio
promedio_min = sum(minima) / len(minima)
print(f"El promedio de las temperaturas mínimas de la semana es: {promedio_min}")

promedio_max = sum(maxima) / len(maxima)
print(f"El promedio de las temperaturas máximas de la semana es: {promedio_max}")

#Muestro cuál es el día con mayor amplitud
amplitud = [fila[1] - fila[0] for fila in temperaturas]
mayor_amplitud = amplitud.index(max(amplitud))+1

print(f"El día con mayor amplitud es el día: {mayor_amplitud}")


# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
# • Mostrar el promedio de cada estudiante. 
# • Mostrar el promedio de cada materia. 

notas = [
    [8, 7, 9],
    [7, 6, 7],
    [6, 5, 5],
    [9, 9, 8],
    [8, 6, 9]
]

#Muestro las notas
for fila in notas:
    for nota in fila:
        print(nota, end=" ")
    print()

#Saco el promedio  de las notas de cada estudiante
for i in range(5):
    suma = 0
    for j in range(3):
        suma += notas[i] [j]
    promedio = suma/3
    i+=1
    print(f"El estudiante: {i}, tiene un promedio de: {promedio}")

#Saco el promedio por materia
for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i] [j]
    promedio= suma /5
    j += 1
    print(f"El promedio por la materia: {j} es de: {promedio}")


# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
# • Inicializarlo con guiones "-" representando casillas vacías. 
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
# • Mostrar el tablero después de cada jugada. 

#Inicializo las casillas con guiones
tablero=[]

for i in range(3):
    fila = []
    for j in range(3):
        fila.append("-")
    tablero.append(fila)

#Muestro el tablero completo
for fila in tablero:
    for celda in fila:
       print(celda, end=" ")
    print()

#Inicializo las variables
jugadas = 0
jugador= "X"


#El juego se repetirá hasta que llegue a 9
while jugadas < 9:
    print(f"Turno del jugador {jugador}")

    fila = int(input("Ingrese la fila que desea (0-2):"))
    columna = int(input("Ingrese la columna que desea (0-2):"))

    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Esa posición no se encuentra en el rango, vuelva a colocar su rango")
        continue

    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        jugadas += 1
    else:
        print("Esa casilla ya se encuentra ocupada, vuelva a colocar su rango")
        continue

    #Muestro el tablero completo actualizado
    for fila in tablero:
        for celda in fila:
         print(celda, end=" ")
        print()

    #Cambio de jugador
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"


# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
# • Mostrar el total vendido por cada producto. 
# • Mostrar el día con mayores ventas totales. 
# • Indicar cuál fue el producto más vendido en la semana.

productos = [
    [1, 5, 6, 2, 5, 9, 8],
    [2, 5, 10, 3, 10, 8, 5],
    [6, 2, 5, 7, 5, 1, 5],
    [5, 0, 2, 3, 5, 2, 0]
]
#Muestro la tabla de las ventas de productos
for fila in productos:
        for celda in fila:
         print(celda, end=" ")
        print()

#Muestro el total de las ventas de cada producto
productos_total = []

for i in range(4):
    total = 0
    for j in range (7):
        total += productos[i] [j]
    productos_total.append(total)
    print(f"El total del producto {i+1} es de: {total}")

#Muestro el día con mayores ventas totales
mayor_ventas = 0
dia_mayor = 0

for j in range(7):
    suma_dia = 0
    for i in range(4):
        suma_dia += productos[i][j]
    if suma_dia > mayor_ventas:
        mayor_ventas = suma_dia
        dia_mayor = j

print(f"El día que más se vendió es el día {dia_mayor+1} y el total fue: {mayor_ventas}")

#Muestro el producto más vendido
mas_vendido = 0
producto = 0

for i in range(4):
    if productos_total[i] > mas_vendido:
        mas_vendido = productos_total[i]
        producto = i

print(f"El producto que más se vendió fue el: {producto+1} con {mas_vendido} ventas en la semana.")
