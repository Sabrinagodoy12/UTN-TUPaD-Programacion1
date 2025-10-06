# 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
print(f"El diccionario sin modificaciones:\n{precios_frutas}")

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(f"\nEl diccionario con modificiaciones:\n{precios_frutas}")

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800 

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(f"\nEl diccionario con precios actualizados:\n{precios_frutas}")

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios. 

frutas = list(precios_frutas.keys())
print(f"\nLista solo con las frutas:\n{frutas}")

# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe. 

contactos = {}

for i in range(5):
    nombre = input("\nIngrese el nombre del contacto que desea agregar: ").title()
    telefono = int(input("Ingrese el número de teléfono de ese contacto: "))
    contactos[nombre] = telefono

print(f"\nLista de contactos:\n{contactos}")

consulta = input("\nIngrese el nombre del contacto que desea buscar: ").title()

if consulta in contactos:
    print(f"El número del contacto: {consulta} es: {contactos[consulta]}")
else:
    print(f"{consulta} no se encuentra en sus contactos.")


# 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")
palabras = frase.split()

palabras_unicas = set(palabras)
print(f"\nLas palabras únicas de la frase son:\n{palabras_unicas}")

contador_palabras = {}

for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print(f"\nCantidad de veces que aparece cada palabra:\n{contador_palabras}")


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno.

alumnos = {}
for i in range(3):
    nombre = input(f"\nIngresa el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingresá la nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

print("\nPromedio de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")


# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {10, 11, 15, 17, 40}
parcial2 = {15, 40, 32, 25}

ambos = parcial1 & parcial2
print(f"\nAprobaron ambos parciales: {ambos}")

solo_uno = parcial1 ^ parcial2
print(f"\nAprobaron al menos un parcial: {solo_uno}")

al_menos_uno = parcial1 | parcial2
print(f"\nAprobaron al menos uno de los parciales: {al_menos_uno}")


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe. 

productos = {'Llavero': 2, 'Agenda': 7, 'Cuadernillo': 9, 'Abrochadora': 4, 'Resaltadores': 10}
print(f"\nNuestros productos\n{list(productos.keys())}")

#Consulta el stock de un producto ingresado
consulta_stock = input("\nIngresa el nombre del producto por el que deseas consultar: ").title()

if consulta_stock in productos:
    print(f"\nEl stock del producto: {consulta_stock} es de: {productos[consulta_stock]}")

#Agrega unidades al stock si existe el producto
print(f"\nNuestros productos con su stock actual: {productos}")
consulta_unidades = input("\nIngresa el producto al que desea agregar unidades: ").title()

if consulta_unidades in productos:
    cantidad = int(input("\nIngresa la cantidad que desea agregarle al producto: "))
    productos[consulta_unidades] += cantidad
    print(f"\nAhora el producto '{consulta_unidades}' tiene: {productos[consulta_unidades]} unidades disonibles.")
else:
    print(f"\nEl producto '{consulta_unidades}' no existe en nuestro listado.")

#Agregar un nuevo producto que no exista
producto_nuevo = input("\nIngrese el nuevo producto que desea agregar: ").title()

if producto_nuevo in productos:
    print(f"\nEl producto '{producto_nuevo}' ya se encuentra en nuestra lista.")
else:
    consulta_cantidad = int(input(f"Ingrese la cantidad que desea agregarle a {producto_nuevo}: "))
    productos[producto_nuevo] = consulta_cantidad
    print(f"\nEl producto {producto_nuevo} con su stock de: {consulta_cantidad} unidades, ha sido agregado con éxito\n")
    print(productos)

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Permití consultar qué actividad hay en cierto día y hora. 

agenda = {
    ("lunes", "10:00"): "Reunión laboral",
    ("lunes", "18:00"): "Turno al médico",
    ("viernes", "19:30"): "Clase de inglés",
    ("viernes", "18:00"): "Gimnasio",
    ("sabado", "18:00"): "Merienda con amiga"
}

print("\nDías y horarios agendados:")
for dia, hora in agenda.keys():
    print(f"- {dia} a las {hora}")

dia = input("\nIndica el día por el que deseas consultar la actividad agendada: ").lower()
hora = input("Indica qué horario deseas consultar la actividad agendada (formato: 00:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"\nActividad programada el {dia} a las {hora}: {agenda[clave]}")
else:
    print(f"\nNo hay actividades programadas el {dia} a las {hora}.")


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores. 

original = {"Argentina": "Buenos Aires", "Perú": "Lima", "Estados unidos": "Washington D.C.", "Colombia": "Bogotá", "Brasil": "Brasilia"}
invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print(f"\nDiccionario original: {original}\nDiccionario invertido: {invertido}")
