student_record = {"name": "Ibrahim",
                  "DOB": "01/01/1996",
                  "Country of Birth": "Saudi Arabia",
                  "Employee ID": "12345",
                  "Comment": "He likes football"}
def record_printer():
    for keys in student_record:
        print(keys, ":", student_record.get(keys))

# print()
#
# for keys, value in student_record.items():
#     print(keys, ":", value)
#
# print()
#
# for keys in student_record:
#     print(keys, ':', student_record[keys])
