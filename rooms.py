import sys
import random
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

#Rooms:

class Library:
    
    library_first = True
    is_searched = False

    @classmethod
    def entry(cls, player):
        if cls.library_first:
            input("""
            You blink awake on the cold library floor, the sharp scent of 
            old paper and dust filling your nose as your head pounds.
            Books lie scattered around you like fallen soldiers, a silent 
            testament to the struggle that left you here, alone in the dim, quiet stacks.
            You also see two doors, one of them is for the Study and the other is for the Wine room.
            \n""")
            cls.library_first = False
            cls.valid_options(player)

        else:
            input("""
            This stillness makes the room feel less like a place and more like a trap, 
            holding you in the moment of impact, refusing to let the story continue.
            \n""")
            cls.valid_options(player)
            


    @classmethod
    def search(cls, player):
        if not cls.is_searched:
            input("You found a note that has '3714' on it.")
            player.inventory.add_item({"Note": "3714"})
            cls.is_searched = True
            cls.entry(player)
        else:
            input("There is nothing else interesting in the room.")
            cls.entry(player)

    @classmethod
    def valid_options(cls, player):
        user_choice = action("(E)xplore the room", "(W)ine room", "(S)tudy room")

        while True:
            match user_choice:
                case "E":
                    Library.search(player)                    
                    break
                case "W":
                    Wine_room.entry(player)
                    break
                case "S":
                    Study.entry(player)
                    break
                case "I":
                    print(player.inventory)
                    input()
                    Library.entry(player)
                    break
                case _:
                    print("Invalid input.")
                    continue


class Wine_room:

    wine_room_first = True
    is_searched = False

    @classmethod
    def entry(cls, player):
        if cls.wine_room_first:
            input("""
            You enter a cool, dimly lit room lined with wooden racks holding rows of wine bottles,
            the air rich with the scent of oak and grapes. Faint candlelight glimmers off the glass,
            and a rustic table stands in the center, ready for tasting.You also see two new doors, one of them 
            is for the Cigar lounge and the other is for the Master bedroom.
            \n""")
            cls.wine_room_first = False
            cls.valid_options(player)
        else:
            input("""
            You look around in the wine room, its familiar oak-scented air and dim glow now tinged with 
            anticipation as you eye the racks for hidden clues or a forgotten bottle.
            \n""")
            cls.valid_options(player)

    #Picking up a potion.
    @classmethod
    def search(cls, player):
        if not cls.is_searched:
            input("You found a potion which can heal you for 10 hp. ")
            if player.health < player.max_health:
                while True:
                    user_choice = input("Would you like to drink the potion?(You can't overheal.) (Y/N)").upper().strip()
                    if user_choice == "Y":
                        player.health += 10
                        if player.health > player.max_health:
                            player.health = player.max_health
                        print(f" Your health is {player.health}.")
                        input()
                        break
                    elif user_choice == "N":
                        input("You decide it is not worth drinking it yet, but might be a good idea to remember the location.")
                        break
                    else:
                        input("Invalid input.")
                        continue

                    
            else:
                print("Your health is currently at a maximum, no point of drinking it.")


            cls.is_searched = True
            cls.entry(player)
        else:
            input("There is nothing else interesting in the room.")
            cls.entry(player)


    @classmethod
    def valid_options(cls, player):
        user_choice = action("(E)xplore the room", "(C)igar lounge", "(M)aster bedroom", "(L)ibrary")

        while True:
            match user_choice:
                case "E":
                    Wine_room.search(player)                    
                    break
                case "C":
                    Cigar_lounge.entry(player)
                    break
                case "M":
                    Master_bedroom.entry(player)
                    break
                case "L":
                    Library.entry(player)
                    break
                case "I":
                    print(player.inventory)
                    input()
                    Wine_room.entry(player)
                    break
                case _:
                    print("Invalid input.")
                    continue

class Study:
    
    study_first = True

    @classmethod
    def entry(cls):
        if cls.study_first:
            input("First entry.")
            cls.study_first = False
        else:
            input("Not first entry.")

class Cigar_lounge:

    cigar_lounge_first = True
    
    @classmethod
    def entry(cls):
        if cls.cigar_lounge_first:
            input("First entry.")
            cls.cigar_lounge_first = False
        else:
            input("Not first entry.")

class Master_bedroom:

    master_bedroom = True
    
    @classmethod
    def entry(cls):
        if cls.master_bedroom:
            input("First entry.")
            cls.master_bedroom = False
        else:
            input("Not first entry.")

class Kitchen:

    kitchen = True
    
    @classmethod
    def entry(cls):
        if cls.kitchen:
            input("First entry.")
            cls.kitchen = False
        else:
            input("Not first entry.")

class Guest_room:

    guest_room = True
    
    @classmethod
    def entry(cls):
        if cls.guest_room:
            input("First entry.")
            cls.guest_room = False
        else:
            input("Not first entry.")

class Hidden_room:
    ...

