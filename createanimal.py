from animals import Animal
from dogs import dog1








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

