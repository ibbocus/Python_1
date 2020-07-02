from animals import Animal
class Cat(Animal):
    species = "Feline"

    def meow(self):
        return print("Meow meow")

    def play(self):
        self.mood = "happy"
