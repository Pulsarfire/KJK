from player import Player
from rooms import Library

def main():
    input("\nWelcome to my game! Any time you want the game to progress after a text just press enter to continue.(Like now.)\n") 
    player = Player.create()
    print(player)
    input("Good luck! Press enter to continue.")
    Library.entry(player)
    
    

if __name__ == "__main__":
    main()

