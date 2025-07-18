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

""" STRINGS ARE ARRAYS CHALLENGE """
"""
✅ Challenge 1: First & Last Letter Extractor
Goal: Ask the user for their name and print the first and last letter.

🔹 Example:
Input: "Chika"
Output: "C" and "a"

python
Copy
Edit
# Your turn: Use indexing to extract first and last character"""

# # Asking User For Their Name
# name = input("What is your name? ")

# # Extracting First and Last Character
# first_character = name[0]
# last_character = name[-1]

# # Printing out the character
# print(f"The first character is: {first_character} and The last character is: {last_character}")

"""
✅ Challenge 2: Tracking Code Splitter
Goal: Given a tracking code like "ORD56983", extract and print:

Prefix (first 3 characters)

Numeric code (rest of the characters)

🔹 Output:

mathematica
Copy
Edit
Order Prefix: ORD  
Order Number: 56983
"""

# # Get the tracking code of this Order
# Tracking_code = 'ORD56988'

# # Spliting the charcter to get the order number
# Order_Prefix = Tracking_code[:3]
# Order_Number = Tracking_code[3:]

# # Printing out the order values
# print("Your Order Perfix:", Order_Prefix)
# print("Your Order Number", Order_Number)

"""
✅ Challenge 3: String Reverser
Goal: Ask the user to input a word, and print it backwards.

🔹 Example:
Input: "delivery"
Output: "yreviled"

python
Copy code
# Tip: Use slicing with [::-1]
"""

# # Asking users to input any word of their choice
# word = input("Type in any word here: ")

# # Setting the system to print it backwards
# print_backwards = word[::-1]

# # Printing out the values
# print(print_backwards)

"""
✅ Challenge 4: Email Username Extractor
Goal: Given an email address like "rider@quickpedal.com", extract only the username ("rider").

🔹 Hint: Use .split("@") method.

🔹 Output:

python
Copy code
Email username is: rider
python
Copy code
# Use string split() method here
"""

# # User email
# email = input("What is your email? ").strip()

# # checking if user includes '@' in emial before spliting the email
# if "@" in email:
#     email_username = email.split("@")[0]
#     print(f"Email Username is:", email_username)
# else:
#   print("@ is missing in your email")

"""
✅ Challenge 5: Initials from Full Name
Goal: Ask the user for their full name and print their initials in uppercase.

🔹 Example:
Input: "chika bright"
Output: "Your initials are: CB"

python
Copy code
# Use split() and indexing to grab the first letter of each name
"""

# Full Name input

# Full_Name = input("What is your name? ").upper()

# # Spliting the values
# first_Initials = Full_Name.split()[0]
# second_initials = Full_Name.split()[1]

# # Getting initial character of each value
# Your_Initials = first_Initials[0] + second_initials[0]
# print(f"Your Initials are: {Your_Initials}")

# x = "Hello, World!"
# print(x[2:5])

# print(10 < 9)
# print(10 == 9)
# print (10 < 9)
"""
PYTHON OPERATORS
"""

# DETERMINE THE FOLLOWING EXPRESSION

# # Expression = (6 + 4) * 2 ** 3 - 10 / 2

# a = 2 ** 3
# b = 10 / 2
# c = 6 + 4

# e = a * c
# f = e - b
# print(f)

"""PYTHON LIST"""

# CREATING A FULL NAME LIST

# names = ["bright", "chika", "okezie"]

# # Checking if chika is in the above list

# if "chika" in names:
#     print("Yes", "chika is in the list of names")

# else:
#     print("We don'nt have chika in the list above")

"""
✅ Challenge: Check Package Type
You’re building a feature to check if a rider can carry a certain package.

python
Copy
Edit
allowed_packages = ["documents", "small box", "parcel", "groceries"]
🎯 Your Task:
Ask the user to input the type of package they want to send.

Use an if statement and the in operator to check if the package type is allowed.

If it's allowed, print:
"✅ This package type is allowed for delivery."

If not, print:
"❌ Sorry, this package type is not allowed."
"""
# # Package types that are allowed on QuickPedal
# allowed_packages = ["documents", "small box", "parcel", "groceries"]

# # Asking users for their package type
# package_type = input("What type of package are you delivering today? ")

# # Checking the of package the customer is delivering 
# if package_type in allowed_packages:
#     print("This package type is allowd for delivery.")

# else:
#     print("Sorry, this package type is not allowed.")


