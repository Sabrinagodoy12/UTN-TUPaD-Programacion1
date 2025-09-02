# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for i in range(101):
#     print(i)





# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# num = int(input("Ingrese un número entero: "))
# cantidad = 0

# while num > 0:
#     cantidad += 1
#     num = num // 10

# print(f"EL número ingresador tiene: {cantidad} de dígitos")



# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# num1 = int(input("Ingrese un número: "))
# num2 = int(input("Ingrese otro número: "))
# suma = 0

# if num1 > num2 :
#     for i in range(num2+1, num1):
#         suma = suma + i
#         print(f"{num2} + {i} = {suma}")
# elif  num1 < num2:
#     for i in range(num1+1, num2):
#         suma = suma + i
#         print(f"{num1} + {i} = {suma}")




# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# corte = 0
# suma = 0

# num = int(input(f"Ingrese un número mayor a cero: (Si desea salir ingrese: {corte}) "))

# while num != corte :
#     suma += num
#     num = int(input("Ingrese otro número"))

# if suma != 0:
#     print(f"El total acumulado de los números ingresados es: {suma}")
# else:
#     print("No ha ingresado ningún número")




# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# import random 
# numero_aleatorio = random.randint(0, 9)
# intento = 0
# num = 10

# while num != numero_aleatorio :
#     if intento == 0 :
#      num = int(input("Ingrese un número entre el 0 y el 9 para adivinar el número aleatorio: "))
#      intento +=1
#     else:
#       num = int(input("El número es incorrecto ¡Vuelve a intentarlo con otro número!: "))
#       intento += 1

# print(f"¡Felicidades! Acertaste el número aleatorio: {numero_aleatorio} en el intento: {intento}")







# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# for i in range(100, 0, -2):
#     print(i)




# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.