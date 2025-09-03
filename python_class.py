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