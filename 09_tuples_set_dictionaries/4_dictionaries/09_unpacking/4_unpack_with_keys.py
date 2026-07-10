# Desempaquetar claves especificas de un diccionario con ** para una funcion matematica
def calculate_force(mass, acceleration):
    return mass * acceleration

data = {'mass': 60, 'acceleration': 9.8, 'friction': 0.3}

# Crear un nuevo diccionario con solo las claves necesarias
physics_data = {key: data[key] for key in ['mass', 'acceleration']}

# Desempaquetando el diccionario filtrado
force = calculate_force(**physics_data)
print('Force:', force)  # Force: 588.0
