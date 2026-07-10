# Ejemplo de desempaquetado de diccionarios anidados para una funcion matematica
def calculate_volume(length, width, height):
    return length * width * height

box = {
    'materials': 'carton',
    'dimensions': {
        'length': 10,
        'width': 5,
        'height': 4
    }
}

# Desempaquetando la diccionario 'dimensiones'
volume = calculate_volume(**box['dimensions'])
print('Volume:', volume)  # Salida: Volumen: 200
