from snake import Snake


class Python(Snake):
    def __init__(self):
        self.large = True
        self.two_lungs = True
        self.venom = True

    def digest_large_prey(self):
        print("yum")

    def constrict(self):
        print("squeeze")

    def climb(self):
        print("up the tree")

    def shed_skin(self):
        print("new clothes")
