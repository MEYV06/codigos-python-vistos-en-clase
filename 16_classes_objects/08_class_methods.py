# Version de Python: Los metodos de clase existen desde las primeras versiones de Python.

# Metodos de clase
# Un metodo de clase recibe la clase como primer parametro, normalmente llamado cls.
# Se define usando el decorador @classmethod.
#
# Diferencia con un metodo normal:
# metodo normal -> recibe self y puede acceder a atributos del objeto.
# @classmethod   -> recibe cls y puede acceder a atributos de la clase.


class Student:
    school_name = "Escuela de Python"
    total_students = 0

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Estudiante:", self.name)

    @classmethod
    def register_student(cls):
        cls.total_students += 1
        print("Estudiantes registrados:", cls.total_students)

    @classmethod
    def change_school(cls, new_school_name):
        cls.school_name = new_school_name


# Metodo normal: trabaja con un objeto especifico.
# Puede acceder a atributos creados con self, como self.name.
student_1 = Student("Ana")
student_1.introduce()

# Llamar a metodos de clase desde la clase
Student.register_student()
Student.register_student()
Student.change_school("Escuela Pythonista")

print("Escuela:", Student.school_name)

# Evita llamar metodos de clase desde objetos.
# Ejemplo de algo permitido, pero no recomendado:
# student_1.register_student()
# Aunque Python lo permite, en estos ejemplos los llamaremos desde la clase
# porque trabajan con datos de la clase, no con datos de un objeto especifico.
#
# Un metodo de clase no puede acceder directamente a self.name,
# porque recibe cls, no self.

# Salidas:
# Estudiante: Ana
# Estudiantes registrados: 1
# Estudiantes registrados: 2
# Escuela: Escuela Pythonista

# Nota: Los metodos de clase se usan cuando el metodo necesita trabajar con la clase.
# Por claridad, se recomienda llamarlos desde la clase:
# Student.register_student()
