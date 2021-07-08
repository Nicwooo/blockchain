import uuid
import json


class Wallet:
    unique_id = ''
    balance = 100
    history = []

    def __init__(self):
        self.generate_unique_id()

    def generate_unique_id(self):
        self.unique_id = uuid.uuid1()

    def add_balance(self, amount):
        self.balance += amount

    def sub_balance(self, amount):
        self.balance -= amount

    def send(self):
        pass

    def save(self):

        data = {
            'id': str(self.unique_id),
            'balance': self.balance,
            'history': self.history
        }

        path = "content/wallets/" + str(self.unique_id) + ".json"

        with open(path, "w") as jsonFile:
            json.dump(data, jsonFile)
