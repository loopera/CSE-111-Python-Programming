import csv

from datetime import datetime

def main():
    try:

        PRODUCT_NUMBER_INDEX = 0
        products_dict = read_dictionary("products.csv", PRODUCT_NUMBER_INDEX)

        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)

            print("Inkom Emporium")

            print()
            # print("\nRequested Items:")
            subtotal = 0
            number_of_items = 0

            for row in reader:
                request_product = row[0]  # key
                request_quantity = float(row[1])

                # if request_product in products_dict:
                # value = products_dict[request_product]
                # product_name = value[0]
                # price = float(value[1])

                # Another way to write this:
                price = float(products_dict[request_product][1])
                product_name = products_dict[request_product][0]

                print(f"{product_name}: {request_quantity:.0f} @ {price}")

                number_of_items += request_quantity
                cost = request_quantity * price
                subtotal += cost

            print(f"\nNumber of Items: {number_of_items:.0f}")

        # Exceeding Requirements
        current_date_and_time = datetime.now()
        day_of_week = current_date_and_time.weekday()        
        #print(f"\nDay of the week {day_of_week}")

        # Discount on Tuesday and Wednesday
        if day_of_week == 1 or day_of_week == 2:
            discount = 0.10 * subtotal
            subtotal_with_discount = subtotal - discount
            sales_tax_disc = 0.06 * subtotal_with_discount
            total_disc = subtotal_with_discount + sales_tax_disc
            print(f"Subtotal: {subtotal_with_discount:.2f}")
            print(f"Discount amount: {discount:.2f}")
            print(f"Sales tax: {sales_tax_disc:.2f}")
            print(f"Total: {total_disc:.2f}")
        else:
            sales_tax = subtotal * 0.06
            total = subtotal + sales_tax
            print(f"Subtotal: {subtotal:.2f}")
            print(f"Sales tax: {sales_tax:.2f}")
            print(f"Total: {total:.2f}")
      
        print()
        print("Thank you for shopping at the Inkom Emporium.")

            # Use an f-string to print the current
            # date and the current time.
        print(f"{current_date_and_time:%a %b  %d %H:%M:%S %Y}")

    except (FileNotFoundError, PermissionError) as error:
        print("Error: missing file")
        print(error)

    except KeyError as key_err:
        print("Error: Unknown product ID in the request.csv file")
        print(key_err)


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
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
            product_number = row[0]
            product_name = row[1]
            price = float(row[2])

            dictionary[product_number] = [product_name, price]

    return dictionary


if __name__ == "__main__":
    main()
