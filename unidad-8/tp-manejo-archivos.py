# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

with open("productos.txt", "w") as archivo:
    archivo.write("Cuadernillo,10000,10\n")
    archivo.write("Abrochadora,8000,6\n")
    archivo.write("Resaltadores,6000,8\n")

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato: Producto: Lapicera | Precio: $120.5 | Cantidad: 30

#Utilizando el archivo generado en el ejericicio anterior
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

#Utilizando el archivo .txt generado en el primer ejercicio y la lectura de productos del segundo ejercicio
with open("productos.txt", "a") as archivo:
    nuevo_producto = input("\nIngrese el nombre del nuevo producto: ").title()
    precio_producto = int(input("Ingrese el precio del nuevo producto: "))
    cantidad_producto = int(input("Ingrese la cantidad del nuevo producto: "))
    archivo.write(f"{nuevo_producto},{precio_producto},{cantidad_producto}\n")
    print("Producto agregado con éxito!")

# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.

productos = []

#Utilizando el archivo .txt generado en el primer ejercicio
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")

        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

print("\nLista de los productos: ")
for producto in productos:
    print(f"{producto["nombre"]} | ${producto["precio"]} | {producto["cantidad"]}")

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

#Utilizando la lista del ejercicio anterior
consulta_producto = input("\nIngrese el nombre del producto que desea buscar: ").title()

for producto in productos:
    if producto["nombre"].title() == consulta_producto:
        print("Producto encontrado:")
        print(f"{producto["nombre"]} | ${producto["precio"]} | {producto["cantidad"]}")
        break
else:
    print(f"El producto '{consulta_producto}' no se encuentra en nuestra lista.")

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

#Utilizando el archivo 'productos.txt' ya generado con todas sus actualizaciones
with open("productos.txt", "w") as archivo:
    for producto in productos:
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        archivo.write(linea)

print("\nEl archivo 'productos.txt' ha sido actualizado correctamente.")