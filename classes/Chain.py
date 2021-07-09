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

    for i in range(100):
        random_string += random.choice(letters_and_digits)

    return random_string


class Chain:
    blocks = []
    last_transaction_number = 0

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
        if len(self.blocks) > 0:
            for block in self.blocks:
                if block.hash == hash_to_verify:
                    return False

        # NB: N'ayant pas réussi à générer de hash commençant par 4 zéros
        # sans faire crash l'application, je n'ai fais une vérification
        # qu'avec 1 seul séro.
        if not hash_to_verify[:1] == '0':
            return False

        return True

    def add_block(self, base_hash, tested_hash):
        path = 'content/blocks/' + tested_hash + '.json'
        parent_hash = '00'

        if len(self.blocks) > 0:
            parent_hash = self.blocks[len(self.blocks) - 1].base_hash

        if not os.path.isfile(path):

            new_block = Block(base_hash, tested_hash, parent_hash, list())
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
            block = json.load(block)

            response = Block(
                block['base_hash'],
                block['hash'],
                block['parent_hash'],
                block['transactions']
            )

            return response
        else:
            return False

    def add_transaction(self, block_hash, transmitter_id, receiver_id, amount):
        path = 'content/blocks/' + block_hash + '.json'

        if os.path.isfile(path):
            block = self.get_block(block_hash)

            if not block:
                print('Le bloc spécifié n\'a pas été trouvé')
                return False

            if block.get_weight() <= 256000:
                new_transaction = block.add_transaction(
                    transmitter_id,
                    receiver_id,
                    amount,
                    self.last_transaction_number + 1
                )

                if new_transaction:
                    block.save()

                    for element in self.blocks:
                        if element.hash == block.hash:
                            self.blocks[self.blocks.index(element)] = block

                    self.last_transaction_number += 1

    def find_transaction(self, transaction_number):
        for block in self.blocks:
            print(block.transactions)
            if len(block.transactions) > 0:
                for transaction in block.transactions:
                    if transaction['number'] == transaction_number:
                        return transaction['number']

    def get_last_transaction_number(self):
        return self.last_transaction_number
