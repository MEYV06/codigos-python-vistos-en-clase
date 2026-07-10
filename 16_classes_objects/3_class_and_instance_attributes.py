# Version de Python: Los atributos de clase y de instancia se han soportado desde la version 1.0 de Python.

# Atributos de clase y atributos de instancia
# Un atributo de clase pertenece a la clase y se comparte entre todos los objetos.
# Un atributo de instancia pertenece a cada objeto y puede tener un valor diferente.


class Student:
    school_name = "Escuela de Python"  # Atributo de clase
    total_students = 0  # Otro atributo de clase

    def __init__(self, name, course):
        self.name = name  # Atributo de instancia
        self.course = course  # Atributo de instancia
        Student.total_students += 1


# Crear instancias de la clase Estudiante
student_1 = Student("Ana", "Python Basico")
student_2 = Student("Luis", "Python Intermedio")

# Cada objeto tiene sus propios atributos de instancia
print("Estudiante 1:", student_1.name, "-", student_1.course)
print("Estudiante 2:", student_2.name, "-", student_2.course)
# Salidas:
# Estudiante 1: Ana - Python Basico
# Estudiante 2: Luis - Python Intermedio

# El atributo de clase se comparte entre todos los objetos
print("Escuela compartida:", Student.school_name)
print("Escuela de Ana:", student_1.school_name)
print("Escuela de Luis:", student_2.school_name)
# Salidas:
# Escuela compartida: Escuela de Python
# Escuela de Ana: Escuela de Python
# Escuela de Luis: Escuela de Python

# Cambiar un atributo de instancia afecta solo a ese objeto
student_2.course = "Python Avanzado"

print("Curso de Ana:", student_1.course)
print("Curso actualizado de Luis:", student_2.course)
# Salidas:
# Curso de Ana: Python Basico
# Curso actualizado de Luis: Python Avanzado

# Cambiar un atributo de clase desde la clase afecta a todos los objetos
Student.school_name = "Escuela Pythonista"

print("Nueva escuela de Ana:", student_1.school_name)
print("Nueva escuela de Luis:", student_2.school_name)
# Salidas:
# Nueva escuela de Ana: Escuela Pythonista
# Nueva escuela de Luis: Escuela Pythonista

print("Total de estudiantes:", Student.total_students)
# Salida: Total de estudiantes: 2

# Nota: Usa atributos de instancia para datos propios de cada objeto.
# Usa atributos de clase para datos compartidos por todos los objetos de la clase.
