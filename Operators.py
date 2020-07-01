# print(15 % 2)
#
# print("Ib's classroom")
# print('Ib\'s classroom')
#
# # The slash escapes the apostrophe
#
greeting = 'Hello World yeet'
# print(len(greeting))
# print(greeting[::-1])
# print(greeting[0:5])
# print(greeting[6:])
print(greeting[-5:])
print(greeting[-6:-11])

remove_white_space = "remove space at end of string                    "
print(len(remove_white_space))
print(len(remove_white_space.strip()))

print(greeting.count('l'))

print(greeting.upper())
print(greeting.lower())
print(greeting.endswith('yeet'))

print(greeting.join(remove_white_space))