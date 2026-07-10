# Version de Python: Los metodos publicos y privados se han usado desde las primeras versiones de Python.

# Metodos publicos y metodos privados
# Un metodo publico se puede llamar directamente desde fuera de la clase.
# Un metodo privado usa doble guion bajo __ para indicar que debe usarse solo dentro de la clase.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Metodo privado: ayuda a otros metodos de la clase
    def __diameter(self):
        return self.radius * 2

    # Metodo publico: se puede llamar desde fuera de la clase
    def area(self):
        return 3.14159 * (self.radius**2)

    # Metodo publico: usa un metodo privado internamente
    def circumference(self):
        return 3.14159 * self.__diameter()


# Crear un objeto de la clase Circulo
my_circle = Circle(5)

# Llamar a metodos publicos desde fuera de la clase
print("Area del circulo:", my_circle.area())
print("Circunferencia del circulo:", my_circle.circumference())
# Salidas:
# Area del circulo: 78.53975
# Circunferencia del circulo: 31.4159

# No se debe llamar a un metodo privado directamente desde fuera de la clase.
# La siguiente linea produciria un AttributeError:
# print(my_circle.__diameter())

# Nota: Los metodos privados sirven para organizar logica interna de la clase.
# En Python, el doble guion bajo ayuda a evitar llamadas accidentales desde fuera de la clase.
