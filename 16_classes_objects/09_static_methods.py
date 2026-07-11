# Version de Python: Los metodos estaticos existen desde las primeras versiones de Python.

# Metodos estaticos
# Un metodo estatico no recibe self ni cls.
# Se define usando el decorador @staticmethod.
#
# Diferencia rapida:
# metodo normal -> recibe self y trabaja con datos de un objeto.
# @classmethod  -> recibe cls y puede trabajar con datos de la clase.
# @staticmethod -> no recibe cls ni self; solo usa los argumentos que le pasas.


class Student:
    total_students = 0

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hola, soy", self.name)

    @classmethod
    def register_student(cls):
        cls.total_students += 1
        print("Estudiantes registrados:", cls.total_students)

    @staticmethod
    def is_valid_grade(grade):
        return 0 <= grade <= 20

    @staticmethod
    def average(grade_1, grade_2):
        return (grade_1 + grade_2) / 2


# metodo normal: trabaja con un objeto especifico porque usa self.name
student_1 = Student("Ana")
student_1.introduce()

# classmethod: trabaja con la clase porque modifica Student.total_students
Student.register_student()
Student.register_student()

# staticmethod: no trabaja con la clase ni con un objeto.
# Solo usa los valores que recibe como argumentos.
print("Nota valida:", Student.is_valid_grade(18))
print("Promedio:", Student.average(16, 18))

# Salidas:
# Hola, soy Ana
# Estudiantes registrados: 1
# Estudiantes registrados: 2
# Nota valida: True
# Promedio: 17.0

# Nota: Los metodos estaticos se usan cuando la funcion pertenece a la clase,
# pero no necesita acceder a atributos del objeto ni de la clase.
#
# Tambien se puede acceder a un metodo estatico desde un objeto:
# student_1.is_valid_grade(18)
#
# Python lo permite, pero normalmente es mas claro llamarlo desde la clase:
# Student.is_valid_grade(18)
#
# Python prioriza la flexibilidad en vez de prohibir usos que pueden ser confusos.