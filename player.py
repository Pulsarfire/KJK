from items import dice
from items import Axe
from items import Knife
from inventory import Inventory

class Player:

    def __init__(self, name, health, weapon, max_health, inventory):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.max_health = max_health
        self.inventory = inventory
       

    def __str__(self):
        return f"""Character details:
        Name:   {self.name}
        Health: {self.health}
        Max HP: {self.max_health}
        Weapon: {self.weapon}"""

    #Character creator
    @classmethod
    def create(cls):
        while True:
            name = input("Input your name: ")
            if not name:
                print("Missing name.")
                continue
            else:               
                print("Then, let's decide your starting health with a D20.")
                health = dice(20)                
                if health > 8:
                    input("\nRolling... In the meantime pick a weapon.")
                else:                
                    input(f"{health}? Wow that is a terrible roll... Here have 5 hp extra. Now chose your weapon.")
                    health += 5
                inventory = Inventory.create()  
                weapon = cls.get_weapon()
                inventory.add_item(weapon)
                max_health = health
                return Player(name, health, weapon, max_health, inventory)


    @classmethod            
    def get_weapon(cls):
        while True:
            user_input = input("\n(1) Axe: D6 with crit. (2) Knife: D8 without crit.\n").strip()
                            
            if user_input == "1":
                return Axe()
            elif user_input == "2":
                return Knife()           
            else: 
                print("Incorrect input.")
                continue