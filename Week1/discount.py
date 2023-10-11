from datetime import datetime

current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

subtotal = float(input("Please enter the subtotal: "))

if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    discount = 0.10 * subtotal
    total_with_discount = subtotal - discount
    sales_tax = 0.06 * total_with_discount
    total = total_with_discount + sales_tax
    print(f"Discount amount: {discount:.2f}")
    print(f"Sales tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")
else:
    sales_tax = 0.06 * subtotal
    total = subtotal + sales_tax
    print(f"Sales tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")

print(f"Day of week: {day_of_week}")
