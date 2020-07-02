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
if age > 17:
    print("These are the movies you can watch:", classifications)
elif 14 < age < 18:
    print("These are the movies you can watch:", classifications[0:4])
elif 11 < age < 15:
    print("These are the movies you can watch:", classifications[0:3])
else:
    print("These are the movies you can watch:", classifications[0:2])
