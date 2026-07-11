# TODO 1: crea una lista con numeros del 1 al 10 usando range().
# Luego revisa el valor de numbers para ver la lista creada.
numbers = list(range(1, 11))
# TODO 2: crea una lista con numeros pares del 2 al 20 usando range().
# Luego revisa el valor de even_numbers para ver la lista de pares.
even_numbers = list(range(2, 21, 2))
# TODO 3: crea una lista descendente del 10 al 1 usando range().
# Luego revisa el valor de countdown para ver la cuenta regresiva.
countdown = list(range(10, 0, -1))
# TODO 4: crea una lista con multiplos de 5 desde 5 hasta 50 usando range().
# Luego revisa el valor de multiples_of_five para ver los multiplos.
multiples_of_five = list(range(5, 51, 5))
# TODO 5: obtiene el primer numero de numbers usando indice positivo.
# Luego revisa el valor de first_number para ver el resultado de usar numbers[0].
first_number = numbers[0]
# TODO 6: obtiene el ultimo numero de numbers usando indice negativo.
# Luego revisa el valor de last_number para ver el resultado de usar numbers[-1].
last_number = numbers[-1]
# TODO 7: obtiene los primeros cinco numeros usando slicing.
# Luego revisa el valor de first_five para ver el resultado del slicing.
first_five = numbers[:5]
# TODO 8: suma los numeros del 1 al 10 usando un ciclo for y un acumulador.
# Luego revisa el valor de total para ver la suma final.
total = 0
for n in range(1, 11):
    total += n
# TODO 9: cuenta cuantos numeros pares hay entre 1 y 20 usando range() y len().
# Luego revisa el valor de even_count para ver la cantidad de pares.
even_count = len(range(2, 21, 2))
# TODO 10: recorre range(1, 11) para crear la tabla del 3.
# Dentro del for, crea una variable llamada multiplication_line con textos como:
# "3 x 1 = 3", "3 x 2 = 6", etc.
# Luego revisa el valor de multiplication_line en cada vuelta para ver como cambia.
for i in range(1, 11):
    multiplication_line = f"3 x {i} = {3 * i}"
