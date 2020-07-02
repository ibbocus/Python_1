# A dictionary is a data collection
# more dynamic than tuples and lists
# simple concept of key value pairs

student_record = {"name": "Ibrahim",
                  "stream": "Devops",
                  "completed_lessons": 5,
                  "completed_lessons_names": ["strings", "Tuples", "variables"]}

student_record = {"name": "Ibrahim",
                  "stream": "Devops",
                  "completed_lessons": 5,
                  "completed_lessons_names": ["strings", "Tuples", "variables"]}

print(student_record["completed_lessons_names"][2])
print(student_record["name"])
print(student_record["completed_lessons"])

student_record["completed_lessons_names"].extend(["operators", "dictionaries", "append", "extend"])
print(student_record)
print(student_record.get("name"))














