import csv

def print_dictionary(some_dict):
    for row in some_dict:
        print(row,end="--->")
        for column in some_dict[row]: 
            print(" ",column,end=" ||")
        print()
    print()

def print_list(lista):
    for element in lista:
        if isinstance(element, list):
            print_list(element)
        else:
            print(element,end=" ")
    print()

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
    products_dict = read_dictionary("products.csv",0)
    print("All Products")
    print_dictionary(products_dict)
    request = read_request("request.csv",products_dict)
    print("Requested Items")
    
    for row in request:
        print(f"{row[1]}: {row[2]} @ {row[3]}")
    
    #print_list(request)
    #print()
    # for row in request:
    #     print(f"Product Name: {row[1]}\t Requested Quantity: {row[3]}   Unit Price: {row[2]}   Total/Product: {float(row[2])*float(row[3])}")
    # print(f"Subtotal: { round(sum([row[2]*row[3] for row in request]),2)  }")

if __name__ == "__main__":
    main()
