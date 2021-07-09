import hashlib
import os.path
import json
from random import randint
from classes.Block import Block


def generate_random_string():
    return str(randint(0, 1000))


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
        print(hash_to_verify)
        if len(self.blocks) > 0:
            for i in self.blocks:
                if self.blocks[i].hash == hash_to_verify:
                    return False

        if not hash_to_verify[:1] == '0':
            return False

        return True

    def add_block(self, base_hash, tested_hash):
        path = 'content/blocks/' + tested_hash + '.json'
        parent_hash = '00'

        if len(self.blocks) > 0:
            parent_hash = self.blocks[len(self.blocks) - 1]['base_hash']

        if not os.path.isfile(path):

            new_block = Block(base_hash, tested_hash, parent_hash)
            new_block.save()

            if os.path.isfile(path):
                self.blocks.append(new_block)

            else:
                print('Erreur lors de la création du bloc')

        else:
            print('Ce bloc existe déjà')

    def get_block(self, asked_hash):
        path = 'content/blocks/' + asked_hash + '.json'

        if os.path.isfile(path):
            block = open(path, 'r')

            return json.load(block)

        else:
            return 'Ce bloc n\'éxiste pas'

    def add_transaction(self, block):
        path = 'content/blocks/' + block + '.json'

        if block.get_weight():
            new_transaction = block.add_transaction(transmitter_id, receiver_id, amount, self.last_transaction_number)

            if new_transaction and os.path.isfile(path):
                with open(path, 'w') as block_data:
                    json.dump(block, block_data)

                self.last_transaction_number += 1
