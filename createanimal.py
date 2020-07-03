from animals import Animal
from dogs import Dog
from cats import Cat


class CreatePet(Animal):

    def dog():
        dog1 = Dog(name=" ", colour="black", mood="sad",
                   sleepy=True, hunger="Hungry", species=Dog.species, alive=True)

        return dog1

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


class DogActions(CreatePet):

    def action(self):
        if dog1.alive == True:
            player_action = self
            if player_action == "name dog":
                dog1.change_name()
            if player_action == "feed dog":
                dog1.feed()
            if player_action == "play with dog":
                dog1.run()
            if player_action == "put dog to bed":
                dog1.sleep()
            if player_action == "check status":
                dog1.check_status()
            if player_action == "kill dog":
                dog1.kill()
            if player_action == "show cat":
                dog1.bark()
            if player_action == "help":
                print("List of commands as follows:")
                print("feed dog")
                print("play with dog")
                print("put dog to bed")
                print("check status")
                print("kill dog")
                print("show cat")
            else:
                pass


cat1 = CreatePet.cat()

dog1 = CreatePet.dog()


class CatActions(CreatePet):
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
