# Version de Python: Los metodos estaticos existen desde las primeras versiones de Python.

# Metodos estaticos
# Un metodo estatico no recibe self ni cls.
# Se define usando el decorador @staticmethod.


class Student:
    @staticmethod
    def is_valid_grade(grade):
        return 0 <= grade <= 20

    @staticmethod
    def average(grade_1, grade_2):
        return (grade_1 + grade_2) / 2


# Llamar a metodos estaticos desde la clase
print("Nota valida:", Student.is_valid_grade(18))
print("Promedio:", Student.average(16, 18))
# Salidas:
# Nota valida: True
# Promedio: 17.0

# Nota: Los metodos estaticos se usan cuando la funcion pertenece a la clase,
# pero no necesita acceder a atributos del objeto ni de la clase.
