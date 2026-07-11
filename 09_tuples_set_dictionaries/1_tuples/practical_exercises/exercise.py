# TODO 1: crea una tupla llamada student con "Ana", 18 y "Python".
# Luego revisa el valor de student para ver la tupla creada.
student = ("Ana", 18, "Python")
# TODO 2: desempaqueta student en student_name, student_age y student_course.
# Luego revisa el valor de student_name, student_age y student_course.
student_name, student_age, student_course = student
# TODO 3: crea una tupla llamada scores con 15, 18, 20, 17 y 19.
# Luego revisa el valor de scores para ver la tupla de notas.
scores = (15, 18, 20, 17, 19)
# TODO 4: obtiene la primera nota usando indice positivo.
# Luego revisa el valor de first_score para ver el resultado de usar scores[0].
first_score = scores[0]
# TODO 5: obtiene la ultima nota usando indice negativo.
# Luego revisa el valor de last_score para ver el resultado de usar scores[-1].
last_score = scores[-1]
# TODO 6: obtiene las notas centrales usando slicing.
# Luego revisa el valor de middle_scores para ver el resultado del slicing.
middle_scores = scores[1:-1]
# TODO 7: usa desempaquetado extendido para separar la primera nota, las notas del medio y la ultima nota.
# Luego revisa el valor de first_grade, other_grades y final_grade.
first_grade, *other_grades, final_grade = scores
# TODO 8: crea una tupla anidada llamada points con (10, 20) y (30, 40).
# Luego revisa el valor de points para ver la tupla anidada.
points = ((10, 20), (30, 40))
# TODO 9: desempaqueta points en first_x, first_y, second_x y second_y.
# Luego revisa el valor de first_x, first_y, second_x y second_y.
(first_x, first_y), (second_x, second_y) = points
# TODO 10: crea una tupla llamada products con pares de producto y precio.
# Usa ("lapiz", 2.5), ("cuaderno", 8.0) y ("regla", 3.0).
# Luego revisa el valor de products para ver la tupla de pares.
products = (("lapiz", 2.5), ("cuaderno", 8.0), ("regla", 3.0))
# TODO 11: crea una lista vacia llamada formatted_products.
# Luego revisa el valor de formatted_products para ver que empieza vacia.
formatted_products = []
# TODO 12: recorre products desempaquetando product_name y price.
# Dentro del for, crea product_summary con textos como "lapiz cuesta 2.5".
# Agrega product_summary a formatted_products.
# Luego revisa el valor de product_summary en cada vuelta y formatted_products al final.
for product_name, price in products:
    product_summary = f"{product_name} cuesta {price}"
    formatted_products.append(product_summary)
# TODO 13: crea una funcion get_min_max que reciba grades y retorne la menor y la mayor nota.
# Luego usa la funcion en el siguiente TODO.
def get_min_max(grades):
    return min(grades), max(grades)
# TODO 14: llama get_min_max(scores) y desempaqueta el resultado en min_score y max_score.
# Luego revisa el valor de min_score y max_score.
min_score, max_score = get_min_max(scores)
# TODO 15: crea dos variables left y right con "rojo" y "azul".
# Luego revisa el valor de left y right antes del intercambio.
left = "rojo"
right = "azul"
# TODO 16: intercambia left y right usando desempaquetado de tuplas.
# Luego revisa el valor de left y right despues del intercambio.
left, right = right, left
