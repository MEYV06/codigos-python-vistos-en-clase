# La version de Python ha soportado la comparacion de objetos desde la version 1.0.

# Comparacion de Objetos en Python
# Los objetos pueden ser comparados usando los operadores de comparacion como ==, !=, <, >, etc.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Sobreescribir el metodo __eq__ para comparar libros basandose en su titulo y autor
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False


# Crear dos objetos libro
book1 = Book("1984", "George Orwell")
book2 = Book("1984", "George Orwell")
book3 = Book("El Gran Maquiavellismo", "Aldous Huxley")

# Comparando objetos
print('book1 is equal to book2:', book1 == book2)  # Salida: libro1 es igual a libro2: True
print('book1 is equal to book3:', book1 == book3)  # Salida: libro1 es igual a libro3: False

# Nota: La comparacion de objetos en Python puede ser personalizada cambiando los metodos magicos de comparaion como __eq__ y __lt__.
# Este permite comparar objetos basandose en sus atributos, lo cual permite comparaciones mas significativas.
