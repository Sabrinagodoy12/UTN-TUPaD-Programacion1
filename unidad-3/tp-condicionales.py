# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

edad = int(input("Ingrese su edad: "))
if edad > 18 :
    print("Es mayor de edad")


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
# mensaje “Desaprobado”. 

nota = int(input("Ingrese su nota: "))

if nota >= 6 :
    print("Aprobado")
else : 
    print("Desaprobado")


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
# operador de módulo (%) en Python para evaluar si un número es par o impar. 

num = int(input("Ingrese un número: "))

if num % 2 == 0 :
    print("Ha ingresado un número par")
else : 
    print("Por favor, ingrese un número par")


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad < 12 :
    print("Usted pertenece a la categoría: Niño/a.")
elif edad >= 12 and edad < 18:
    print("Usted pertenece a la categoría: Adolescente.")
elif edad >= 18 and edad < 30:
    print("Usted pertenece a la categoría: Adulto/a joven.")
else:
    print("Usted pertenece a la categoría: Aulto/a")


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 

contrasenia = input("Ingrese su contraseña: ")

if len(contrasenia) >= 8 and len(contrasenia) <= 14 :
    print("Ha ingresado una contraseña correcta")
else :
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6) escribir un programa que tome la lista 
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 

from statistics import mode, median, mean 
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

media = mean(numeros_aleatorios)
moda =  mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)

if (media > mediana) and (mediana > moda) :
    print("Sesgo positivo o a la derecha")
elif (media < mediana) and (mediana < moda) :
    print ("Sesgo negativo o a la izquierda")
else :
   print("Sin sesgo")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla.
 
palabra = input("Ingrese una palabra: ")
ultima_letra = palabra[-1].lower()

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u" :
    print(f"{palabra}!")
else :
    print(palabra)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas. 

nombre = input("Ingrese su nombre: ")
num = int(input("Ingrese el número de la opción que desea: \n 1- Si quiere su nombre en mayúsculas. \n 2- Si quiere su nombre en minúsculas. \n 3- Si quiere su nombre con la primera letra mayúscula. "))

if num == 1 :
    print(nombre.upper())
elif num == 2 :
    print(nombre.lower())
elif num == 3 :
    print(nombre.title())
else :
    print("La opción ingresada no es válida.")


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
# por pantalla: 
# ● Menor que 3: "Muy leve" (imperceptible). 
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
# generalmente no causa daños). 
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
# débiles). 
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

terremoto = int(input("Ingrese la magnitud del terremoto: "))

if terremoto < 3 :
    print("El terremoto recibe la clasificación de: Muy leve")
elif terremoto >= 3 and terremoto < 4 :
    print("El terremoto recibe la clasificación de: Leve")
elif terremoto >= 4 and terremoto < 5 :
    print("El terremoto recibe la clasificación de: Moderado")
elif terremoto >= 5 and terremoto < 6 :
    print("El terremoto recibe la clasificación de: Fuerte")
elif terremoto >= 6 and terremoto < 7 :
    print ("El terremoto recibe la clasificación de: Muy fuerte")
else :
    print("El terremoto recibe la clasificación de: Extremo")


# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
# del año es y qué día es. El programa deberá utilizar esa información (tabla dada en el ejercicio) para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano. 

hemisferio = input("Ingrese en qué hemisferio se encuentra: N/S").lower()
mes = input("Indique en qué mes se encuentra: ").lower()
dia = int(input("Indique en qué día se encuentra:"))

if hemisferio == "n" :
    if  mes == "enero" or mes == "febrero" :
        print ("Se encuentra en Invierno")
    elif (mes == "diciembre" and dia >= 21 )or (mes == "marzo" and dia <= 20):
        print("Se encuentra en Invierno")
    elif mes == "abril" or mes == "mayo" :
          print ("Se encuentra en Primavera")
    elif (mes == "marzo" and dia >= 21) or (mes == "junio" and dia <= 20):
          print ("Se encuentra en Primavera")
    elif mes == "julio" or mes == "agosto":
          print ("Se encuentra en Verano")
    elif (mes == "junio" and dia >= 21) or (mes == "septiembre" and dia <= 20):
          print ("Se encuentra en Verano")
    elif mes == "octubre" or mes == "noviembre" :
          print ("Se encuentra en Otoño")
    elif (mes == "septiembre" and dia >= 21) or (mes == "diciembre" and dia <= 20):
          print ("Se encuentra en Otoño")

elif hemisferio == "s":
     if mes == "enero" or mes == "febrero":
         print ("Se encuentra en Verano")
     elif (mes == "diciembre" and dia >= 21 )or (mes == "marzo" and dia <= 20):
        print("Se encuentra en Verano")
     elif mes == "abril" or mes == "mayo" :
          print ("Se encuentra en Otoño")
     elif (mes == "marzo" and dia >= 21) or (mes == "junio" and dia <= 20):
          print ("Se encuentra en Otoño")
     elif mes == "julio" or mes == "agosto":
          print ("Se encuentra en Invierno")
     elif (mes == "junio" and dia >= 21) or (mes == "septiembre" and dia <= 20):
          print ("Se encuentra en Invierno")
     elif mes == "octubre" or mes == "noviembre" :
          print ("Se encuentra en Primavera")
     elif (mes == "septiembre" and dia >= 21) or (mes == "diciembre" and dia <= 20):
          print ("Se encuentra en Primavera")
