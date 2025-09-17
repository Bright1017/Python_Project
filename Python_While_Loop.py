# While Loops in Python

# i = 0
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1
#     continue


# QuickPedal Rider Delivery Search Simulation

# available_requests = [
#     {"pickup": "Market Square", "drop": "Central Park"},
#     {"pickup": "Mall Junction", "drop": "City Center"},
#     {"pickup": "University Gate", "drop": "Downtown"},
# ]

# preferred_location = "Mall Junction"
# i = 0

# while i < len(available_requests):
#     request = available_requests[i]
#     print(f"Checking request {i+1}: Pickup at {request['pickup']}")

#     if request["pickup"] == preferred_location:
#         print(f"Match found! Pickup: {request['pickup']} → Drop: {request['drop']}")
#         break
#     i += 1
# else:
#     print("No matching requests found. Try again later.")


import random
# def read_speedometer():
#     speed = random.randint(30, 130)
#     print(f"Speedometer reading: {speed} km/h")
#     return speed


# def check_speed_limit(limit=80):
#     speed = read_speedometer()
#     if speed > limit:
#         print("You are over speeding! Slow down.")

# check_speed_limit()


"""
📝 Task: QuickPedal Fuel Check Simulation

Imagine QuickPedal wants to monitor rider fuel level (instead of speed).

Write a function read_fuel_gauge() that:

Randomly returns a number between 0 and 100 (fuel percentage).

Prints the reading like:

Fuel gauge reading: 35%


Returns the fuel percentage.

Write another function check_fuel_level(limit=20) that:

Calls read_fuel_gauge().

If fuel is less than limit (default 20%), print:

Warning: Low fuel! Please refill.


Otherwise, print:

Fuel level is okay.


Call check_fuel_level() at the end to test it.

💡 Extra Challenge (if you want to push yourself):

Modify check_fuel_level to take rider’s name as an argument so it prints:

Chika's fuel gauge reading: 10%
Warning: Low fuel! Please refill.

"""

# def read_fuel_gauge():
#     Fuel_pencentage = random.randint(0, 130)
#     print(f"Fuel gauge reading: {Fuel_pencentage} %")
#     return Fuel_pencentage


# def check_fuel_level(level=20):
#     rider_name = input("What is your name? ")
#     Fuel_pencentage = read_fuel_gauge()
#     print(f"{rider_name}'s fuel gauge reading: {Fuel_pencentage}%")


#     if Fuel_pencentage < level:
#         print(f"{rider_name}, Warning: Low fuel! Please refill.")
#     else:
#         print(f"{rider_name}, Fuel level is okay.")

# check_fuel_level()