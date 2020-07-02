class Employees:
    raise_amount = 1.05

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + "." + last + "@techltd.com"

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def give_raise(self):
        self.salary = (self.salary * self.raise_amount)


class Developers(Employees):
    raise_amount = 1.10
    def new_dev(self):
        dev2 = (input("first name?"),input("last name?"),input("salary?"))

    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_lang = prog_lang


emp1 = Employees("Andrew", "Osborne", 120_000.00)
dev1 = Developers("Ib", "Bocus", 100_000.00, "Python")
dev
emp1.give_raise()
dev1.give_raise()
print(int((dev1.salary)))
print(int(emp1.salary))
print(dev1.full_name())

