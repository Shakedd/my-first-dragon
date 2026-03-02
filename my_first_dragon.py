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

    def __init__(
        self,
        name: str,
        type: Pet_Type,
        hunger: int = 50,
        happiness: int = 50,
        energy: int = 50,
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
        print("options: eat, play, sleep, is hungry, is happy, is tired, history")

    def is_hungry(self) -> bool:
        return True if self.hunger > 50 else False

    def is_happy(self) -> bool:
        return True if self.happiness > 50 else False

    def is_tired(self) -> bool:
        return True if self.energy < 50 else False

    def get_history(self) -> None:
        with open(DEFAULT_PATH, "r") as f:
            print(f.read())

    @history
    def eat(self) -> None:
        self.hunger = 0
        if (self.energy + 20) > 100:
            self.energy = 100
        else:
            self.energy += 20
        print("yummy, now I'm not hungry anymore!")

    @history
    def sleep(self) -> None:
        self.energy = 100
        if (self.hunger + 20) < 0:
            self.hunger = 0
        else:
            self.hunger += 20
        if (self.happiness - 20) < 0:
            self.happiness = 0
        else:
            self.happiness -= 20
        print("ZZZ...\n I slept well! now I'm not tired anymore!")

    @history
    def play(self) -> None:
        self.happiness = 100
        if (self.energy - 50) < 0:
            self.energy = 0
        else:
            self.energy -= 50
        if (self.hunger + 50) < 0:
            self.hunger = 0
        else:
            self.hunger += 50
        print("🏈🏀\nwow, that was fun, now I'm super happy!")


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
        r = functions[command]()
        if r is True:
            print("yes!!")
        elif r is False:
            print("no!")
        p.points_update()


def main(name: str, type: Pet_Type):
    p = Pet(name, type)
    operation_interface(p)


if __name__ == "__main__":
    typer.run(main)
