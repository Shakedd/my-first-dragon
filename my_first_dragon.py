from enum import Enum
import typer
import functools


class PetType(Enum):
    Bear = "bear"
    Deer = "deer"
    Horse = "horse"


class Pet:
    FULL = 100
    EMPTY = 0
    HALF = 50
    FIFTH = 20
    HISTORY_JSON = {"history": []}

    def __init__(
        self,
        name: str,
        type: PetType,
        hunger: int = HALF,
        happiness: int = HALF,
        energy: int = HALF,
        history: dict = HISTORY_JSON,
    ):
        self.name = name
        self.type = type
        self.hunger = max(0, min(100, hunger))
        self.happiness = max(0, min(100, happiness))
        self.energy = max(0, min(100, energy))
        self.history = history
        self.points = int((self.hunger + self.happiness + self.energy) / 3)

    @staticmethod
    def history_log(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            key = self.type.value + "_" + self.name
            if key in self.history.keys():
                self.history[key].append(func.__name__)
            else:
                self.history[key] = [func.__name__]
            return func(self, *args, **kwargs)

        return wrapper

    def points_update(self) -> None:
        self.points = int((self.hunger + self.happiness + self.energy) / 3)

    def menu(self) -> None:
        print(
            """
              options:
              eat, play, sleep - treat your pet
              is hungry, is happy, is energetic - check your pet's status
              history - watch the treatment history of your pet
              exit - exit the game
              """
        )

    def is_hungry(self) -> bool:
        return self.hunger < self.HALF

    def is_happy(self) -> bool:
        return self.happiness > self.HALF

    def is_energetic(self) -> bool:
        return self.energy > self.HALF

    def get_history(self) -> None:
        key = self.type.value + "_" + self.name
        for i in self.history[key]:
            print(i)

    def update(self, param: int, amount: int, operator: str) -> int:
        if operator == "+":
            param = max(self.EMPTY, min(self.FULL, param + amount))
        if operator == "-":
            param = min(self.FULL, max(self.EMPTY, param - amount))
        return param

    @history_log
    def eat(self) -> None:
        self.hunger = self.update(self.hunger, self.HALF, "+")
        self.energy = self.update(self.energy, self.FIFTH, "+")
        print("yummy, that was delicious!")
        self.points_update()

    @history_log
    def sleep(self) -> None:
        self.energy = self.FULL
        self.hunger = self.update(self.hunger, self.FIFTH, "-")
        self.happiness = self.update(self.happiness, self.FIFTH, "-")
        print("ZZZ...\n I slept well! now I'm not tired anymore!")
        self.points_update()

    @history_log
    def play(self) -> None:
        self.happiness = self.FULL
        self.energy = self.update(self.energy, self.HALF, "-")
        self.hunger = self.update(self.hunger, self.HALF, "-")
        print("🏈🏀\nwow, that was fun, now I'm super happy!")
        self.points_update()


def operation_interface(p: Pet):
    functions = {
        "is hungry": p.is_hungry,
        "is happy": p.is_happy,
        "is energetic": p.is_energetic,
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
    # try:
    p = Pet(name, type)
    operation_interface(p)


# except TypeError:
# print("no such animal! the available animals are: bear, deer, horse")


if __name__ == "__main__":
    typer.run(main)
