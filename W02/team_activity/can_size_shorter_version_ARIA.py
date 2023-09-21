import math
import os
import platform

def clear_cls():
    os.system('cls' if platform.system() == "Windows" else 'clear')

def get_text_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except IOError:
        print("An error occurred while opening the file.")
        return None

def text_matrix_to_array(text="",line="\n",column=","):
    return [row.split(column) for row in text.split(line) if len(row)>0]

def compute_volume(radius,height):
    return math.pi*(radius**2)*height

def surface_area(radius,height):
    return 2*math.pi*radius*(radius+height)

def compute_storage_efficiency_rh(radius,height):
    return compute_volume(radius,height)/surface_area(radius,height)

def compute_cost_efficiency_v_c(volume,cost_per_can):
    return volume/cost_per_can

def print_list(lista, sorted_by_column=0, row_separator="-", column_separator="|"):
    clear_cls()
    for row in lista:
        for column in row:
            print(column, end="") if isinstance(column, str) else None
            print(" "*(12 - len(str(column))), end="") if not(lista.index(row)==0 and row.index(column)==sorted_by_column) else print("♦",end="")
            print(column, end="") if not isinstance(column, str) else None
            print(column_separator, end="")
        print()
        if row_separator != "" and column_separator != "":
            print(column_separator.join([row_separator]*len(row)))

def print_menu(items,exit_option="X"):
    for i, item in enumerate(items):
        print(f"{i+1}. {item}")
    print(f"\n{exit_option}. Exit.")
    return input("\tPlease choose an option: ")

def main():
    clear_cls()
    cans = text_matrix_to_array(get_text_file("data.txt"), "\n", "\t")
    menu_items = ["Sort by Name", "Sort by Radius", "Sort by Height", "Sort by Cost", "Sort by Volume",
                  "Sort by Surface", "Sort by Storage Efficiency", "Sort by Cost Efficiency"]

    for row in cans:
        for i, column in enumerate(row):
            try:
                row[i] = float(column.strip("$"))
            except:
                pass

    cans[0].extend(["Volume cm3", "Surface cm3", "Stor. Eff."])

    while True:
        choice = print_menu(menu_items)

        if choice == "X":
            break

        if choice.isdigit() and 1 <= int(choice) <= len(menu_items):
            sort_option = int(choice) - 1
            sorted_cans = sorted(cans[1:], key=lambda x: x[sort_option])
            sorted_cans.insert(0, cans[0])
            print_list(sorted_cans, sorted_by_column=sort_option)

        input("Press Enter to continue...")
main()