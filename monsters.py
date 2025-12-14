import random

class Vampire:

    def __init__(self, health):
        self.health = health
        
    @classmethod
    def create(cls):
        health = random.randint(5, 10)
        return Vampire(health)

    def dmg(self):
        x = random.randint(1, 6)
        print(f"They've dealt {x} damage.")
        return x

class Werewolf:

    def __init__(self, health):
        self.health = health

    @classmethod
    def creat(cls):
        health = random.randint(6, 12)
        return Werewolf(health)

    def dmg(self):
        x = random.randint(2, 5)
        print(f"They've dealt {x} damage.")
        return x

class Alfred:
    
    def __init__(self, health):
        self.health = health

    @classmethod
    def create(cls):
        health = random.randint(10, 15)
        return Alfred(health)

    def dmg(self):
        x = random.randint(3, 7)
        print(f"They've dealt {x} damage.")
        return x