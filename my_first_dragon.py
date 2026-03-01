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