#Exceeding: Joined request and products data into a single array for easy of use, used a funciton to clear the screen before the output regarding the os.
#           Created a custom "print_list" recursive function that prints any sort of array regarding the size or dimensions (not used here though, it was edited to print produc_name: n_items @ item_price
#           Created a function that converts elements of any list into numbers, using try-except to handle values that can't be converted such as strings.
#           Repeated items ar not dupliccated: ex Yogurt 4 items, and then Yogurt 3 itmes again. Instead it store Yogurt 7 items.
#           a 10% discount is applied if today is tueswday or wednesday and it's still morning before 11am
import csv,os, platform, sys
from datetime import datetime

def clear_cls():
    """Use the clear terminal function for Linux or Windows"""
    sistema_operativo = platform.system()
    if sistema_operativo == "Windows":
        os.system('cls')
    elif sistema_operativo == "Linux":
        os.system('clear')
    else:
        print("Undetermined OS")

def print_dictionary(some_dict):
    for row in some_dict:
        print(row,end="--->")
        for column in some_dict[row]: 
            print(" ",column,end=" ||")
        print()
    print()

def print_list(request):
    # for element in lista:
    #     if isinstance(element, list):
    #         print_list(element)
    #     else:
    #         print(element,end=" ")
    # print()
    for row in request:
        print(f"{row[1]}: {row[2]} @ {row[3]}")

def list_items_to_number(some_list):
    for i in range(len(some_list)):
        if isinstance(some_list[i],list):
            some_list[i] = list_items_to_number(some_list[i])
        else:
            try:
                some_list[i] = float(some_list[i])
            except:
                None
    return some_list
    
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    buff = {}
    with open(filename,"rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list)>0:
                key = row_list[key_column_index]
                buff[key] = row_list
    return buff

def read_request(filename,some_dict):
    arr = []
    with open(filename,"rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list)>0:
                buff = some_dict[row_list[0]]+row_list[1:]
                buff = list_items_to_number(buff)
                duplicated = False
                for i,row in enumerate(arr):
                    if row_list[0] in row:
                        duplicated = True
                        break
                if duplicated:
                    arr[i][3]+=float(row_list[1])
                    duplicated = False
                else:
                    arr.append(buff)
    return arr

def main():
    try:
        products_dict = read_dictionary("products.csv",0)        
    except FileNotFoundError:
        print("The \"products.csv\" file has not been found.")
        sys.exit(0)
    except PermissionError:
        print("This user has no enough privileges to open  \"products.csv\"")
        sys.exit(0)
    
    try:
        request = read_request("request.csv",products_dict)
    except FileNotFoundError:
        print("The \"request.csv\" file has not been found.")
        sys.exit(0)
    except PermissionError:
        print("This user has no enough privileges to open  \"request.csv\"")
        sys.exit(0)
    except KeyError:
        print("The requested key is not in our database.")
        sys.exit(0)
    clear_cls()
    date = datetime.now()
    tax_rate = .06
    n_items = round(sum([int(row[3]) for row in request]),2)
    subtotal = round(sum([row[2]*row[3] for row in request]),2)
    taxes = round(subtotal * tax_rate,2)
    total = round(subtotal + taxes,2)
    print("------------------------------------")
    print("-----       --JPSMART--        -----")
    print("------------------------------------")
    #print_list(request)
    for row in request:
        print(f"Product: {row[1]}\t Quantity: {row[3]}   Unit Price: {row[2]}   product/subtotal: {float(row[2])*float(row[3])}")
    print()
    print(f"Number of Items: {n_items}")
    print(f"Subtotal: {subtotal }")
    print(f"Sales Tax: {taxes}")
    print(f"Total: {total}")
    print()
    print("Thank you for shopping at JPSMART, come again!")
    print(f"{date:%a %b %d %T %Y}")
    print()
    if (date.weekday()==1 or date.weekday()==2) and date.hour<=11:
        print(f"Congratulations, you just earned a 10%% discount in your buy!.\nYour new total is: {round(total*.9,2)}")
    print("We would love to know your thoughts while buying at JPSMART, please click here to do the survey: https://www.lipsum.com/feed/html")
    

if __name__ == "__main__":
    main()