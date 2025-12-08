class Inventory:

    def __init__(self, inventory):
        self.inventory = inventory

    def __str__(self):
        return self.browse_inv()

    
    def browse_inv(self):
        result = []
        for i, item in enumerate(self.inventory):
            if isinstance(item, str):
                result.append(f"{i + 1}. {item}")

            else:
                for key, value in item.items():
                    result.append(f"{i + 1}. {key}: {value}")
        return "\n".join(result)            

    @classmethod
    def create(cls):
        inventory = []
        return cls(inventory)                


