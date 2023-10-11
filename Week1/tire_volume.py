import math

width = float(input("\nEnter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
volume = (math.pi * width**2 * aspect_ratio) * (width * aspect_ratio + 2540 * diameter) / 10000000000

#Formula:
# Volume = (pi * width**2 * aspect_ratio) * (width * aspect_ratio + 2540 * diameter) / 10000000000

print(f"\nThe approximate volume is {volume:.2f} liters\n")

#Exceeding Requirements
#Asking for Phone number and storing it in file txt 
choice = input("Would you like to purchase a tire? (yes/no): ")
if choice.lower() == 'yes':
    phone_number = input("Please type in your Phone Number and our Customer Service will contact you shortly: ")
    print(f"\nThank you. One of our agents will call you shortly on your Phone Number: {phone_number}. Have a lovely day!\n")
    with open("volumes.txt", "at") as volumes_file:
        print(phone_number, file = volumes_file)
else:
    print("\nHave a lovely day! Goodbye!\n")

from datetime import datetime
current_date_and_time = datetime.now()

with open("volumes.txt", "at") as volumes_file:
    print (f"{current_date_and_time: %Y-%m-%d}, {width:.0f}, {aspect_ratio:.0f}, {diameter:.0f}, {volume:.2f}", file = volumes_file) 
    


