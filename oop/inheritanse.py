from typing import Self
from random import randint


class Character:
    def __init__(self, name: str):
        self.name = name.strip()
        self.health = 100
        self.armor = 10
        self.precision_percentage = 50

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def attack(self, other: Self):
        if not self.is_alive:
            print(f"{self} - skip")
            return

        if not self.armor > 0:
            print(f"{self} - skip (no armor)")
            return

        is_success_shot = randint(0, 100) < self.precision_percentage
        self.armor -= 1
        if not is_success_shot:
            print(f"{self} >>> missed")
            return

        other.health -= 17
        print(f"{self} - success ({other})")


class Tank(Character):
    def __init__(self, name: str, diesel: int = 100):
        super().__init__(name)
        self.diesel = diesel
        self.armor = 24

    def __str__(self):
        return f"Tank {self.name} with {self.diesel=} and {self.armor=}, {self.is_alive=}"

    def attack(self, other: Self):
        super().attack(other)
        self.diesel -= 23
        if self.diesel < 0:
            self.precision_percentage = 25
            print(f"low precision of the {self}")


class Artillery(Character):
    def __str__(self):
        return f"Artillery {self.name} {self.armor=}, {self.is_alive=}"


tank1 = Tank(name='111111111')
tank2 = Tank(name='2222222222')
arta = Artillery(name='mjnhvghf')

tank1.attack(tank2)
tank1.attack(tank1)
arta.attack(tank1)

tank1.attack(arta)
arta.attack(tank1)

tank1.attack(arta)
arta.attack(tank1)

tank1.attack(arta)
arta.attack(tank1)

tank1.attack(arta)
arta.attack(tank1)

tank1.attack(arta)
arta.attack(tank1)

tank1.attack(arta)
arta.attack(tank1)

tank1.attack(arta)
arta.attack(tank1)

tank1.attack(arta)
arta.attack(tank1)

tank1.attack(arta)
arta.attack(tank1)

tank1.attack(arta)
arta.attack(tank1)

tank1.attack(arta)
arta.attack(tank1)









