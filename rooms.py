from actions import action
from actions import browse_inv
from items import inventory


class Room:
    ...
    

class Library:
    
    library_first = True
    is_searched = False

    @classmethod
    def entry(cls):
        if cls.library_first:
            input("""
            You blink awake on the cold library floor, the sharp scent of 
            old paper and dust filling your nose as your head pounds.
            Books lie scattered around you like fallen soldiers, a silent 
            testament to the struggle that left you here, alone in the dim, quiet stacks.
            You also see two doors, one of them is for the Study and the other is for the Wine room.
            \n""")
            cls.library_first = False
            cls.valid_options()

        else:
            input("""
            This stillness makes the room feel less like a place and more like a trap, 
            holding you in the moment of impact, refusing to let the story continue.
            \n""")
            cls.valid_options()
            


    @classmethod
    def search(cls):
        if not cls.is_searched:
            input("You found a note that has '3714' on it.")
            inventory.append({"Note": "3714"})
            cls.is_searched = True
            cls.entry()
        else:
            input("There is nothing else interesting in the room.")
            cls.entry()

    @classmethod
    def valid_options(cls):
        user_choice = action("(E)xplore the room", "(W)ine room", "(S)tudy room")

        while True:
            match user_choice:
                case "E":
                    Library.search()                    
                    break
                case "W":
                    Wine_room.entry()
                    break
                case "S":
                    Study.entry()
                    break
                case "I":
                    browse_inv()
                    Library.entry()
                    break
                case _:
                    print("Invalid input.")
                    continue

class Wine_room:

    wine_room_first = True
    is_searched = False

    @classmethod
    def entry(cls):
        if cls.wine_room_first:
            input("""
            You enter a cool, dimly lit room lined with wooden racks holding rows of wine bottles,
            the air rich with the scent of oak and grapes. Faint candlelight glimmers off the glass,
            and a rustic table stands in the center, ready for tasting.You also see two new doors, one of them 
            is for the Cigar lounge and the other is for the Master bedroom.
            \n""")
            cls.wine_room_first = False
            cls.valid_options()
        else:
            input("""
            You look around in the wine room, its familiar oak-scented air and dim glow now tinged with 
            anticipation as you eye the racks for hidden clues or a forgotten bottle.
            \n""")
            cls.valid_options()

    #Picking up a potion.
    @classmethod
    def search(cls):
        if not cls.is_searched:
            input("You found a potion which can heal you for 10 hp. ")
            inventory.append("Potion")
            cls.is_searched = True
            cls.entry()
        else:
            input("There is nothing else interesting in the room.")
            cls.entry()


    @classmethod
    def valid_options(cls):
        user_choice = action("(E)xplore the room", "(C)igar lounge", "(M)aster bedroom", "(L)ibrary")

        while True:
            match user_choice:
                case "E":
                    Wine_room.search()                    
                    break
                case "C":
                    Cigar_lounge.entry()
                    break
                case "M":
                    Master_bedroom.entry()
                    break
                case "L":
                    Library.entry()
                    break
                case "I":
                    browse_inv()
                    Wine_room.entry()
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

