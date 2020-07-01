# A dictionary is a data collection
# more dynamic than tuples and lists
# simple concept of key value pairs

student_record = {"name": "Ibrahim",
                  "stream": "Devops",
                  "completed_lessons": 5,
                  "completed_lessons_names": ["strings", "Tuples", "variables"]}

rent = {'London': 5600.00, 'Paris': 3500.00, 'Tokyo': 5000.00}
print(rent)
total_income: float = 0.00
for value in rent.values():
    total_income += value  # Accumulate the values in total_income
print("total income:", total_income)
v = list(rent.values())
k = list(rent.keys())
print("The city with the largest rent is:", k[v.index(max(v))])
# Alternative method to retrieve a specific value from a key
print("The city with the lowest rent is:", min(rent, key=rent.get))

student_record = {"name": "Ibrahim",
                  "stream": "Devops",
                  "completed_lessons": 5,
                  "completed_lessons_names": ["strings", "Tuples", "variables"]}

print(student_record["completed_lessons_names"][2])
print(student_record["name"])
print(student_record["completed_lessons"])

student_record["completed_lessons_names"].extend(["operators", "dictionaries", "append", "extend"])
print(student_record)














