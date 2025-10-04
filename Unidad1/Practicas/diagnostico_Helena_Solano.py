#Diagnostico_nombre.py
#Simulador de pedidos
#Conceptos basicos: variables, inputs, condicionales, funciones y bucles

#Elegir una tematica de tienda y escribir 3 productos
productos = ["Fresa", "Chocolate", "Vainilla"]
precios = [30, 34, 38]

#Funcion para calcular total
def calcular_total(cantidad, precios):
    total=0
    for i in range (len(cantidad)):
        total += cantidad [i] * precios [i]
    return total

#Menu para usuario (Outpus)
print("Menu de nieves Bienvenido")
nombre = (input("Ingresa tu nombre: "))
cantidad = []
for i in range (len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]}")
    cantidad_add = int(input(f"¿Cuántos helados de {productos[i]} desea? "))
    cantidad.append(cantidad_add)

total = calcular_total(cantidad, precios)

print("--RESUMEN DE LA COMPRA--")
print(f"Cliente: {nombre}")
for i in range (len(productos)):
    if cantidad[i] > 0:
        print(f"{cantidad[i]} {productos[i]} - ${cantidad[i] * precios[i]}")
print(f"Total a pagar: ${total}")