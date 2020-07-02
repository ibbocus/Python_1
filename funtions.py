# What is a function
# why should we use functions?
# what is the benefit - reusability!
# What functions have we used
# DRY - Don't Repeat Yourself
# functions should be simple and basic, very easy to describe.
from Cinema import age_checker
from EmployeeRecord import record_printer

def greeting():
    name = input("What's your name? ")
    return f"Hello {name}!"


# this gives the function a value of the string, which will need to be accessed by print(greeting())
age = int(input("What is your age?:"))
age_checker(age)

def square(n1):
    return n1*n1

print(square(5))
