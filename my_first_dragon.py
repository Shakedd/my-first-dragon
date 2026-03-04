from enum import Enum
import typer
import json
# import flask

HISTORY_JSON = {"history": []}


class PetType(Enum):
    Bear = "bear"
    Deer = "deer"
    Horse = "horse"


def history(func):
    def wrapper(*args, **kwargs):
        HISTORY_JSON["history"].append(func.__name__)
        return func(*args, **kwargs)

    return wrapper


class Pet:
    FULL = 100
    EMPTY = 0
    HALF = 50
    FIFTH = 20

    def __init__(
        self,
        name: str,
        type: PetType,
        hunger: int = HALF,
        happiness: int = HALF,
        energy: int = HALF,
    ):
        self.name = name
        self.type = type
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.points = (hunger + happiness + energy) / 3

    def points_update(self) -> None:
        self.points = (abs(self.hunger-100) + self.happiness + self.energy) / 3

    def menu(self) -> None:
        print("options: eat, play, sleep, is hungry, is happy, is tired, history, exit")

    def is_hungry(self) -> bool:
        return self.hunger > self.HALF

    def is_happy(self) -> bool:
        return self.happiness > self.HALF

    def is_tired(self) -> bool:
        return self.energy < self.HALF

    def get_history(self) -> None:
        for i in HISTORY_JSON["history"]:
            print(i)
    
    def update(self, param, amount, operator):
        if operator is "+":
            if(param + amount) > self.FULL:
                param = self.FULL
            else:
                param += amount
        if operator is "-":
            if(param - amount) < self.EMPTY:
                param = self.EMPTY
            else:
                param -= amount
        return param

    @history
    def eat(self) -> None:
        self.hunger = self.EMPTY
        self.energy = self.update(self.energy, self.FIFTH, "+")
        print("yummy, now I'm not hungry anymore!")
        self.points_update()

    @history
    def sleep(self) -> None:
        self.energy = self.FULL
        self.hunger = self.update(self.hunger, self.FIFTH, "+")
        self.happiness = self.update(self.happiness, self.FIFTH, "-")
        print("ZZZ...\n I slept well! now I'm not tired anymore!")
        self.points_update()

    @history
    def play(self) -> None:
        self.happiness = self.FULL
        self.energy = self.update(self.energy, self.HALF, "-")
        self.hunger = self.update(self.hunger, self.HALF, "+")
        print("🏈🏀\nwow, that was fun, now I'm super happy!")
        self.points_update()


def operation_interface(p: Pet):
    functions = {
        "is hungry": p.is_hungry,
        "is happy": p.is_happy,
        "is tired": p.is_tired,
        "eat": p.eat,
        "sleep": p.sleep,
        "play": p.play,
        "history": p.get_history,
        "menu": p.menu,
    }

    while True:
        command = str(
            input(
                f"""
what would you like to do with {p.name} the {p.type.value} ?
(enter 'menu' to view options)
                """
            )
        )
        if command in functions.keys():
            r = functions[command]()
            if r is True:
                print("yes!!")
            elif r is False:
                print("no!")
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("please enter a valid option.\nHint: type 'menu'")


def main(name: str, type: PetType):
    try:
        p = Pet(name, type)
        operation_interface(p)
    except TypeError:
        print("no such animal! the available animals are: bear, deer, horse")


if __name__ == "__main__":
    typer.run(main)
