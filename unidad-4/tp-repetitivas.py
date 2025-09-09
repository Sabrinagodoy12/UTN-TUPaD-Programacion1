# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = int(input("Ingrese un número entero: "))
cantidad = 0

while num > 0:
    cantidad += 1
    num = num // 10

print(f"EL número ingresado tiene: {cantidad} de dígitos")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
suma = 0

if num1 > num2 :
    for i in range(num2+1, num1):
        suma = suma + i
        print(f"{num2} + {i} = {suma}")
elif  num1 < num2:
    for i in range(num1+1, num2):
        suma = suma + i
        print(f"{num1} + {i} = {suma}")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

corte = 0
suma = 0

num = int(input(f"Ingrese un número mayor a cero: (Si desea salir ingrese: {corte}) "))

while num != corte :
    suma += num
    num = int(input("Ingrese otro número"))

if suma != 0:
    print(f"El total acumulado de los números ingresados es: {suma}")
else:
    print("No ha ingresado ningún número")


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random 
numero_aleatorio = random.randint(0, 9)
intento = 0
num = 10

while num != numero_aleatorio :
    if intento == 0 :
     num = int(input("Ingrese un número entre el 0 y el 9 para adivinar el número aleatorio: "))
     intento +=1
    else:
      num = int(input("El número es incorrecto ¡Vuelve a intentarlo con otro número!: "))
      intento += 1

print(f"¡Felicidades! Acertaste el número aleatorio: {numero_aleatorio} en el intento: {intento}")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, 0, -2):
    print(i)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

suma = 0
num = int(input("Ingrese un número entero positivo: "))

if num > 0: 
    for i in range(num+1):
     suma += i
    print(f"La suma total de los números del 0 al {num} es: {suma}")
elif num == 0:
   print("El número ingresado es 0, por lo que el total es 0")
else:
   print("No ingresó un número positivo")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

rango = 0
contador_par = 0
contador_impar = 0
contador_negativos = 0
contador_positivo = 0

while rango < 100 :
    num = int(input("Ingrese un número entero: "))
    rango += 1
    if num % 2 == 0:
        contador_par += 1
    else :
        contador_impar += 1
    if num < 0:
        contador_negativos += 1
    elif num > 0:
        contador_positivo += 1

print(f"Ingresaste {contador_positivo} números positivos, {contador_negativos} números negativos, {contador_impar} números impares y {contador_par} números pares.")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

rango = 0
contador = 0
suma = 0

for i in range(100):
    num = int(input("Ingrese un número entero: "))
    contador += 1
    suma += num
    print(contador)

media = suma / contador
print(f"La media de los números ingresados es: {media}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

invertido = 0
num = int(input("Ingrese un número para invertirlo: "))

signo = "-" if num < 0 else ""
num = abs(num)

while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10

print(f"El número invertido es {signo}{invertido}")
        
