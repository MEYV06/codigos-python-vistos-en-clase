# La version de Python tiene atributos desde la version 1.0.

# Los atributos en Python
# Los atributos son datos que pertenecen a un objeto.


class Car:
    def __init__(self, make, model, year):
        self.make = make  # Atributo publico
        self.model = model
        self.year = year


# Crear una instancia de la clase Coche
my_car = Car("Toyota", "Corolla", 2020)

# Acceder a los atributos
print('My car is a', my_car.year, my_car.make, my_car.model, '.')
# Mi coche es un Toyota Corolla de 2020.

# Modificando atributos
my_car.year = 2021
print('My car is now a', my_car.year, my_car.make, my_car.model, '.')
# Mi coche ahora es una Toyota Corolla de 2021.

# Nota: Los atributos de los objetos son datos vinculados a instancias especificas.
# Los atributos pueden ser accedidos y modificados directamente, proporcionando flexibilidad en como objetos almacenan y administran datos.
