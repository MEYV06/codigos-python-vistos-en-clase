# Version de Python: Las metodos de objeto, incluyendo los metodos instanciados, se han soportado desde la version 1.0 de Python.

# Metodos de Objetos en Python
# Los metodos son funciones que pertenecen a un objeto y generalmente operan sobre el dato del objeto.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Definir un metodo para calcular el area de la circunferencia
    def area(self):
        return 3.14159 * (self.radius**2)

    # Definir una metodo para calcular el perimetro del circulo
    def circumference(self):
        return 2 * 3.14159 * self.radius


# Crear un objeto de la clase Circulo
my_circle = Circle(5)

# Llamar a metodos en el objeto
print('Area of the circle:', my_circle.area())  # Salida: Area del circulo: 78.53975
print('Circumference of the circle:', my_circle.circumference())  # Circunferencia de la circunferencia: 31.4159

# Metodos son similares a las funciones, pero se definen dentro de una clase y se llaman en instancias de esa clase.
# Los metodos operan sobre los atributos del objeto proporcionando comportamiento especifico para ese objeto.
