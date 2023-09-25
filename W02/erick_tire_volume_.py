import math

# El usuario ingresa valores del ancho, relación de aspecto y diámetro desde el teclado
w = int(input("Ingrese el ancho del neumático en milímetros: "))
a = int(input("Ingrese la relación de aspecto del neumático: "))
d = int(input("Ingrese el diámetro de la rueda en pulgadas: "))

# Calcular el volumen del neumático
volumen = (math.pi * (w ** 2) * a * w * a + 2.540 * d) / 10_000_000_000

# Imprimir el resultado
print("El volumen del neumático es:", round(volumen, 2), "litros")