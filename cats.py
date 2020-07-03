from animals import Animal


class Cat(Animal):
    species = "Feline"

    def meow(self):
        return print("Meow meow")

    def play(self):
        self.mood = "happy"
        return print("you play with the cat!")


class CreateCat(Cat):

    def cat():
        cat1 = Cat(name=" ",
                   colour="black",
                   mood="mad",
                   hunger="starving",
                   sleepy=True,
                   species=Cat.species,
                   alive=True
                   )
        return cat1


cat1 = CreateCat.cat()


class CatActions(CreateCat):
    def action(self):
        if cat1.alive == True:
            player_action = self
            if player_action == "name cat":
                cat1.change_name()
            if player_action == "feed cat":
                cat1.feed()
            if player_action == "play with cat":
                cat1.play()
            if player_action == "put cat to bed":
                cat1.sleep()
            if player_action == "check status":
                cat1.check_status()
            if player_action == "kill cat":
                cat1.kill()
            if player_action == "show cat":
                cat1.meow()
            if player_action == "help":
                print("List of commands as follows:")
                print("feed cat")
                print("play with cat")
                print("put cat to bed")
                print("check status")
                print("kill cat")
                print("show cat")
            else:
                pass