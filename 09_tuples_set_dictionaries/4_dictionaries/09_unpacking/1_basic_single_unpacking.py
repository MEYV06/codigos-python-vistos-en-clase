# Ejemplo de desempaquetar un solo diccionario con ** para una funcion matematica
def calculate_area(length, width):
    return length * width

# ¿Hay algun error?
dimensions = {'longitud': 10, 'ancho': 5}

# Desempaquetando el diccionario en argumentos de la funcion
area = calculate_area(**dimensions)
print('Area:', area)  # Area: 50
