# TUPLE
# name = ("bright", "chika", "melvin")
# new_names = list(name)
# new_names.append("okezie")
# new_names.append('Chimamanda')
# long_names = [names for names in new_names if len(names) > 6]
# print(long_names)

"""
🚴 QuickPedal Tuple Challenge

You are managing a list of QuickPedal riders stored in a tuple:

riders = ("John", "Chika", "Sandra", "Grace", "Michael", "Patricia", "Bright")

🎯 Tasks:

Convert the tuple into a list so you can modify it.

Add two new riders: "Melvin" and "Okezie".

Remove "John" from the list (he quit).

Replace "Sandra" with "Maryam".

From the updated list, create a new list long_names that only contains rider names with 7 or more characters.

Convert the updated rider list back into a tuple and print it.

Print the long_names list.
"""

# riders = ("John", "Chika", "Sandra", "Grace", "Michael", "Patricia", "Bright")

# # Converting tuple data to list data type before making modification
# riders_list = list(riders)

# # Adding new rider names to Quickpedal
# riders_list.append("Melvin")
# riders_list.append("Okezie")

# # Removing a rider that's no longer active on Quickpedal
# riders_list.remove("John")

# # Changed a rider name on Quickpedal and hard coding their name into specific index position
# riders_list[2] = "Maryam"

# # Filtering names that have seven characters
# long_names = [names for names in riders_list if len(names) > 6]
# print(tuple(riders_list))
# print("Names that have seven characters are:", long_names)

# digits = list(range(10))
# print(digits)
# even_digits = [number for number in range(1, 10) if number % 2 == 0]
# print(even_digits)

# combs = []

# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x,y))

# print(combs)


# combs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x >= y]
# print(combs)

# combs = []

# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x == y:
#             combs.append((x,y))

# print(combs)

# personal_info = ("bright", (+2349036628832), "lagos")


# for i in range(len(personal_info)):
#     print(personal_info[i])


# i = 10
# total = 0
# while i > 0 :
#     total += i
#     i -= 1
#     print(total)


# DICTIONARIES IN PYTHON

# config = {
#     "color": "green",
#     "width": 42,
#     "height": 100,
#     "font": "Bold"
# }

# x = config.keys()
# print(x)

# riders = {

#     "Roo1":{"name":"chika","deliveries": 45,"wallet": 5000},
#     "Roo2":{"name":"mary","deliveries": 30,"wallet": 2000},
#     "Roo3":{"name":"ahmed","deliveries": 55,"wallet": 4000}
# }

# x = riders.get("Roo1")
# print(x)

# # Increased chika's delivery by 5
# riders["Roo1"]["deliveries"] += 5

# # increased mary's wallet balance by 1000
# riders["Roo2"]["wallet"] += 1000

# # Added a new rider in the dictonary 
# riders["Roo4"] = {"name":"bright","deliveries": 10,"wallet": 7000}

# # deleting Ahmed from the rider's dictionary
# del riders["Roo3"]

# # Printing out all rider's name from the dictionary
# for rider_id, details in riders.items():
#     print(details["name"])

# for rider_id, details in riders.items():
#      print(f"{details['name']} - Wallet Balance: ₦{details['wallet']}")

# # Checking if "Roo5" is avialable in the dictionary
# if "Roo5" in riders:
#     print("Yes, we have Roo5 in the rider's dictionary")
# else:
#     print("We don't have Roo5 in the dictionary")

# top_rider = max(riders.values(), key=lambda x: x["deliveries"])
# print(f"Top Performer: {top_rider['name']} with {top_rider['deliveries']} deliveries")

# print(riders)

"""
📌 QuickPedal Dictionary Task

You’re managing QuickPedal’s riders database. Complete the following using Python dictionaries:

riders = {
    "Roo1": {"name": "Chika", "deliveries": 45, "wallet": 5000},
    "Roo2": {"name": "Mary", "deliveries": 30, "wallet": 2000},
    "Roo3": {"name": "Ahmed", "deliveries": 55, "wallet": 4000},
    "Roo4": {"name": "Bright", "deliveries": 10, "wallet": 7000},
}

✅ Your Tasks:

Add a new rider → Roo5: name = Grace, deliveries = 20, wallet = 2500.

Update wallet → Add ₦2000 to Mary’s wallet.

Remove a rider → Bright leaves QuickPedal, remove Roo4.

Total Deliveries → Calculate how many deliveries all riders made combined.

Find Richest Rider → Print rider with the highest wallet balance.

Export Summary → Loop through and print in this format:
"""


# riders = {
#     "Roo1": {"name": "Chika", "deliveries": 45, "wallet": 5000},
#     "Roo2": {"name": "Mary", "deliveries": 30, "wallet": 2000},
#     "Roo3": {"name": "Ahmed", "deliveries": 55, "wallet": 4000},
#     "Roo4": {"name": "Bright", "deliveries": 10, "wallet": 7000},
# }

# # Added a new rider in the dictionary
# riders["Roo5"] = {"name": "Grace", "deliveries": 20, "wallet": 2500}
# riders["Roo2"]["wallet"] += 2000
# del riders["Roo3"]

# number1 = 10
# number2 = 5

# x = number1 + number2
# print(f"Addtion of {number1} and {number2} is {x}")

