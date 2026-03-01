from enum import Enum
import logging

class Pet_Type(Enum):
    Bear,
    Deer,
    Hourse

def history(func):
    def wrapper(*args, **kwargs):
        history = logging.basicConfig("history.txt")
        history.info('{func.__name__}\n')
        func(*args, **kwargs)
    return wrapper
        

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
        
    def points_update(self) -> None:
        self.points = (self.hunger + self.happiness + self.energy)/3

    def is_hungry(self) -> bool:
        if self.hunger > 50:
            return True
        else:
            return False

    def is_happy(self) -> bool:
        if self.happiness > 50:
            return True
        else:
            return False
        
    def is_tired(self) -> bool:
        if self.energy < 50:
            return True
        else:
            return False
        
    def get_history(self) -> str:
        with open("history.txt", "a") as f:
            return f.read()
    
    @history
    def eat(self) -> str:
        self.hunger = 0
        if (self.energy + 20) > 100:
            self.energy = 100
        else:
            self.energy += 20
    
    @history
    def sleep(self) -> str:
        self.energy = 100
        if (self.hunger - 20) < 0:
            self.hunger = 0
        else:
            self.hunger -= 20
    
    @history
    def play(self) -> str:
        self.happiness = 100
        if (self.energy -20) < 0:
            self.energy = 0
        else:
            self.energy -= 20

