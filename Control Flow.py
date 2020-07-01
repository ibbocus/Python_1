# What is Control flow
# Conditional Statements and Loops

# if, elif, else, for loop, while loop
import random

lucky_number = random.randint(1, 10)

while True:
    try:
        guess = int(input("Pick a number between 1 and 10!"))
        if guess < 1 or guess > 10:
            raise ValueError  # this will send it to the print message and back to the input option
        break
    except ValueError:
        print("Invalid integer. The number must be in the range of 1-10.")
if guess == lucky_number:
    print("lucky guess!")
else:
    print("unlucky!")

age = int(input("What is your age?:"))
classifications = ["U", "PG", "12a", "15", "18"]
if age >18:
    print("These are the movies you can watch:", classifications)
elif 14 < age < 18:
    print("These are the movies you can watch:", classifications[0:4])
elif 11 < age < 15:
    print("These are the movies you can watch:", classifications[0:3])
else:
    print("These are the movies you can watch:", classifications[0:2])




# rent = {'London': 5600.00, 'Paris': 3500.00, 'Tokyo': 5000.00}
# print(rent)
# total_income: float = 0.00
# for value in rent.values():
#     total_income += value  # Accumulate the values in total_income
# print("total income:", total_income)
# v = list(rent.values())
# k = list(rent.keys())
# print("The city with the largest rent is:", k[v.index(max(v))])
# # Alternative method to retrieve a specific value from a key
# print("The city with the lowest rent is:", min(rent, key=rent.get))

#
# weather = "sunny"
# if weather == "sunny":
#     print("go to the beach")
# else:
#     print("stay home")