# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

import sys
sys.setrecursionlimit(20000)

def factorial(num):
    return 1 if num == 0 else num * factorial(num - 1)

def mostrar_factoriales(actual, limite):
    if actual > limite:
        return
    print(f"El factorial de: {actual} es: {factorial(actual)}")
    mostrar_factoriales(actual + 1, limite)

numero = int(input("Ingrese un número para calcular su factorial: "))

mostrar_factoriales(1, numero)

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion-1) + fibonacci(posicion-2)

posicion_num = int(input("Ingrese un número para calcular el valor de la serie de Fibonacci de esa posición: "))

for i in range(posicion_num):
    print(f"En la posición {i} obtenemos el valor de Fibonacci: {fibonacci(i)}")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛**𝑚 = 𝑛 ∗ 𝑛**(𝑚−1). Prueba esta función en un 
# algoritmo general. 

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

calculo = potencia(base, exponente)
print(f"{base} elevado a la potencia: {exponente} es: {calculo}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto.  

def decimal_a_binario(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return decimal_a_binario(num // 2) + str(num % 2)

numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("No se ha ingresado un número positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"El número decimal: {numero} en binario es: {binario}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena 
# de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# - La solución debe ser recursiva.
# - No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra sin espacios ni tildes: ").lower().replace(" ", "")

if es_palindromo(texto):
    print(f"La palabra: '{texto}' es un palíndromo.")
else:
    print(f"La palabra: '{texto}' no es un palíndromo.")

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 
# Restricciones: 
# - No se puede convertir el número a string. 
# - Usá operaciones matemáticas (%, //) y recursión. 

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("El número ingresado no es positivo.")
else:
    print(f"La suma de los dígitos del número: {numero} es: {suma_digitos(numero)}")

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque. 
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
# pirámide. 

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
nivel = int(input("Ingrese la cantidad de bloques del nivel más bajo: "))

if nivel < 1:
    print("Se ha ingresado un número menor a 1. Por lo tanto no hay bloques")
else:
    total = contar_bloques(nivel)
    print(f"La pirámide con: {nivel} bloques en la base, necesita: {total} bloques en total.")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número. 

def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        ultimo = numero % 10
        return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)

numero = int(input("Ingresa un número entero positivo: "))
digito = int(input("Ingrese el dígito a contar (entre 0 y 9): "))

if numero < 0 or digito < 0 or digito > 9:
    print("El valor indicado no es válido.")
else:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito: {digito} aparece {cantidad} veces en el número: {numero}")