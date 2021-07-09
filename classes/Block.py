import os
import json
import hashlib
from classes.Wallet import Wallet


class Block:
    base_hash = 0
    hash = ''
    parent_hash = ''
    transactions = []

    def __init__(self, base_hash, hash, parent_hash, transactions):
        self.base_hash = base_hash
        self.hash = hash
        self.parent_hash = parent_hash
        self.transactions = transactions

    def check_hash(self):
        expected_hash = hashlib.sha256(self.base_hash.encode()).hexdigest()

        return expected_hash == self.hash

    def add_transaction(
            self,
            transmitter_id,
            receiver_id,
            amount,
            transaction_number
    ):
        transmitter_wallet = Wallet()
        transmitter_wallet.load(transmitter_id)

        receiver_wallet = Wallet()
        receiver_wallet.load(receiver_id)

        if transmitter_wallet.balance - amount >= 0:
            transmitter_wallet.sub_balance(amount)
            receiver_wallet.add_balance(amount)

            new_transaction = {
                "number": transaction_number,
                "transmitter": transmitter_id,
                "receiver": receiver_id,
                "amount": amount
            }

            transmitter_wallet.send(new_transaction)
            receiver_wallet.send(new_transaction)

            transmitter_wallet.save()
            receiver_wallet.save()

            self.transactions.append(new_transaction)
            return True

        else:
            return False

    def get_transaction(self, transaction_number):

        if self.transactions[transaction_number]:
            return self.transactions[transaction_number]
        else:
            return 'Le numéro de la transaction est incorrect'

    def get_weight(self):
        path = 'content/blocks/' + self.hash + '.json'
        file_stats = os.stat(path)

        return file_stats.st_size <= 256000

    def save(self):
        data = {
            'base_hash': self.base_hash,
            'hash': self.hash,
            'parent_hash': self.parent_hash,
            'transactions': self.transactions
        }

        path = 'content/blocks/' + self.hash + '.json'

        with open(path, 'w') as jsonFile:
            json.dump(data, jsonFile)

    def load(self, block_hash):
        path = 'content/blocks/' + block_hash + '.json'

        if os.path.isfile(path):
            block = open(path, 'r')

            block = json.load(block)

            self.base_hash = block['base_hash']
            self.hash = block['hash']
            self.parent_hash = block['parent_hash']
            self.transactions = block['transactions']
