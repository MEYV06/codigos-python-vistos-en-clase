# TODO 1: crea una lista de numeros del 1 al 10.
# Luego revisa el valor de numbers para ver la lista inicial.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# TODO 2: crea una lista con los cuadrados de numbers usando list comprehension.
# Luego revisa el valor de squares para ver los cuadrados.
squares = [n**2 for n in numbers]
# TODO 3: crea una lista solo con los numeros pares.
# Luego revisa el valor de evens para ver los numeros pares.
evens = [n for n in numbers if n % 2 == 0]
# TODO 4: crea una lista solo con los numeros mayores que 5.
# Luego revisa el valor de greater_than_five para ver los numeros filtrados.
greater_than_five = [n for n in numbers if n > 5]
# TODO 5: crea una lista de etiquetas "Par" o "Impar".
# Luego revisa el valor de labels para ver las etiquetas creadas.
labels = ["Par" if n % 2 == 0 else "Impar" for n in numbers]
# TODO 6: crea una lista donde los pares se dupliquen y los impares se conviertan en 0.
# Luego revisa el valor de modified_numbers para ver los numeros modificados.
modified_numbers = [n * 2 if n % 2 == 0 else 0 for n in numbers]
# TODO 7: crea una lista de nombres.
# Luego revisa el valor de names para ver la lista de nombres.
names = ["Ana", "Luis", "Marcela", "Jose"]
# TODO 8: crea una lista con los nombres en mayusculas.
# Luego revisa el valor de uppercase_names para ver los nombres transformados.
uppercase_names = [name.upper() for name in names]
# TODO 9: crea una lista solo con los nombres que tengan mas de 4 caracteres.
# Luego revisa el valor de long_names para ver los nombres filtrados.
long_names = [name for name in names if len(name) > 4]
# TODO 10: crea una lista de numeros pequeños y una lista de letras.
# Luego revisa el valor de small_numbers y letters para ver las listas base.
small_numbers = [1, 2, 3]
letters = ["a", "b"]
# TODO 11: crea pares (numero, letra) combinando small_numbers y letters con varios for.
# Luego revisa el valor de number_letter_pairs para ver las combinaciones.
number_letter_pairs = [(n, l) for n in small_numbers for l in letters]
# TODO 12: crea una lista de numeros y una lista de vocales.
# Luego revisa el valor de more_numbers y vowels para ver las listas base.
more_numbers = [1, 2, 3, 4]
vowels = ["a", "e", "i"]
# TODO 13: crea pares solo con numeros pares y vocales "a" y "e".
# Luego revisa el valor de filtered_pairs para ver las combinaciones filtradas.
filtered_pairs = [(n, v) for n in more_numbers if n % 2 == 0 for v in vowels if v in ("a", "e")]
