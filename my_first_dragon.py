from enum import Enum

class Pet_Type(Enum):
    Bear,
    Deer,
    Hourse

class Pet():
    DEFAULT_PATH = "history.txt"
    
    def __init__(name: str, type: Pet_Type, hunger: int = 50, happiness: int = 50, energy: int = 50, history: str = DEFAULT_PATH):
        self.name = name
        self.type = type
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.points = (hunger + happiness + energy)/3
        self.history = history
        
    def points_update(self):
        self.points = (self.hunger + self.happiness + self.energy)/3
        
    def eat(self):
        self.hunger = 0
        if (self.energy + 20) > 100:
            self.energy = 100
        else:
            self.energy += 20
    
    def sleep(self):
        self.energy = 100
        if (self.hunger - 20) < 0:
            self.hunger = 0
        else:
            self.hunger -= 20
    
    def play(self):
        self.happiness = 100
        if (self.energy -20) < 0:
            self.energy = 0
        else:
            self.energy -= 20
