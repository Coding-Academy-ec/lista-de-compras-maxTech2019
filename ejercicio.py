# Ingrese una lista de compras: manzanas, plátanos, leche, pan
# Los productos en la lista de compras son: ['manzanas', 'plátanos', 'leche', 'pan']

compras = "manzanas, plátanos, leche, pan"
productos = compras.split(", ")
print(f"Los productos en la lista de compras son: {productos}")

# Convertir la lista de compras en una tupla
def convertir_lista_a_tupla(lista):
    tupla_productos = tuple(lista)
    return tupla_productos

print(convertir_lista_a_tupla(productos))