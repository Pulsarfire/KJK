import sys
import random
from items import dice
from items import Axe
from items import Knife
from items import Cross
from items import Paper
from monsters import Vampire
from monsters import Werewolf
from monsters import Alfred

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
        
        while True:
            user_choice = action("(E)xplore the room", "(W)ine room", "(S)tudy room")
            match user_choice:
                case "E":
                    cls.search(player)                    
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
                    cls.entry(player)
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

    #Healing.
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
                input("Your health is currently at a maximum, no point of drinking it.")


            cls.is_searched = True
            cls.entry(player)
        else:
            input("There is nothing else interesting in the room.")
            cls.entry(player)


    @classmethod
    def valid_options(cls, player):
        
        while True:
            user_choice = action("(E)xplore the room", "(C)igar lounge", "(M)aster bedroom", "(L)ibrary")
            match user_choice:
                case "E":
                    cls.search(player)                    
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
                    cls.entry(player)
                    break
                case _:
                    print("Invalid input.")
                    continue

class Study:
    
    study_first = True

    @classmethod
    def entry(cls, player):
        if cls.study_first:
            input("""
            Upon entering the study in a manor, you step into a hushed, richly paneled room lined with leather-bound books,
            where a heavy oak desk sits beneath a tall window, illuminated by soft, natural light. The air carries the scent
            of old paper and polished wood, evoking an atmosphere of quiet intellect and timeless refinement.
            \n""")
            cls.fight(player)
            cls.study_first = False
        else:
            input("""
            Upon looking at the study again, you notice subtle details you missed before—a faint smudge on the windowpane,
            a book slightly ajar on the shelf, or the way the light now glints off an old candle holder. You have two new doors
            in front of you. One of them leads you to the guest room the other one to the kitchen.
            \n""")
            cls.valid_options(player)
        
    @classmethod
    def fight(cls, player):
        opponent = random.choice(["Vampire", "Werewolf"])
        input(f"You notice something else too. From the corner of the room a shadow emerges. It is a {opponent}!")
        if opponent == "Vampire":
            fight_func(player, Vampire.create())
        else:
            fight_func(player, Werewolf.creat())

    @classmethod
    def valid_options(cls, player):
        
        while True:
            user_choice = action("(G)uest room", "(K)itchen", "(L)ibrary")
            match user_choice:
                case "G":
                    Guest_room.entry(player)
                    break
                case "K":
                    Kitchen.entry(player)
                    break
                case "L":
                    Library.entry(player)
                    break
                case "I":
                    print(player.inventory)
                    input()
                    cls.entry(player)
                    break
                case _:
                    print("Invalid input.")
                    continue
    
class Cigar_lounge:

    cigar_lounge_first = True
    is_searched = False
    
    @classmethod
    def entry(cls, player):
        if cls.cigar_lounge_first:
            input("""
            The heavy oak door opens to a warm embrace of cedar and aged tobacco, with amber light illuminating leather chairs and a glowing humidor.
            Jazz hums softly as patrons sip whiskey, their cigars burning like embers in the dim, welcoming haze. No further doors ahead.
            \n""")
            cls.cigar_lounge_first = False
            cls.valid_options(player)
        else:
            input("""
            The chair is warm, the ashtray bears a fresh extinguished cigar—yours?—and the air holds a lingering breath of smoke.
            \n""")
            cls.valid_options(player)

    @classmethod
    def search(cls, player):
        if not cls.is_searched:
            input("You found a Cross. It looks interesting, so you put it away.")
            player.inventory.add_item(Cross())
            cls.is_searched = True
            cls.entry(player)
        else:
            input("There is nothing else interesting in the room.")
            cls.entry(player)

    @classmethod
    def valid_options(cls, player):
        
        while True:
            user_choice = action("(E)xplore the room", "(W)ine Room")
            match user_choice:
                case "E":
                    cls.search(player)
                    break
                case "W":
                    Wine_room.entry(player)
                    break
                case "I":
                    print(player.inventory)
                    input()
                    cls.entry(player)
                    break
                case _:
                    print("Invalid input.")
                    continue

    

class Master_bedroom:

    master_bedroom_first = True
    
    @classmethod
    def entry(cls, player):
        if cls.master_bedroom:
            input("First entry.")
            cls.master_bedroom = False
        else:
            input("Not first entry.")

class Kitchen:

    kitchen_first = True
    
    @classmethod
    def entry(cls, player):
        if cls.kitchen_first:
            input("""
            You step into the kitchen, and it looks like the most ordinary one you've ever seen.
            There is nothing interesting here but it feels like this is the central hub of the house. 
            You've got a couple of doors here.
            \n""")
            cls.kitchen = False
            cls.valid_options(player)
        else:
            input("""
            Nothing has changed here. The most interesting thing is the fly on the wall.
            \n""")
            cls.valid_options(player)

    @classmethod
    def valid_options(cls, player):
        
        while True:
            user_choice = action("(S)tudy room", "(M)aster bedroom", "(G)uest room",)
            match user_choice:
                case "S":
                    Study.entry(player)
                    break
                case "M":
                    Master_bedroom.entry(player)
                    break
                case "G":
                    Guest_room.entry(player)
                    break
                case "I":
                    print(player.inventory)
                    input()
                    cls.entry(player)
                    break
                case _:
                    print("Invalid input.")
                    continue

class Guest_room:

    guest_room_first = True
    is_searched = False
    
    @classmethod
    def entry(cls, player):
        if cls.guest_room_first:
            input("""
            You step into the small guest room and immediately notice its snug,
            welcoming charm—soft light filters through simple curtains, and a 
            neatly made bed with fresh linens stands against one wall.
            \n""")
            cls.guest_room = False
            cls.valid_options(player)
            
        else:
            input("""
            It is quite obvious the room hasn't been used that often recently. You don't
            think there have been many guests here over the past few years.
            \n""")
            cls.valid_options(player)

    @classmethod
    def search(cls, player):
        if not cls.is_searched:
            input("You found a piece of paper. It has some kind of incantation on it. It reads: Abracadabra Ignis Crux.")
            player.inventory.add_item(Paper())
            cls.is_searched = True
            cls.entry(player)
        else:
            input("There is nothing else interesting in the room.")
            cls.entry(player)

    @classmethod
    def valid_options(cls, player):
        
        while True:
            user_choice = action("(E)xplore the room", "(S)tudy Room", "(K)itchen")
            match user_choice:
                case "E":
                    cls.search(player)
                    break
                case "S":
                    Study.entry(player)
                    break
                case "K":
                    Kitchen.entry(player)
                    break
                case "I":
                    print(player.inventory)
                    input()
                    cls.entry(player)
                    break
                case _:
                    print("Invalid input.")
                    continue

class Hidden_room:
    ...