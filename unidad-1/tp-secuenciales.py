# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  

print("Hola mundo")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
# realizar la impresión por pantalla. 

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")


# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
# la impresión por pantalla. 

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro. 

radio = float(input("Ingrese el radio de un círculo: "))
area = 3.14159 * (radio ** 2)
perimetro =  2 *  3.14159 * radio

print(f"El círculo con radio de: {radio} tiene un área de: {area} y un perímetro de: {perimetro}")


# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
# cuántas horas equivale. 

segundos = float(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600

print(f"Los segundos: {segundos} equivalen a {horas} horas.")


# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número.  

numero = int(input("Ingrese un número para calcular su tabla de multiplicar: "))

print(f"Tabla de multiplicar del número {numero}: 1x{numero} = {numero*1} | 2x{numero} = {numero*2} | 3x{numero} = {numero*3} | 4x{numero} = {numero*4} | 5x{numero} = {numero*5} | 6x{numero} = {numero*6} | 7x{numero} = {numero*7} | 8x{numero} = {numero*8} | 9x{numero} = {numero*9} | 10x{numero} = {numero*10} ")


# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

num1 = int(input("Ingrese un número entero distinto a cero: "))
num2 = int(input("Ingrese otro número entero distinto a cero: "))

print(f"Resultado de los números ingresados: Suma = {num1 + num2} | División = {num1/num2} | Multiplicación = {num1*num2} | Resta = {num1-num2}")


# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal. IMC = peso en kg / (altura en m)2

altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))

imc = peso / (altura)**2

print(f"El índice de masa corporal con la altura de: {altura}m y el peso de: {peso}kg es de IMC = {imc}")


# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
# pantalla su equivalente en grados Fahrenheit. 

celsius = float(input("Ingrese una temperatura en Celsius: "))
fahrenheit = celsius * (9/5) + 32

print(f"Su temperatura en grados Celsius de {celsius}° es {fahrenheit} °F ")


#  10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
# dichos números. 

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
num3 = int(input("Ingrese otro número: "))

promedio = (num1 + num2 + num3)/3

print(f"El promedio de los números: {num1}, {num2}, {num3} es: {promedio}")