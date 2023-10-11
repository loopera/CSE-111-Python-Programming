import math

items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

boxes = items / items_per_box

print (f"\nFor {items} items, packing {items_per_box} items in each box, you will need {math.ceil(boxes)} boxes.\n")

