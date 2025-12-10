import sys
import random
from items import inventory
from items import dice
from items import Axe
from items import Knife



#Reusable code for optional number of actions 
#How to use: action("(O)pen", "(C)lose")
def action(first, second=0, third=0, fourth=0):
    options = [first]
    if second:
        options.append(second)
    if third:
        options.append(third)
    if fourth:
        options.append(fourth)  

    for i in range(len(options)):
        print(options[i])
    print("(I)nventory") 
    valid_options = [first[1]]
    if second:
        valid_options.append(second[1])
    if third:
        valid_options.append(third[1])
    if fourth:
        valid_options.append(fourth[1])    

    while True:
        user_input = input("What do you want to do? ").upper().strip()  
        if user_input in valid_options or user_input == "I":
            return user_input
        else:
            print("Invalid input.")
        
#Reusable code for 1v1 fight
def fight_func(player, opponent):
    
    initiative_result = initiative()

    if initiative_result:
        while True:
            player_turn(player, opponent)
            if opponent.health <= 0:
                print("Congratulations, you killed the beast.\n")  
                break
            opponent_turn(player, opponent)
            if player.health <= 0:
                print("You died. Game over.")
                sys.exit()
    else:
        while True:
            opponent_turn(player, opponent)
            if player.health == 0:
                print("You died. Game over.\n")
                sys.exit()
            player_turn(player, opponent)
            if opponent.health == 0:
                print("Congratulations, you killed the beast.\n")  
                break
            
def player_turn(player, opponent):

    for item in player.inventory.weapon():
        if isinstance(item, Axe):
            opponent.health -= Axe.deal_dmg()
            if opponent.health < 0:
                opponent.health = 0
            print(f"Their health is {opponent.health}.\n")
          
        else:
            opponent.health -= Knife.deal_dmg()
            if opponent.health < 0:
                opponent.health = 0
            print(f"Their health is {opponent.health}.\n")
        
def opponent_turn(player, opponent):

    user_input = input("\nPress enter for your opponent's turn.")
    player.health -= opponent.dmg()
    if player.health < 0:
        player.health = 0
    print(f"Your health is {player.health}.\n")
            
#Who starts the battle
def initiative():
    print("\nLet's decide who starts the fight!")
    player = dice(20)
    print(f"\nYou rolled {player}.")
    opponent = random.randint(1, 20)
    print(f"They rolled {opponent}.\n")
    if player >= opponent:
        print("Thanks to your quick reflexes you start the battle.")
        return True
    else:
        print("Your opponent seems to be quicker than you. They start the battle.")
        return False

#Browse inventory(old code, probably needs deleting at some point.)
def browse_inv():
    for i, item in enumerate(inventory):
        if isinstance(item, str):
            print(f"{i + 1}. {item}")

        else:
            for key, value in item.items():
                print(f"{i + 1}. {key}: {value}")

    if "Potion" in inventory:
        user_choice = input("Would you like to drink your potion? (Y/N)").upper().strip()
        if user_choice == "Y":
            inventory.remove("Potion")
            #player.health += 10


