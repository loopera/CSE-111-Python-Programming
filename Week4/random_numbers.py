#Team Activity Week 4 Lesson 7

import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print (f"Numbers List: {numbers}")
    
    append_random_numbers(numbers)

    print (f"After calling append_numbers_function, \nthe list is now:{numbers}")

def append_random_numbers (numbers_list, quantity=1):
    

    for i in range(quantity):
        random_number = random.uniform(0,100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)


if __name__ == "__main__":
    main()
