import math
import os
import platform

# Function to clear the console screen based on the operating system
def clear_cls():
    sistema_operativo = platform.system()
    if sistema_operativo == "Windows":
        os.system('cls')
    elif sistema_operativo == "Linux":
        os.system('clear')
    else:
        print("Undetermined OS")

# Function to get the content of a text file
def get_text_file(filename):
    """Opens a file and returns its content."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except IOError:
        print("An error occurred while opening the file. Maybe the file is missing, protected, or you don't have permission to access the file")
        return None

# Function to convert a text matrix into a 2D array using specified separators
def text_matrix_to_array(text="", line="\n", column=","):
    """Converts a string into an array[][] using specified separators"""
    return [row.split(column) for row in text.split(line) if len(row) > 0]

# Function to compute the volume of a cylinder
def compute_volume(radius, height):
    return math.pi * (radius ** 2) * height

# Function to compute the surface area of a cylinder
def surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

# Function to compute the storage efficiency of a cylinder
def compute_storage_efficiency_rh(radius, height):
    return compute_volume(radius, height) / surface_area(radius, height)

# Function to compute the cost efficiency of a cylinder based on cost per can
def compute_cost_efficiency_rh_c(radius, height, cost_per_can):
    return compute_volume(radius, height) / cost_per_can

# Function to compute the cost efficiency of a cylinder based on cost per can and volume
def compute_cost_efficiency_v_c(volume, cost_per_can):
    return volume / cost_per_can

# Function to print a list in a formatted way
# Function to print a 2D list in a formatted way
def print_list(lista, sorted_by_column=0, row_separator="-", column_separator="|"):
    # Clear the console screen
    clear_cls()
    
    # Iterate through the rows of the input list
    for i in range(len(lista)):
        row = lista[i]
        
        # Iterate through the columns of each row
        for j in range(len(row)):
            column = row[j]
            
            # If it's a string, prints the value before the whitespaces (align left)
            print(column, end="") if isinstance(column, str) else None
            
            # Add padding spaces or a special character (♦) for the sorted column
            for k in range(12 - len(str(column))):
                print(" ", end="") if not (i == 0 and j == sorted_by_column) else print("♦", end="")
            
            # If it's not a string, prints the column value (align right)
            print(column, end="") if not isinstance(column, str) else None
            
            # Print the column separator
            print(column_separator, end="")
        
        # Print a new line if both row_separator and column_separator are not empty
        print() if row_separator != "" and column_separator != "" else None
        
        # Print the horizontal line separator
        for x in range(len(row) * 12):
            print(column_separator, end="") if x > 0 and x % 12 == 0 else None
            print(row_separator, end="")
        
        # Print the row separator
        print(row_separator)


# Function to print a menu and get user input
def print_menu(items, exit_option="X"):
    for i in range(len(items)):
        print(f"{i + 1}. {items[i]}")
    print(f"\n{exit_option}. Exit.")
    return input("\tPlease choose an option: ")

# Import necessary libraries or modules

# Main function to execute the program
def main():
    # Clear the console screen
    clear_cls()
    
    # Read the data from the text file and convert it into a 2D array
    cans = text_matrix_to_array(get_text_file("data.txt"), "\n", "\t")
    
    # Define menu items for sorting options
    menu_items = ["Sort by Name", "Sort by Radius", "Sort by Height", "Sort by Cost", "Sort by Volume", "Sort by Surface", "Sort by Storage Efficiency", "Sort by Cost Efficiency"]
    
    # Convert the dollar values in the array to float values
    for i in range(len(cans)):
        for j in range(len(cans[i])):
            try:
                cans[i][j] = float(cans[i][j].strip("$"))
            except:
                None
    
    # Add additional headers to the array
    cans[0].append("Volume cm3")
    cans[0].append("Surface cm3")
    cans[0].append("Stor. Eff.")
    cans[0].append("Cost Eff $")
    
    # Calculate and add volume, surface area, storage efficiency, and cost efficiency for each can
    for i in range(1, len(cans)):
        cans[i].append(round(compute_volume(cans[i][1], cans[i][2]), 2))
        cans[i].append(round(surface_area(cans[i][1], cans[i][2]), 2))
        cans[i].append(round(compute_storage_efficiency_rh(cans[i][1], cans[i][2]), 2))
        cans[i].append(round(compute_cost_efficiency_v_c(cans[i][4], cans[i][3]), 2))
    
    # Print the list of cans
    print_list(cans, 0)
    
    # Initialize response variable
    resp = None
    
    # Display menu options and process user input until 'X' is entered
    while resp != "X":
        resp = print_menu(menu_items).upper()
        
        try:
            # Convert response to integer and check if it is a valid menu option
            resp = int(resp) - 1
            if not (resp >= 0 and resp < len(menu_items)):
                resp = "w"
                resp = float(resp)
            
            # Sort and print the list based on the selected column
            if (resp == 0):
                print_list(cans, resp)
            else:
                print_list(cans[0:1] + sorted(cans[1:], key=lambda x: x[resp], reverse=True), sorted_by_column=resp)
        
        # Handle invalid input
        except:
            if(resp!="X"):
                input("Invalid option.")

# Execute the main function
main()
