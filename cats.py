from animals import Animal


class Cat(Animal):
    species = "Feline"

    def meow(self):
        return print("Meow meow")

    def play(self):
        self.mood = "happy"

    def cat():
        cat1 = Cat(name="fluffy",
                   colour="black",
                   mood="mad",
                   hunger="starving",
                   sleepy=True,
                   species=Cat.species,
                   alive=True
                   )

Cat.cat()
