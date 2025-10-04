# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre)

print(saludo)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")

presentacion = informacion_personal(nombre, apellido, edad, residencia)
print(presentacion)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el 
# radio al usuario y llamar ambas funciones para mostrar los resultados.

import math 
valor_de_pi = math.pi

def calcular_area_circulo(radio):
    return (radio ** 2) * valor_de_pi

def calcular_perimetro_circulo(radio):
    return (radio * 2) * valor_de_pi

radio = float(input("Ingresa el radio para calcular el perímetro y área de un círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"\nEl radio del círculo es de: {radio}\nEl área es de: {area}\nY el perímetro es de: {perimetro}")
    
# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos que desea pasar a horas: "))
cantidad_horas = segundos_a_horas(segundos)

print(f"{segundos} segundos, son {cantidad_horas} horas")

#  6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#  número como parámetro y imprima la tabla de multiplicar de ese
#  número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{i} * {numero} = {resultado}")

num = int(input("Ingrese un número para ver su tabla de multiplicar: "))

tabla_multiplicar(num)

#  7. Crear una función llamada operaciones_basicas(a, b) que reciba
#  dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    multiplicar = a * b
    resta = a - b
    if (b!= 0):
        division = a / b
    else:
        division = None

    return(suma, resta, multiplicar, division)

a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número:"))

suma, resta, multiplicar, division = operaciones_basicas(a, b)

print(f"{a} + {b} = {suma}")
print(f"{a} - {b} = {resta}")    
print(f"{a} * {b} = {multiplicar}")
if division is not None:
    print(f"{a} / {b} = {division}")  
else:
    print("División: No se puede dividir por cero")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#  peso en kilogramos y la altura en metros, y devuelva el índice de
#  masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales

def calcular_imc(peso, altura):
    return peso / (altura)**2

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"El índice de masa corporal con la altura de: {altura}m y el peso de: {peso}kg es IMC = {imc: .2f}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return celsius * (9/5) + 32

celsius = float(input("Ingrese una temperatura en Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)
print(f"Su temperatura en grados Celsius de {celsius}° es {fahrenheit} °F ")

#  10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#  tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta
#  función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese un número: "))
b = float(input("Ingrese otro número: "))
c = float(input("Ingrese el último número: "))

promedio = calcular_promedio(a, b, c)
print(f"Los números ingresados: {a} | {b} | {c}\nPromedio: {promedio: .2f}")
