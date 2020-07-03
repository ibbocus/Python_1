from animals import Animal


class Dog(Animal):
    species = "Canine"

    # class to create a dog
    def bark(self):
        return "woof woof"

    def run(self):
        self.mood = "happy"
        print(f"You take {self.name} for a run!\n")


class CreateDog(Dog):

    def dog():
        dog1 = Dog(name=" ", colour="black", mood="sad",
                   sleepy=True, hunger="Hungry", species=Dog.species, alive=True)

        return dog1

dog1 = CreateDog.dog()


class DogActions(CreateDog):

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