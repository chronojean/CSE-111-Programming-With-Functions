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
        print("Undetermined OS")

def print_items(price_items):
    print("----------------------------------")
    for i in range(len(price_items)):        
        print(f"Item {i+1}: {price_items[i][0]}\tQuantity: {price_items[i][1]}\nTotal of item {i+1}: {round(price_items[i][0]*price_items[i][1],2)}")
        print("----------------------------------")
clear_cls()
subtotal = 0
price = ""
count = 0
cant = 0
price_items = []
while price != 0:
    clear_cls()
    if(subtotal>0):
        print(f"Subtotal: {round(subtotal,2)}")
    price = float(input(f"Price of item {count+1}: "))
    if(price== 0):
        break
    count += 1
    cant = float(input(f"Quantity of item {count}: "))
    price_items.append([price,cant])
    subtotal += (price*cant)

day_of_week = datetime.datetime.now().weekday()
clear_cls()
print_items(price_items)

print(f"Subtotal: {round(subtotal,2)}")

if day_of_week == 1 or day_of_week == 2:
    if subtotal >= 50:
        subtotal *= 0.90
    else:
        print(f"Amount needed to receive the discount: {(50-subtotal):.2f}")

print(f"Sales Tax: {(subtotal * 0.06):.2f}")
print(f"Total: {(subtotal * 1.06):.2f}")
print()