"""
✅ Challenge: QuickPedal Delivery Booking Summary
🎯 Goal: Simulate a basic delivery booking system that:

Asks the customer for their full name

Collects details of the item they want to deliver

Confirms if the package is allowed

Calculates the total cost

Displays a summary with the user’s initials

✍️ Challenge Requirements
Step 1: Ask for user input
Full name

Package type

Quantity

Price per item

Step 2: Check if package is allowed
Allowed packages:

python
Copy
Edit
allowed_packages = ["documents", "electronics", "groceries", "books"]
Step 3: If package is allowed:
Show total cost

Extract initials from name

Print a neat delivery summary

Step 4: If not allowed:
Print “❌ This package type is not accepted on QuickPedal.”

📌 Example Output
plaintext
Copy
Edit
Welcome to QuickPedal!
Enter your full name: Chika Bright
Enter package type: electronics
Enter quantity: 2
Enter price per item: 3500

✅ Package type is accepted.
Your delivery will cost ₦7000.
Customer Initials: CB

Thanks for choosing QuickPedal!
💡 Hint:
Use:

.split() to get initials

input() to collect user data

float() and int() for calculations

if and in to verify package type
"""

# # Asking users for their name, type of package, quantity and price per item
# full_name = input("What is your full name? ").strip().title()
# package_type = input("Enter your package type: ").lower().strip()
# quantity = int(input("How many items are you delivering? "))
# price_per_item = int(input("What is the price per item? ₦"))
# confirm_payment = input("Have you paid? (yes/no): ").lower().strip()

# # Convert full name to initials
# split_name = full_name.split()
# initials = ''.join([name[0].upper() for name in split_name])

# # Set payment status
# is_paid = True if confirm_payment == "yes" else False

# # Allowed package types
# allowed_packages = ["documents", "electronics", "books", "food"]

# # Check if package type is allowed
# if package_type in allowed_packages:
#     total = quantity * price_per_item
#     print("\n--- ORDER SUMMARY ---")
#     print(f"Customer Initials: {initials}")
#     print(f"Package Type: {package_type}")
#     print(f"Total Quantity: {quantity}")
#     print(f"Total Cost: ₦{total:,}")  # Formats with comma, e.g. ₦10,000

#     if is_paid:
#         print("✅ Payment Status: Confirmed")
#     else:
#         print("❌ Payment Status: Pending")
# else:
#     print("\n❌ Sorry, this package type is not allowed on QuickPedal.")
"""
Write a code that takes user input and check if a student have been offered admission.
"""
# admision_list = ['bright', 'chika', 'okezie', 'faith', 'amanda', 'ihuoma', 'trinty', 'ben', 'ada', 'ola']
# student_name = input('What is your name? ')

# for student in admision_list:
#     if student == student_name:
#         print("you have been offered an admission")
#         break
# else:
#     print("you have not gained admission yet!")
""""
🚚 Challenge: Box Delivery Tagger
You're creating a feature for QuickPedal that helps riders identify which packages are boxes and which are not.

🎯 Your Task:
You have a list of delivery items.

Use a list comprehension to check each item.

If the item contains the word "box", tag it as "{item} ✅ Box".

If it doesn’t, tag it as "{item} ❌ Not a box".

Print the final list.
"""""

# items = ["shoe box", "documents", "parcel", "gift box", "water bottle"]

# newlist = [f"{x}" if "box" in x else f"{x} Not a box" for x in items]
# print(newlist)

"""
✅ Challenge: QuickPedal Delivery Filter & Tagger
You're building a feature that prepares a summary of delivery items.
You are given a list of packages with different names. Your goal is to:

🎯 Your Task:
Given: A list of delivery items (mixed types: allowed and not allowed).

Use list comprehension to:

Check if the item is allowed.

If it's allowed and contains the word "box" → tag as: "✅ {item} (Box Approved)"

If it's allowed but not a box → tag as: "✅ {item} (Approved)"

If it's not allowed → tag as: "❌ {item} (Not Approved)"


"""
# Packages that are allowed on Quickpedal
allowed_packages = ["documents", "small box", "electronics", "gift box", "books", "clothes", "parcel"]


delivery_items = ["small box", "fridge", "gift box", "shoe", "books", "electronics", "water bottle", "parcel"]

delivery_list = [
    f"{item} (Box Approved)" if item in allowed_packages and "box" in item
    else f"{item} (Approved)" if item in allowed_packages
    else f"{item} (Not Approved)"
    for item in delivery_items 
]

print(delivery_list)