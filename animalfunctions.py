from animals import Animal
from dogs import Dog
from cats import Cat


class CreatePet(Animal):

    def dog():
        dog1 = Dog(name=input("What would you like to name your dog? "), colour="black", mood="sad",
                   sleepy=True, hunger="Hungry", species=Dog.species, alive=True)

        return dog1

    def cat():
        cat1 = Cat(name=input("What would you like to name your cat? "),
                   colour="black",
                   mood="mad",
                   hunger="starving",
                   sleepy=True,
                   species=Cat.species,
                   alive=True
                   )
        return cat1


dog1 = CreatePet.dog()


class PlayerActions(CreatePet):

    def action(self):
        player_action = self
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