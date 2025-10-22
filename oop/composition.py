
class FinancialActivity:
    def __init__(self):
        self.accounts: list[BankAccount] = []

    @property
    def total_money(self):
        money = 0
        for account in self.accounts:
            money += account.balance

        return money


class Person(FinancialActivity):
    def __init__(self, name: str):
        super().__init__()
        self.name: str = name.title()
        self.accounts: list["BankAccount"] = []

    def __str__(self):
        return f"<Person {self.name} has {len(self.accounts)} totally with {self.total_money}grn>"


class BankAccount:
    def __init__(self, client: Person, emitent: "Bank"):
        self.client = client
        self.emitent = emitent
        self.balance = 0

    def spending(self, amount: int):
        self.balance -= amount

    def depositing(self, amount: int):
        self.balance += amount

    def __str__(self):
        return f"<BankAccount belongs {self.client} and was emmited by {self.emitent}>"


class Bank(FinancialActivity):
    def __init__(self, name: str):
        super().__init__()
        self.name: str = name.title()
        self.accounts: list[BankAccount] = []

    def __str__(self):
        return f"<Bank {self.name} has {len(self.accounts)} totally with {self.total_money}grn>"

    def open_account(self, client: Person) -> BankAccount:
        new_account = BankAccount(client=client, emitent=self)
        self.accounts.append(new_account)
        client.accounts.append(new_account)
        return new_account


person_alex = Person(name='Alex')
print(person_alex)

bank_mono = Bank('Monobank')

bank_raif = Bank('Raif')
print(bank_raif)

bank_mono.open_account(person_alex)
bank_raif.open_account(person_alex)
print(person_alex)
print(bank_mono)


person_alex.accounts[0].depositing(1000)
person_alex.accounts[0].depositing(1000)
person_alex.accounts[-1].depositing(1200)
print(person_alex)
print(bank_mono)
print(bank_raif)

