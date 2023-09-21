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

def get_text_file(filename):
    """Opens a file and return it's content."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except IOError:
        print("An error occurred while opening the file. Maybe the file is missing, protected or you don't have the permission to access the file")
        return None
    
def text_matrix_to_array(text="",line="\n",column=","):
    """Converts a string into an array[][] using specified separators"""
    return [row.split(column) for row in text.split(line) if len(row)>0]

def compute_volume(radius,height):
    return math.pi*(radius**2)*height

def surface_area(radius,height):
    return 2*math.pi*radius*(radius+height)

def compute_storage_efficiency_rh(radius,height):
    return compute_volume(radius,height)/surface_area(radius,height)

def compute_storage_efficiency_vs(volume,surface):
    return volume/surface

def compute_cost_efficiency_rh_c(radius,height,cost_per_can):
    return compute_volume(radius,height)/cost_per_can

def compute_cost_efficiency_v_c(volume,cost_per_can):
    return volume/cost_per_can

def print_list(lista, sorted_by_column=0, row_separator="-", column_separator="|"):
    my_var = sorted_by_column + 99
    my_var = None
    clear_cls()
    for i in range(len(lista)):
        row = lista[i]
        for j in range(len(row)):
            column = row[j]
            print(column, end="") if isinstance(column, str) else None
            for k in range(12 - len(str(column))):
                print(" ", end="")if not(i==0 and j==sorted_by_column) else print("♦",end="")
            print(column, end="") if not isinstance(column, str) else None
            print(column_separator, end="")
        print() if row_separator != "" and column_separator != "" else None
        for x in range(len(row) * 12):
            print(column_separator, end="") if x > 0 and x % 12 == 0 else None
            print(row_separator, end="")
        print(row_separator)

def print_menu(items,exit_option="X"):
    for i in range(len(items)):
        print(f"{i+1}. {items[i]}")
    print(f"\n{exit_option}. Exit.")
    return input("\tPlease choose an option: ")

def main():
    clear_cls()
    cans = text_matrix_to_array(get_text_file("data.txt"),"\n","\t")
    menu_items = ["Sort by Name","Sort by Radius","Sort by Height","Sort by Cost", "Sort by Volume", "Sort by Surface","Sort by Storage Efficiency","Sort by Cost Efficiency"]
    for i in range (len(cans)):
        for j in range(len(cans[i])):
            try:
                cans[i][j] = float(cans[i][j].strip("$"))
            except:
                None
    cans[0].append("Volume cm3")
    cans[0].append("Surface cm3")
    cans[0].append("Stor. Eff.")
    cans[0].append("Cost Eff $")
    for i in range(1,len(cans)):
        cans[i].append(round(compute_volume(cans[i][1],cans[i][2]),2))
        cans[i].append(round(surface_area(cans[i][1],cans[i][2]),2))
        cans[i].append(round(compute_storage_efficiency_vs(cans[i][4],cans[i][5]),2))
        cans[i].append(round(compute_cost_efficiency_v_c(cans[i][4],cans[i][3]),2))
    print_list(cans,0)
    resp = None
    while resp != "X":
        resp = print_menu(menu_items).upper()
        try:
            resp = int(resp)-1
            if not (resp>=0 and resp <len(menu_items)):
                resp = "w"
                resp = float(resp)
            if(resp == 0):
                print_list(cans,resp)
            else:
                print_list(cans[0:1]+sorted(cans[1:],key=lambda x:x[resp],reverse=True),sorted_by_column=resp)
        except:
            if(resp!="X"):
                input("Invalid option.")
main()