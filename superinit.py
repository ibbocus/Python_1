"""
This is the parent/base/super class
"""


class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary


"""
We have now created a subclass of Employee, called Developers
All developers have a first, last name and all developers have a pay
but on-top of this, developers ALSO have a main programming language
"""


class Developer(Employee):
    def __init__(self, first_name, last_name, salary, main_prog_lang):
        # By using super, we don't need to explicitly initialize the parent class
        super().__init__(first_name, last_name, salary)
        self.main_prog_lang = main_prog_lang


Employee1 = Employee("Charles", "Winston", 120_000)
Developer1 = Developer("Joe", "Smith", 120_000, "Python")
print(Employee1.first_name, Employee1.last_name)
print(Developer1.first_name, Developer1.last_name)
print(Employee1.main_prog_lang)
