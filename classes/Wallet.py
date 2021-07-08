import uuid


class Wallet:
    unique_id = ''
    balance = 100
    history = []

    def generate_unique_id(self):
        self.unique_id = uuid.uuid1()

    def add_balance(self, amount):
        self.balance += amount

    def sub_balance(self, amount):
        self.balance -= amount

    def send(self):
        pass
