# name = input("Please Enter Your Name")
# while True:
#     try:
#         age = int(input("Please Enter Your Age"))
#         if age < 1 or age > 50:
#             raise ValueError  # this will send it to the print message and back to the input option
#         break
#     except ValueError:
#         print("Invalid integer. The number must be in the range of 1-50.")
# print(name)
# print(age)
#Exercise 1: Capturing User Details

first_name = input("Please Enter Your First Name")
last_name = input("Please Enter Your Last Name")
full_name = first_name + ' ' + last_name
print(full_name)
age = input("Please Enter Your age")
address = input("Please Enter Your Address")

print(full_name, '/', age, '/', address)