import random
from enum import Enum, auto
from pprint import pp

random.seed(0xDEADBEEF)


class Power(Enum):
    SPEED_BOOTS    = auto()
    STRONG_WILL    = auto()
    MONEY_MAKER    = auto()
    SUPER_STRENGTH = auto()


class Duck:
    def __init__(self, name: str = "duck"):
        self.name = name

    def __repr__(self):
        if hasattr(self, 'power'):
            return f'{self.__class__.__name__} with {self.__getattribute__("power").name}' \
                    f' says: Hello, my name is {self.name}'
        return f"{self.__class__.__name__} says: Hello, I'm {self.name}"


class WeaklingDuck(Duck):
    pass


class SuperDuck(Duck):
    def __init__(self, name, power):
        super().__init__(name)
        if isinstance(power, Power):
            self.power = power
        else:
            self.power = random.choice(list(Power))


def main():
    d1 = WeaklingDuck()
    d2 = Duck("Huey")
    d3 = SuperDuck("Scrooge McDuck", Power.MONEY_MAKER)
    d4 = SuperDuck("Launchpad McQuack", Power.SPEED_BOOTS)
    ducks_in_a_row = [d4, d3, d2, d1]  # Here boss, I've sorted it... it's done boss
    pp(ducks_in_a_row)
    # add some code here (and/or edit that above this line)

if __name__ == '__main__':
    main()
