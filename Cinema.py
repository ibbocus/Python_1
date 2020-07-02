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
