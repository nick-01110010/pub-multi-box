class Item:

    def __init__(self, name, level, equip_effects = None, active_effects = None):
        self.name = name
        self.level = level
    
    def get_item_name(self):
        return self.name
    
    def get_item_level(self):
        return self.level
    

class Device(Item):
    pass

class Engine(Item):
    pass

class Projectile(Item):
    pass

class Reactor(Item):
    pass

class Shield(Item):
    pass

class Weapon(Item):
    pass