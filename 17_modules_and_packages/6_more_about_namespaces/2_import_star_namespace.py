# Utilizar `from <module> import *` implica todas las nombres de un modulo en la nube global.
# Esto puede causar colisiones de nombre y generalmente se recomienda en programas grandes.

# Importa todo del modulo math en la nube global.
from math import *

# Ahora todos los funciones y variables de math estan en la nube global.
print("Acesa el valor de pi en la biblioteca matematica.", pi)  # No necesidad de usar 'math.'.prefix.

# Define una funcion que sobrepone la importada `sqrt`.
def sqrt(x):
    return "Esta sobrescribe la importada `sqrt`."

print("Ejemplo de sobrecubrimiento:", sqrt(16))  # Devuelve la funcion local `sqrt`, sobrescribiendo a `math.sqrt`.

# Si necesitamos la raiz cuadrada original, ahora es mas dificil acceder debido a que se importo directamente.
# Perdemos claridad al importar todos los nombres de esta manera.
