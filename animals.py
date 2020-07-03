class Animal:
    def __init__(self, name, colour, mood, hunger, sleepy, species, alive):
        self.name = "name"
        self.colour = colour
        self.mood = mood
        self.hunger = "hungry"
        self.sleepy = sleepy
        self.species = species
        self.alive = False

    # this initialises the characteristics of the animal
    def feed(self):
        self.hunger = "full"
        print(f"You give {self.name} a big bowl of food!\n")

    def change_name(self):
        self.name = input(f"What would you like to name your animal?")

    def kill(self):
        self.alive = False
        print(f"You kill {self.name}!\n")

    def sleep(self):
        self.sleepy = False
        print(f"zzzzzz\n {self.name} takes a long nap!\n")

    def check_status(self):
        print(f"is {self.name} sleepy?", self.sleepy)
        print(f"How is {self.name}'s hunger levels?", self.hunger)
        print(f"what is {self.name}'s mood?", self.mood)
        print(f"what species is {self.name}?", self.species)
        print(f"What colours is {self.name}?", self.colour, "\n")
        return
