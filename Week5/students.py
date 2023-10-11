import csv


def main():

    ID_NUMBER_INDEX = 0
    NAME_INDEX = 1
    students_dict = read_dictionary("students.csv", ID_NUMBER_INDEX)
    print(students_dict)

    id = input("Please enter an I-Number: ")
    


    if id in students_dict:
        value = students_dict[id]
        name = value[NAME_INDEX]
        print(name)
    else:
        print("No such student")


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

    dictionary = {}
    with open(filename,"rt") as csv_file:

        # use csv module to create a reader object
        reader = csv.reader(csv_file)

        # Skip First row
        next(reader)

        # read rows one row at a time.
        for row_list in reader:
            # if data is not blank, add the data to the dictionary
            if len(row_list) != 0:
                # from current row, retrieve the data that contains key
                key = row_list[key_column_index]
                # store data from current row to the dictionary
                dictionary[key] = row_list

    return dictionary


if __name__ == "__main__":
    main()
