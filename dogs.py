from animals import Animal


class Dog(Animal):
    species = "Canine"

# class to create a dog
    def bark(self):
        return "woof woof"

    def run(self):
        self.mood = "happy"
        print(f"You take {self.name} for a run!\n")


