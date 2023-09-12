import os  # Importa el módulo 'os' para acceder a funcionalidades del sistema operativo
import platform # Importa el módulo platform para saber en qué plataforma funciona (Linux/Windows/etc.)
import datetime # Importa el módulo datetime para acceder a funcionalidades del sistema-fecha

def clear_cls():
    # Obtiene el nombre del sistema operativo
    sistema_operativo = platform.system()

    if sistema_operativo == "Windows":
        os.system('cls')
    elif sistema_operativo == "Linux":
        os.system('clear')
    else:
        print("No se pudo determinar el sistema operativo")
        
clear_cls()

subtotal = float(input("Ingresa el subtotal del cliente: "))
day_of_week = datetime.datetime.now().weekday()

subtotal *= 0.90 if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2) else 1

print(f"Monto del impuesto de ventas: {(subtotal * 0.06):.2f}")
print(f"Total: {(subtotal * 1.06):.2f}")