import math
import os
import platform
"""
The size of a car tire in the United States is represented with three numbers like this: 205/60R15.
The first number is the width of the tire in millimeters. The second number is the aspect ratio.
The third number is the diameter in inches of the wheel that the tire fits.

The volume of space inside a tire can be approximated with this formula:
v = (πw**2a(wa + 2540d))/10**10

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.

Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.

For all assignments in CSE 111, please write your program in a file named as the assignment states. This assignment requires you to name your program tire_volume.py. If you name your program something else, it will be harder for the graders to score your submitted assignment.
"""
"""
test output:

> python tire_volume.py
Enter the width of the tire in mm (ex 205): 185
Enter the aspect ratio of the tire (ex 60): 50
Enter the diameter of the wheel in inches (ex 15): 14

The approximate volume is 24.09 liters

> python tire_volume.py
Enter the width of the tire in mm (ex 205): 205
Enter the aspect ratio of the tire (ex 60): 60
Enter the diameter of the wheel in inches (ex 15): 15

The approximate volume is 39.92 liters
"""
def clear_cls():
    # Obtiene el nombre del sistema operativo
    sistema_operativo = platform.system()

    if sistema_operativo == "Windows":
        os.system('cls')
    elif sistema_operativo == "Linux":
        os.system('clear')
    else:
        print("Undetermined OS")

clear_cls()

w = float(input(f"Enter the width of the tire in mm (ex 205): "))
a = float(input(f"Enter the aspect ratio of the tire (ex 60): "))
d = float(input(f"Enter the diameter of the wheel in inches (ex 15): "))

v = (math.pi*(w**2)*a*(w*a+2540*d))/10**10

print(f"\nThe approximate volume is {round(v,2)} liters.\n")