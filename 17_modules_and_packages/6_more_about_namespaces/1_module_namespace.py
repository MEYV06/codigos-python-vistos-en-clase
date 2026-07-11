# Cuando importas un modulo en Python, crea una caja de nombres para el modulo.
# Las variables, funciones y clases del modulo estan almacenadas en esa caja de nombres.

# Vamos a importar la biblioteca math y inspeccionar su caja de nombres.
import math

# La funcion `dir()` puede usarse para listar todos los nombres en el espacio de nombres del modulo math.
print("Navegacion de la biblioteca matematica:", dir(math))

# Acceso a atributos especificos en el espacio de nombres de la biblioteca matematica.
print("Acesa el valor de pi en la biblioteca matematica.", math.pi)  # Accede al valor del pi en la biblioteca matematica.

# Define una funcion que sobreescribe una funcion importada.
def sqrt(x):
    return "Este esconde math.sqrt"

print("Ejemplo de sobrecubrimiento:", sqrt(16))  # Imprime la funcion raiz cuadrada local.

# Usa la funcion sqrt del modulo explicitamente.
print("Usando math.sqrt:", math.sqrt(16))  # Devuelve el calculo de raiz cuadrada real.
