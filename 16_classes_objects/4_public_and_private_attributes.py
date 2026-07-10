# Version de Python: Los atributos publicos y privados se han usado desde las primeras versiones de Python.

# Atributos publicos y atributos privados
# Un atributo publico se puede acceder directamente desde fuera de la clase.
# Un atributo privado usa doble guion bajo __ para indicar que debe usarse solo dentro de la clase.


class Car:
    def __init__(self, make, model, year):
        self.make = make  # Atributo publico
        self.model = model  # Atributo publico
        self.__year = year  # Atributo privado

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year


# Crear una instancia de la clase Coche
my_car = Car("Toyota", "Corolla", 2020)

# Acceder a atributos publicos directamente
print("Marca:", my_car.make)
print("Modelo:", my_car.model)
# Salidas:
# Marca: Toyota
# Modelo: Corolla

# Acceder a un atributo privado usando un metodo de la clase
print("Ano:", my_car.get_year())
# Salida: Ano: 2020

# Modificar un atributo publico directamente
my_car.model = "Yaris"
print("Nuevo modelo:", my_car.model)
# Salida: Nuevo modelo: Yaris

# Modificar un atributo privado usando un metodo de la clase
my_car.set_year(2021)
print("Nuevo ano:", my_car.get_year())
# Salida: Nuevo ano: 2021

# No se debe acceder a un atributo privado directamente desde fuera de la clase.
# La siguiente linea produciria un AttributeError:
# print(my_car.__year)

# Nota: En Python, los atributos privados no son privados de forma absoluta.
# El doble guion bajo ayuda a evitar accesos accidentales desde fuera de la clase.
