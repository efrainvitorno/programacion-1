# Definir las funciones de descuento
def DescuentoMenor(producto, valor, descuento):
    nombre, precio = producto
    if precio < valor:
        return nombre, precio - descuento
    return nombre, precio

def DescuentoFijo(producto, descuento):
    nombre, precio = producto
    return nombre, precio - descuento

def descuentoPorcentaje(producto, valor, porcentaje):
    nombre, precio = producto
    if precio > valor:
        return nombre, precio * (1 - porcentaje / 100)
    return nombre, precio

# Función principal
# args es una abreviatura de "arguments" (para listas)
def AplicarDescuentos(productos, delegado_descuento, *args):
    productos_descuento = [delegado_descuento(producto, *args) for producto in productos]
    return productos_descuento

# Lista de productos
productos = [("Camiseta", 20.99), ("Pantalón", 34.95), ("Zapatos", 49.99), ("Gorra", 12.50), ("Bufanda", 15.75)]

# Solicitar al usuario los detalles del descuento
print("Seleccione el tipo de descuento:")
print("1. Descuento para productos cuyo costo sea menor que un valor dado")
print("2. Descuento fijo para todos los productos")
print("3. Descuento por porcentaje en productos mayores a un valor dado")
opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion == 1:
    valor = float(input("Ingrese el valor límite para aplicar el descuento: "))
    descuento = float(input("Ingrese el monto del descuento: "))
    ProductoDescuento = AplicarDescuentos(productos, DescuentoMenor, valor, descuento)
    print('===================================================')
    print(f"Descuentos menores a {valor} con descuento de {descuento}:")
    
    print('===================================================')
elif opcion == 2:
    descuento = float(input("Ingrese el monto del descuento fijo: "))
    ProductoDescuento = AplicarDescuentos(productos, DescuentoFijo, descuento)
    print('===================================================')
    print(f"Descuento fijo de {descuento} en todos los productos:")
    print('===================================================')
elif opcion == 3:
    valor = float(input("Ingrese el valor límite para aplicar el descuento: "))
    porcentaje = float(input("Ingrese el porcentaje de descuento: "))
    ProductoDescuento = AplicarDescuentos(productos, descuentoPorcentaje, valor, porcentaje)
    print('===================================================')
    print(f"Descuento de {porcentaje}% para productos mayores a {valor}:")
    print('===================================================')
else:
    print("Opción no válida")
    ProductoDescuento = []

# Mostrar resultados
# ulizaremos Zip para combinar las 2 listas 
print('===================================================')
print("Lista final de productos con precios originales y precios con descuento:")
print('===================================================')
for ProductoOriginal, ProductoDescuento in zip(productos, ProductoDescuento):
    NombreOriginal, PrecioOriginal = ProductoOriginal
    _, PrecioDescuento = ProductoDescuento
    print(f"Producto: {NombreOriginal}, Precio Original: {PrecioOriginal:.2f}, Precio con Descuento: {PrecioDescuento:.2f}")
print('===================================================')
