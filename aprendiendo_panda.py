import pandas as pd

# Desde una lista
mi_serie = pd.Series([1, 2, 3, 4, 5])
print(mi_serie)


mi_serie.info()

# Desde un arra de NumPy
import numpy as np
array = np.array([10, 20, 30, 40, 50])
mi_serie = pd.Series(array)
print(mi_serie)


# Desde un diccionario
diccionario = {'a': 1, 'b': 2, 'c':3}
mi_serie = pd.Series(diccionario)
print(mi_serie)

