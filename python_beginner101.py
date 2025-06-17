# names = "bright", "chika", "okezie"
# first_Name, Middle_Name, Last_Name = names
# age = 26
# print(f"{names} is {age} year old")
# print(type(names))

"""Goal:
Create a simple Python script to track a single customer's order in your delivery app."""

# # Customer order summary
# customer_name = "bright"
# pickup_address = "12 Omodara Ave"
# delivery_address = "13 Fagba Road"
# item_description = "iphone"
# quantity = 10
# delivery_fee = 59.99
# price_per_item = 2000
# is_paid = False
# rider_name = "chika"
# rider_number = 123456789
# if is_paid:
#     print("Payment Status: ✅ Paid")
# else:
#     print("Payment Status: ❌ Awaiting payment")

# # Calculating total cost
# total_cost = quantity * price_per_item
# final_amount_due = total_cost + delivery_fee

# # Order Summary
# print("Order Summary")
# print("Customer Name:", customer_name)
# print("Pickup Address:", pickup_address)
# print(f"Rider Name/Cell Number:", rider_name, rider_number)
# print("Delivery Address:", delivery_address)
# print("Item:", item_description)
# print(f"Total Cost: ${total_cost}")
# print(f"Here's your total cost: ${final_amount_due}")

# """
# Task:
# Create a variable for user_age.

# Use if statements to:

# Print “You’re eligible to register” if age is 18 or above.

# Else print “You’re too young to register.”
# """

# # Ask users for their age
# age = int(input("What is your age? "))

# # check if user is eligible to register based on age
# if age >= 18:
#     print("You're eligible to register")
# else:
#      print("You're not eligible to register")


# x = "bright" # This a global variable which can reused anywhere in our code

# def myfunc():
#     x = "chika" # This is a local variable 
#     print(x + " is learning phython")

# myfunc()
# print(x + " is learning phython")

# DATA TYPES IN PYTHON/ 3 NUMERIC NUMBER

# bright = 20 # int
# bright1= 20.6 # float
# Bright = 2j # complex
# print(type(bright))
# print(type(bright1))
# print(type(Bright))

# DATA TYPE CONVERSION
# age = 20 # int
# price = 20.6 # float
# imaginary_unit = 76j # complex

# A = float(age) # CONVERT FROM INT TO FLOAT
# B = int(price) # CONVERT FROM FLOAT TO INT
# C = complex(age) # CONVERT FROM INT TO COMPLEX
# E = str(imaginary_unit)
# print("A:", A, type(A))
# print("B:", B, type(B))
# print("C:", C, type(C))
# print("E:", E, type(E))

"""
# ✅ Assignment 1: Convert String Input to Integer
# Goal: Ask the user for their age (as input), convert it to an integer, and print the type.

# 🔹 Input: "25"
# 🔹 Expected Output: Your age is 25 and it is of type <class 'int'>
# """

# # Asking User for their age
# age = int(input('What is your age? '))
# print(f"Your age is {age} and it of type {type(age)}")

"""
✅ Assignment 2: Convert Float to Integer and Back
Goal: Create a float variable, convert it to an integer (truncate decimals), then convert back to float.

🔹 Example: price = 45.99
🔹 Output:
Integer version: 45
Back to float: 45.0
"""

# # Craeting a floating Variable
# price = 45.99

# # Converting float to int and back to float
# integer_version = int(price)
# back_to_float = float(integer_version)

# # printing my values
# print(f"Integer version: {integer_version}, Back to float: {back_to_float}")

"""
✅ Assignment 3: Convert Integer to Complex
Goal: Create a variable for distance = 100, convert it to a complex number, and print both value and type.

🔹 Output: Distance as complex: (100+0j) and <class 'complex'>
"""

# # Creating variable for distance

# distance = 100 # this is an int variabale

# # Converting int variable to a complex variable
# complex_variable = complex(distance)

# # Printing the value and the current data type
# print(f"The distance as complex is: {complex_variable}", type(complex_variable))

"""
✅ Assignment 4: Convert Two Strings to Numbers and Add Them
Goal: Ask the user to input two numbers as strings. Convert both to integers and print their sum.

🔹 Input: "5" and "7"
🔹 Output: The total is 12
"""
# # Asking Users to input numeric numbers
# first_input = input("Enter your first numeric number here: ")
# second_input = input("Enter your second number here: ")

# # Converting user input to int before suming their values
# converting_first_input = int(first_input)
# converting_second_input = int(second_input)

# # Suming up the values gotten from the user input
# User_input = converting_first_input + converting_second_input

# # printing the total user input sumed up
# print(f"The total is {User_input}")

"""✅ Assignment 5: Use type() to Compare Original and Converted Types
Goal: Declare one float and one integer. Convert both to string, then print original and converted types.

🔹 Variables:

python
Copy code
weight = 70.5  
count = 3  
🔹 Output:

pgsql
Copy code
Original type of weight: <class 'float'>, After conversion: <class 'str'>
Original type of count: <class 'int'>, After conversion: <class 'str'>."""

# Decaring data type variables
# weight = 70.5 
# count = 3

# # Converting Both numbers to a 'str' data type
# converting_weight = str(weight)
# converting_count = str(count)

# # Printing original data types and converted types
# print(f"Original data type for weight:", type(weight), "After Conversion:", type(converting_weight))
# print(f"Original data type for count:", type(count), "After Conversion:", type(converting_count))

"""
✅ Casting Challenge: Delivery Fee Calculator
Goal:
Ask the user to enter:

The number of items they’re delivering (as a string input)

The price per item (as a float input)

Then:

Convert the values to appropriate types

Calculate the total delivery value

Display the result with the correct type

🧩 Requirements:
Convert number of items to int

Convert price per item to float

Multiply them to get total_cost

Print the result along with its type

📌 Sample Output:
pgsql
Copy
Edit
Enter number of items: 5
Enter price per item: 20.5
Total cost is: 102.5
The data type of total cost is: <class 'float'>
"""

# Asking users to input total item they're deliving
# total_delivering_item = int(input("How many items are you delivering? ")) 
# price_per_item = float(input("How much does each item cost? "))

# # Calculating the total cost of the item
# total_cost = price_per_item * total_delivering_item

# # Printing out the total value and the current data type 
# print("Total cost is:", total_cost)
# print("The data type of total cost is", type(total_cost))