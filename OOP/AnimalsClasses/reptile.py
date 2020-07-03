from animal1 import Animal

class Reptile(Animal):
    def __init__(self):
        self.cold_blooded = bool
        self.tetrapod = bool
        self.heart_chambers = [3, 4]
        self.eat = bool

    # this initialises the characteristics of the animal
    def seek_heat(self):
        print("heat seeking reptile")

    def hunt(self):
        print("this reptile hunts")

    def use_venom(self):
        print("venom attack")

    def attract_mate_through_scent(self):
        print("reptile uses pickup line")