import csv
# Core Requirements
# Your program must do the following:

# Open the students.csv file for reading, skip the first line of text in the file because it contains only headings, and read the other lines of the file into a dictionary. The program must store each student I-Number as a key and each I-Number name pair or each name as a value in the dictionary.
# Get an I-Number from the user, use the I-Number to find the corresponding student name in the dictionary, and print the name.
# If a user enters an I-Number that doesn’t exist in the dictionary, your program must print the message, "No such student" (without the quotes).

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
        # Create an empty dictionary that will
        # store the data from the CSV file.
        dictionary = {}
        with open(filename,"rt") as csv_file:#This will open the file, the name is the value inside filename
            #This will read the first line of the file as you can see, the first line is a header
            #csv_file.readline()#we usually do this to read the 1st line and ignore header, but according to this class it should be done other way
            # Use the csv module to create a reader object
            # that will read from the opened CSV file.
            reader = csv.reader(csv_file)
            
            # The first row of the CSV file contains column
            # headings and not data, so this statement skips
            # the first row of the CSV file.
            next(reader)
            
            # Read the rows in the CSV file one row at a time.
            # The reader object returns each row as a list.
            for row_list in reader:
                # If the current row is not blank, add the
                # data from the current to the dictionary.
                if len(row_list) != 0:                    
                    # From the current row, retrieve the data
                    # from the column that contains the key.
                    key = row_list[key_column_index]
                    # Store the data from the current
                    # row into the dictionary.
                    dictionary[key] = row_list
        # Return the dictionary.
        return dictionary
        

def main():
    #calls the function and store the data of the students in a dictionary
    my_dict = read_dictionary("students.csv",0)
    #prints the dictionary
    #print(my_dict)

    i_number = input("Please enter an I-Number (xxxxxxxxx):").replace("-","")

    if len(i_number)<9:
        print("Invalid i_number, too few digits")
    elif len(i_number)>9:
        print("Invalid I-Number: too many digits")
    elif not i_number.isnumeric():
        print("Invalid I-Number, i_number can only have numbers and dashes.")
    elif i_number in my_dict:
         print(my_dict[i_number][1])
    else:
         print("No such student")
   

if __name__ == "__main__":
    main()

"""
{'751766201': ['751766201', 'James Smith'],
'751762102': ['751762102', 'Esther Einboden'],
'052058203': ['052058203', 'Cassidy Benavidez'],
'323021604': ['323021604', 'Joel Hatch'],
'251041405': ['251041405', 'Brianna Ririe'],
'001152306': ['001152306', 'Stefano Hisler'],
'182706207': ['182706207', 'Hyeonbeom Park'],
'124712708': ['124712708', 'Maren Thomas'],
'212505409': ['212505409', 'Tyler Clark']
}
"""