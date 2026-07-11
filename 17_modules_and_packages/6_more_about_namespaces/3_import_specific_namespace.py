# En lugar de importar todo con `import *`, puedes importar solo las funciones o variables especificas necesarias.
# Esto ayuda a evitar la polucion del espacio de nombres y asegura mas control sobre lo que se lleva en el espacio de nombres global.

# Importando unicamente 'pi' y 'sqrt' desde el modulo math.
from math import pi, sqrt

# Ahora podemos usar estas especificas 'nombres sin estropear el espacio de nombres global.
print("Valor de pi:", pi)  # Imprime el valor de pi.
print("Raiz cuadrada de 16:", sqrt(16))  # Imprime la raiz cuadrada de 16.

# Sin riesgo de colision de nombres con funciones o variables del modulo matematico otro.
