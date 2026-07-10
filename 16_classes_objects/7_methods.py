# La version de Python: Los metodos han sido una parte integral del modelo orientado a objetos de Python desde la version 1.0.

# Definiendo Varios Metodos en Python
# Los metodos en Python se pueden clasificar en metodos instancia, metodos clase y metodos estaticos.


class MathOperations:
    # Metodo instancia: Operan sobre una instancia de la clase.
    def add(self, x, y):
        return x + y

    # Metodo de clase: opera sobre la clase misma, no sobre instancias.
    @classmethod
    def multiply(cls, x, y):
        return x * y

    # Metodo estatico: ni modifica las instancias, ni la clase.
    @staticmethod
    def subtract(x, y):
        return x - y


# Crear una instancia del cluster Operations.
math_op = MathOperations()

# Llamar a un metodo instancia.
print('Addition:', math_op.add(5, 3))  # Suma: 8

# Llama a un metodo de la clase:
print('Multiplication:', MathOperations.multiply(5, 3))  # Multiplicacion: 15

# Llama a una metodo estatico:
print('Subtraction:', MathOperations.subtract(5, 3))  # Resta: 2

# Nota: Metodos instancia se utilizan para operar sobre atributos de los objetos.
# Metodos de clase operan sobre el objeto mismo y estan marcados con @classmethod.
# Metodos estaticos no modifican la estado del objeto ni del objeto mismo y estan marcados con @staticmethod.
