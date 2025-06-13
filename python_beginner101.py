# names = "bright", "chika", "okezie"
# first_Name, Middle_Name, Last_Name = names
# age = 26
# print(f"{names} is {age} year old")
# print(type(names))

"""Goal:
Create a simple Python script to track a single customer's order in your delivery app."""

# Customer order summary
customer_name = "bright"
pickup_address = "12 Omodara Ave"
delivery_address = "13 Fagba Road"
item_description = "iphone"
quantity = 10
delivery_fee = 59.99
price_per_item = 2000
is_paid = False
rider_name = "chika"
rider_number = 123456789
if is_paid:
    print("Payment Status: ✅ Paid")
else:
    print("Payment Status: ❌ Awaiting payment")

# Calculating total cost
total_cost = quantity * price_per_item
final_amount_due = total_cost + delivery_fee

# Order Summary
print("Order Summary")
print("Customer Name:", customer_name)
print("Pickup Address:", pickup_address)
print(f"Rider Name/Cell Number:", rider_name, rider_number)
print("Delivery Address:", delivery_address)
print("Item:", item_description)
print(f"Total Cost: ${total_cost}")
print(f"Here's your total cost: ${final_amount_due}")