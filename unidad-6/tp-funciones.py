# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.


# def imprimir_hola_mundo():
#     print("Hola Mundo!")

# imprimir_hola_mundo()





# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.


# def saludar_usuario(nombre):
#     return f"Hola {nombre}!"

# nombre = input("Ingrese su nombre: ")
# saludo = saludar_usuario(nombre)

# print(saludo)



# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.


# def informacion_personal(nombre, apellido, edad, residencia):
#     return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = int(input("Ingrese su edad: "))
# residencia = input("Ingrese su lugar de residencia: ")

# presentacion = informacion_personal(nombre, apellido, edad, residencia)
# print(presentacion)



# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el 
# radio al usuario y llamar ambas funciones para mostrar los resultados.


# import math 
# valor_de_pi = math.pi

# def calcular_area_circulo(radio):
#     return (radio ** 2) * valor_de_pi

# def calcular_perimetro_circulo(radio):
#     return (radio * 2) * valor_de_pi

# radio = float(input("Ingresa el radio para calcular el perímetro y área de un círculo: "))

# area = calcular_area_circulo(radio)
# perimetro = calcular_perimetro_circulo(radio)

# print(f"\nEl radio del círculo es de: {radio}\nEl área es de: {area}\nY el perímetro es de: {perimetro}")
    


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600


