from animals import Animal


class Dog(Animal):
    species = "Canine"

    # class to create a dog
    def bark(self):
        return "woof woof"

    def run(self):
        self.mood = "happy"
        print(f"You take {self.name} for a run!\n")

    def dog(self):
        dog1 = Dog(name=input("What would you like to name your dog? "), colour="black", mood="sad",
                   sleepy=True, hunger="Hungry", species=Dog.species, alive=True)

dog1 = Dog.dog()
