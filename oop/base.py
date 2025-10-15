from typing import Self
from datetime import datetime

print(int("10449dc10", 16))
print(4366916624)


class Person:
    def __init__(self, name: str, birthday: datetime):
        self.name = name.strip().title()
        self.money = 0
        self.birthday = birthday

    def __str__(self) -> str:
        return f'<{self.name} with {self.money}grn>'

    def walk(self):
        print(f'{self.name} is walking...')

    def deposit_money(self, amount: int):
        self.money += amount

    def lend_money(self, other: Self, amount: int):
        self.money -= amount
        other.money += amount

    @property
    def age(self) -> int:
        return (datetime.now() - self.birthday).days // 365


ivan = Person(name='        ivan', birthday=datetime(year=2010, month=10, day=19))
vasyl = Person(name='vasYL', birthday=datetime(year=1990, month=10, day=19))

ivan.walk()
print(ivan.name)
print(vasyl.name)
print(ivan, vasyl)

ivan.deposit_money(3567)
ivan.deposit_money(222)
print(ivan, vasyl)

ivan.lend_money(vasyl, 500)

print(ivan, vasyl)

print(vasyl.age)

print(ivan.__dict__)
