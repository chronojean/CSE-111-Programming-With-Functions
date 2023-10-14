import pandas as pd

# Crear un array bidimensional
array_bidimensional = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]

# Convertir el array en un DataFrame
df = pd.DataFrame(array_bidimensional)
for row in array_bidimensional:
    if "A" in row:
        print("existe")
        break
# Imprimir el DataFrame
print(df)