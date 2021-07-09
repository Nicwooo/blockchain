import uuid
import json
import os.path


class Wallet:
    unique_id = ''
    balance = 100
    history = []

    def __init__(self):
        self.generate_unique_id()

    def generate_unique_id(self):
        generated_id = uuid.uuid1()
        path = 'content/wallets/' + str(generated_id) + '.json'

        if not os.path.isfile(path):
            self.unique_id = generated_id
        else:
            self.generate_unique_id()

    def add_balance(self, amount):
        self.balance += amount

    def sub_balance(self, amount):
        self.balance -= amount

    def send(self, transaction):
        self.history.append(transaction)

    def save(self):

        data = {
            'unique_id': str(self.unique_id),
            'balance': self.balance,
            'history': self.history
        }

        path = 'content/wallets/' + str(self.unique_id) + '.json'

        with open(path, 'w') as jsonFile:
            json.dump(data, jsonFile)

    def load(self, wallet_id):
        path = 'content/wallets/' + wallet_id + '.json'

        if os.path.isfile(path):
            wallet = open(path, 'r')

            wallet = json.load(wallet)

            self.unique_id = wallet['unique_id']
            self.balance = wallet['balance']
            self.history = wallet['history']
