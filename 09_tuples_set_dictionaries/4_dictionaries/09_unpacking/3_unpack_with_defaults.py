# Desempaquetar con valores por defecto usando ** para una funcion matematica
def calculate_circle_area(radius, pi=3.14159):
    return pi * radius ** 2

circle = {'radius': 7}

# Desempaquetando el diccionario con valor predeterminado para pi
area = calculate_circle_area(**circle)
print('Circle Area:', area)  # Circulo Area: 153.93804


################################################


# Ejemplo de combinar desempaquetado con otras operaciones para una funcion matematica
def calculate_pressure(force, area=1):
    return force / area

data = {'force': 500}

# Desempaquetar y sumar un valor predeterminado de area
pressure = calculate_pressure(**data, area=50)
print('Pressure:', pressure)  # Salida: Presion: 10.0
