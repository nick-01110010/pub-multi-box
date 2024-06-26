from item import Item

class Character:

    characters = 0
        
    def __init__(self, name, password, character_class, formation_position):
        self.name = name
        self.password = password
        self.character_class = character_class
        self.formation_position = formation_position
        
        Character.characters += 1
            
    def get_name(self):
        return self.name
    
    def get_password(self):
        return self.password

    def get_character_class(self):
        return self.character_class

    def get_formation_position(self):
        return self.character_class

class WindowGeomotry(Character):
    def __init__(self, name, password, character_class, formation_position, x_position, y_position, x_length, y_length):
        super().__init__(name, password, character_class, formation_position)
        self.x_position = x_position
        self.y_position = y_position
        self.x_length = x_length
        self.y_length = y_length
    
    def get_x_position(self):
        return self.x_position
    
    def get_y_position(self):
        return self.y_position
    
    def get_x_length(self):
        return self.x_length
    
    def get_y_length(self):
        return self.y_length

class InventoryManagement(Character):
    def __init__(self, name, password, character_class, formation_position, inventory, weapons, devices, shield, reactor, engine, lodouts):
        super().__init__(name, password, character_class, formation_position)
        self.inventory = []
        self.weapons = []
        self.devices = []
        self.shield = shield
        self.reactor = reactor
        self.engine = engine
        self.loadouts = []
    