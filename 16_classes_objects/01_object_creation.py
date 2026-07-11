# La version de Python: Desde la version 1.0 (enero de 1994), Python ha soportado el programacion orientada a objetos.

# Creacion de Objetos en Python
# En Python, los objetos son instancias de clases, que actuan como modelos para crear objetos.


# Definir una clase simple
class Dog:
    # El metodo `__init__` es un metodo especial utilizado para inicializar nuevos objetos.
    def __init__(self, name, age):
        self.name = name  # Asignar atributos al objeto
        self.age = age


# Crear una instancia de la clase Perro
my_dog = Dog("Amigo", 5)

# Accediendo a atributos del objeto
print("My dog's name is", my_dog.name, 'and he is', my_dog.age, 'years old.')
# Salidas: Mi perro se llama Buddy y tiene 5 anos.

# Nota: En Python, todo es un objeto, incluyendo funciones y tipos primitivos basicos.
# Crear objetos desde clases es una concepto fundamental en el programacion orientada a objetos de Python.
