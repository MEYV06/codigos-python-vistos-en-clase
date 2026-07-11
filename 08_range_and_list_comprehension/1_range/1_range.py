# Python Version: La funcion range() fue introducida en Python 1.0 (January 1994).
# Fue modificada en Python 3.0 (December 2008) para comportarse como la
# xrange() de Python 2.

# Introduccion a range() en Python
# ---------------------------------
# La funcion range() en Python es una funcion (function) integrada que genera una secuencia de numeros.
# En versiones anteriores de Python (2.x), habia dos funciones: range() y xrange().
# - range() generaba una lista de numeros de una sola vez en memoria.
# - xrange() generaba numeros uno a uno segun se necesitaban, sin almacenar toda la secuencia en memoria.

# A partir de Python 3.0, la funcion range() fue actualizada para combinar los beneficios de ambas:
# - Ahora se comporta como la antigua xrange() generando numeros bajo demanda.
# - Esto la hace mucho mas eficiente en memoria, especialmente para secuencias grandes.

# La funcion range() devuelve un tipo de secuencia inmutable llamado "range object" (objeto range).
# Este objeto range se comporta como una secuencia (similar a listas o tuplas) pero en realidad no crea una lista de numeros.
# En su lugar, genera cada numero sobre la marcha a medida que iteras sobre el,
# lo que ahorra memoria.

# Caracteristicas del objeto range:
# - Inmutable (Immutable): Una vez creada, la secuencia no se puede modificar.
# - Eficiente (Efficient): Genera numeros solo cuando se necesitan, lo que lo hace adecuado para rangos grandes.
# - Indexable (Indexable): Puedes acceder a elementos en el range usando indexacion, igual que con las listas.
# - Soporta slicing (slicing): Puedes hacer slicing del range para crear un nuevo objeto range con un subconjunto de la secuencia original.

# La funcion range() se usa comunmente en bucles for (for-loops) para iterar sobre una
# secuencia de numeros.

# Ejemplo 1: Usando range() para generar una secuencia de numeros del 0 al 4
sequence = range(5)
# Salida (output): Secuencia del 0 al 4: [0, 1, 2, 3, 4]
print('Secuencia del 0 al 4:', list(sequence))

# Ejemplo 2: Usando range() con un parametro de inicio y fin
# Genera una secuencia del 1 al 5 (el valor de fin no se incluye)
sequence = range(1, 6)
# Salida (output): Secuencia del 1 al 5: [1, 2, 3, 4, 5]
print('Secuencia del 1 al 5:', list(sequence))

# Ejemplo 3: Usando range() con un parametro de paso (step)
# Genera una secuencia del 0 al 10 con un paso de 2
sequence = range(0, 11, 2)
# Salida (output): Secuencia del 0 al 10 con paso de 2: [0, 2, 4, 6, 8, 10]
print('Secuencia del 0 al 10 con paso de 2:', list(sequence))

# Ejemplo 4: Usando un parametro de paso negativo para generar una secuencia en reversa
# Genera una secuencia del 10 al 1
sequence = range(10, 0, -1)
# Salida (output): Secuencia del 10 al 1: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print('Secuencia del 10 al 1:', list(sequence))

# Ejemplo 5: Recorriendo un range en un bucle for (for-loop)
# Imprime cada numero del 0 al 4
for i in range(5):
    print('Numero:', i)
# Salida (output):
# Numero: 0
# Numero: 1
# Numero: 2
# Numero: 3
# Numero: 4

# Nota: range() en Python 3 no crea una lista en memoria, sino un tipo de secuencia inmutable (immutable sequence type),
# lo que significa que es eficiente en memoria incluso para rangos grandes.

# Ejemplo 6: Convirtiendo un range a una lista explicitamente
# Genera una lista de numeros del 1 al 10
numbers_list = list(range(1, 11))
# Salida (output): Lista de numeros del 1 al 10: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Lista de numeros del 1 al 10:', numbers_list)

# Resumen:
# - range() en Python 3.x es una forma poderosa y eficiente en memoria de generar secuencias de numeros.
# - Se comporta de manera similar a la antigua xrange() de Python 2.x, pero con los beneficios adicionales de una interfaz mas unificada y consistente.
# - Se usa comunmente en bucles y es especialmente util cuando se trabaja con secuencias grandes de numeros.



##Resolucion:

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



