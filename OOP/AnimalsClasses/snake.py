from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        self.cold_blooded = True
        self.forked_tongue = True
        self.venom = bool
        self.limbs = False


    def use_tongue_to_smell(self):
        print("snake uses tongue to smell")