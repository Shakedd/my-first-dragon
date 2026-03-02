from enum import Enum
import typer

DEFAULT_PATH = "history.txt"

class Pet_Type(Enum):
    Bear = "bear"
    Deer = "deer"
    Hourse = "horse"


def history(func):
    def wrapper(*args, **kwargs):
        with open(DEFAULT_PATH, "a") as f:
            f.write(func.__name__ + "\n")
        return func(*args, **kwargs)
    return wrapper


class Pet:
    global DEFAULT_PATH
    FULL = 100
    EMPTY = 0
    HALF = 50
    FIFTH = 20

    def __init__(
        self,
        name: str,
        type: Pet_Type,
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
        self.points = (self.hunger + self.happiness + self.energy) / 3

    def menu(self) -> None:
        print("options: eat, play, sleep, is hungry, is happy, is tired, history, exit")

    def is_hungry(self) -> bool:
        return True if self.hunger > self.HALF else False

    def is_happy(self) -> bool:
        return True if self.happiness > self.HALF else False

    def is_tired(self) -> bool:
        return True if self.energy < self.HALF else False

    def get_history(self) -> None:
        with open(DEFAULT_PATH, "r") as f:
            print(f.read())

    @history
    def eat(self) -> None:
        self.hunger = self.EMPTY
        if (self.energy + self.FIFTH) > self.FULL:
            self.energy = self.FULL
        else:
            self.energy += self.FIFTH
        print("yummy, now I'm not hungry anymore!")
        self.points_update()

    @history
    def sleep(self) -> None:
        self.energy = self.FULL
        if (self.hunger + self.FIFTH) > self.FULL:
            self.hunger = self.FULL
        else:
            self.hunger += self.FIFTH
        if (self.happiness - self.FIFTH) < self.EMPTY:
            self.happiness = self.EMPTY
        else:
            self.happiness -= self.FIFTH
        print("ZZZ...\n I slept well! now I'm not tired anymore!")
        self.points_update()

    @history
    def play(self) -> None:
        self.happiness = self.FULL
        if (self.energy - self.HALF) < self.EMPTY:
            self.energy = self.EMPTY
        else:
            self.energy -= self.HALF
        if (self.hunger + self.HALF) > self.FULL:
            self.hunger = self.FULL
        else:
            self.hunger += self.HALF
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
        "menu": p.menu
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


def main(name: str, type: Pet_Type):
    p = Pet(name, type)
    operation_interface(p)


if __name__ == "__main__":
    typer.run(main)
