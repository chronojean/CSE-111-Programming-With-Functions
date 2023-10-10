import csv
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

def main():
    with open("students.csv","rt") as my_file:
        print(my_file.readline())
        print(my_file.read())

if __name__ == "__main__":
    main()