from dogs import *
from cats import *


def start_game():
    user_choice = input("cat or dog?")
    if user_choice == "dog":
        dog1.alive = True

    elif user_choice == "cat":
        cat1.alive = True
    print("ENTER 'help' FOR LIST OF COMMANDS")
    if dog1.alive == True:
        player_action = "name dog"
        DogActions.action(self=player_action)
    elif cat1.alive == True:
        player_action = "name cat"
        CatActions.action(self=player_action)
    while dog1.alive == True or cat1.alive == True:
        player_action = input("What would you like to do?")
        DogActions.action(self=player_action)
        CatActions.action(self=player_action)
