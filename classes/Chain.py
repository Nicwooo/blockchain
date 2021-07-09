import hashlib
import os.path
import json
import random
import string
from classes.Block import Block
import sys

sys.setrecursionlimit(10 ** 6)


def generate_random_string():
    letters_and_digits = string.ascii_lowercase + string.digits
    random_string = ''

    for i in range(1000):
        random_string += random.choice(letters_and_digits)

    return random_string


class Chain:
    blocks = []
    last_transaction_number = 1

    def __init__(self):
        pass

    def generate_hash(self):
        string_to_test = generate_random_string()
        hash_to_test = hashlib.sha256(string_to_test.encode()).hexdigest()

        if self.verify_hash(hash_to_test):
            self.add_block(string_to_test, hash_to_test)
        else:
            self.generate_hash()

    def verify_hash(self, hash_to_verify):
        print(hash_to_verify)
        if len(self.blocks) > 0:
            for block in self.blocks:
                if block.hash == hash_to_verify:
                    return False

        if not hash_to_verify[:1] == '0':
            return False

        return True

    def add_block(self, base_hash, tested_hash):
        path = 'content/blocks/' + tested_hash + '.json'
        parent_hash = '00'

        if len(self.blocks) > 0:
            parent_hash = self.blocks[len(self.blocks) - 1].base_hash

        if not os.path.isfile(path):

            new_block = Block(base_hash, tested_hash, parent_hash)
            new_block.save()

            if os.path.isfile(path):
                self.blocks.append(new_block)

                return True

            else:
                print('Erreur lors de la création du bloc')

        else:
            print('Ce bloc existe déjà')

        return False

    def get_block(self, asked_hash):
        path = 'content/blocks/' + asked_hash + '.json'

        if os.path.isfile(path):
            block = open(path, 'r')

            return json.load(block)

        else:
            return 'Ce bloc n\'éxiste pas'

    def add_transaction(self, block_hash, transmitter_id, receiver_id, amount):
        path = 'content/blocks/' + block_hash + '.json'

        if os.path.isfile(path):
            block = Block('', '', '')
            block.load(block_hash)

            if block.get_weight():
                new_transaction = block.add_transaction(
                    transmitter_id,
                    receiver_id,
                    amount,
                    self.last_transaction_number
                )

                if new_transaction:
                    data = {
                        'base_hash': block.base_hash,
                        'hash': block.hash,
                        'parent_hash': block.parent_hash,
                        'transactions': block.transactions
                    }

                    with open(path, 'w') as block_data:
                        json.dump(data, block_data)

                    self.last_transaction_number += 1

    def find_transaction(self, transaction_number):
        for block in self.blocks:
            if len(block.transactions) > 0:
                for transaction in block.transactions:
                    if transaction.number == transaction_number:
                        return block

    def get_last_transaction_number(self):
        if self.last_transaction_number - 1 > 0:
            return self.last_transaction_number - 1
        else:
            return 'Aucune transaction n\'a été effectuée'
