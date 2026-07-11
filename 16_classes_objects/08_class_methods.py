# Version de Python: Los metodos de clase existen desde las primeras versiones de Python.

# Metodos de clase
# Un metodo de clase recibe la clase como primer parametro, normalmente llamado cls.
# Se define usando el decorador @classmethod.


class Student:
    school_name = "Escuela de Python"
    total_students = 0

    @classmethod
    def register_student(cls):
        cls.total_students += 1
        print("Estudiantes registrados:", cls.total_students)

    @classmethod
    def change_school(cls, new_school_name):
        cls.school_name = new_school_name


# Llamar a metodos de clase desde la clase
Student.register_student()
Student.register_student()
Student.change_school("Escuela Pythonista")

print("Escuela:", Student.school_name)
# Salidas:
# Estudiantes registrados: 1
# Estudiantes registrados: 2
# Escuela: Escuela Pythonista

# Nota: Los metodos de clase se usan cuando el metodo necesita trabajar con la clase.
