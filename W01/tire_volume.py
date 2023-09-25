from datetime import datetime
import math
import os
import platform
import sys


def clear_cls():
    """Use the clear terminal function for Linux or Windows"""
    sistema_operativo = platform.system()
    if sistema_operativo == "Windows":
        os.system('cls')
    elif sistema_operativo == "Linux":
        os.system('clear')
    else:
        print("Undetermined OS")      

def append_volumes_txt(linea):
    """Appends a string to the file 'volumes.txt'
    
        Returns: the content of the file after appending the line
    """
    try:
        with open("./volumes.txt", "a+") as file:
            file.write(f"{linea}\n")
            file.seek(0)
            content = file.read()
            return content
    except IOError:
        input("An error occurred while opening the file. Maybe the file is blocked or marked as 'read only' or you don't have the permission to access the file")
        
def good_bye_message(message="-----Thank You for buying at MythStore.com-----"):
    """Prints a good looking 'Good Bye' message. If the message is not specified for the user, it prints the default message."""
    print("***********************************************")
    print(message)
    print("***********************************************")
    print("\n\t\t Have a wonderful day!.\n")
    
resp = "Y"
while resp == "Y":
    clear_cls()
    w = int(input(f"Enter the width of the tire in mm (ex 205): "))
    a = int(input(f"Enter the aspect ratio of the tire (ex 60): "))
    d = int(input(f"Enter the diameter of the wheel in inches (ex 15): "))
    v = round((math.pi*(w**2)*a*(w*a+2540*d))/10**10,2)
    current_date_and_time = datetime.now()
    text_to_append=f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v}"
    print(f"\nThe approximate volume is {v} liters\n")
    willing=input(f"Would you like to contact one of our agents to check the available brands? Y/N: ").upper()
    text_to_append = f"{text_to_append}, {input('Please type your phone number including your country code (ex: +573024910393): ')}" if willing =="Y" else text_to_append
    append_volumes_txt(text_to_append)
    resp = input("Do you want to check more tire volumes? Y/N: ").upper()
print()

from datetime import datetime
import math
import os
import platform


def clear_cls():
    sistema_operativo = platform.system()
    if sistema_operativo == "Windows":
        os.system('cls')
    elif sistema_operativo == "Linux":
        os.system('clear')
    else:
        print("Undetermined OS")

def append_volumes_txt(linea):
    try:
        with open("./volumes.txt", "a+") as file:
            file.write(f"{linea}\n")
            file.seek(0)
            content = file.read()
            return content
    except IOError:
        input("An error occurred while opening the file. Maybe the file is blocked or marked as 'read only' or you don't have the permission to access the file")
        
def good_bye_message(message="-----Thank You for buying at MythStore.com-----"):
    print("***********************************************")
    print(message)
    print("***********************************************")
    print("\n\t\t Have a wonderful day!.\n")
    
resp = "Y"
while resp == "Y":
    clear_cls()
    w = int(input(f"Enter the width of the tire in mm (ex 205): "))
    a = int(input(f"Enter the aspect ratio of the tire (ex 60): "))
    d = int(input(f"Enter the diameter of the wheel in inches (ex 15): "))
    v = round((math.pi*(w**2)*a*(w*a+2540*d))/10**10,2)
    current_date_and_time = datetime.now()
    text_to_append=f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v}"
    print(f"\nThe approximate volume is {v} liters\n")
    willing=input(f"Would you like to contact one of our agents to check the available brands? Y/N: ").upper()
    text_to_append = f"{text_to_append}, {input('Please type your phone number including your country code (ex: +573024910393): ')}" if willing =="Y" else text_to_append
    append_volumes_txt(text_to_append)
    resp = input("Do you want to check more tire volumes? Y/N: ").upper()
print()