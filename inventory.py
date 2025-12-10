from items import Axe
from items import Knife

class Inventory:

    def __init__(self, inventory):
        self.inventory = inventory

    def __str__(self):
        return self.browse_inv()

    def weapon(self):

        result = []
        for item in self.inventory:
            if isinstance(item, (Axe, Knife)):
                result.append(item)
        return result
        
    def browse_inv(self):
        result = []
        for i, item in enumerate(self.inventory):
            if isinstance(item, Axe):
                result.append(f"{i + 1}. {item}")

            else:
                for key, value in item.items():
                    result.append(f"{i + 1}. {key}: {value}")
        return "\n".join(result)    

    def add(self, addition):
        self.inventory.append(addition)

    @classmethod
    def create(cls):
        inventory = []
        return cls(inventory)                


