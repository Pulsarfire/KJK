import random

inventory = []

#Reusable code for any dice
def dice(side):
    while True:
        user_input = input(f"Press enter to roll the {side} sided dice.")
        if user_input == "":
            return random.randint(1, side)
        else:
            print("Incorrect input.")
            continue

class Axe:

    def __init__(self):
        ...

    @classmethod
    def deal_dmg(cls):
        dmg = dice(6)
        if dmg == 6:
            dmg = int(dmg * 1.5)
            print(f"🪓🪓🪓You've dealt a critical {dmg} damage.🪓🪓🪓")
            return dmg
        else:
            print(f"🪓You've dealt {dmg} damage.🪓")
            return dmg

class Knife:
   
    @classmethod
    def deal_dmg(cls):
        dmg = dice(8)
        print(f"🔪You've dealt {dmg} damage.🔪")
        return dmg
    

class Paper:
    
    @classmethod
    def read_paper(cls):
        return f"🔥Abracadabra Ignis Crux.🔥"

class Cross:
    
    @classmethod
    def place_cross(cls):
        return f"🕆You've placed the cross.🕆"

