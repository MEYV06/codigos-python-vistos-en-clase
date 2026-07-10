# Desempaquetar multiples diccionarios con ** para una funcion matematica
def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

mass_data = {'mass': 70}
velocity_data = {'velocity': 15}

# combinar diccionarios con **
# si hay claves duplicadas, la ultima se utilizara
combined_data = {**mass_data, **velocity_data}

# Desempaquetando el diccionario combinado
ke = calculate_kinetic_energy(**combined_data)
print('Kinetic Energy:', ke)  # Kinetic Energy: 7875.0
