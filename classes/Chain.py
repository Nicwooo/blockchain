import hashlib
import os.path
import json
from random import randint


def generate_random_string():
    return str(randint(0, 1000))


class Chain:
    blocks = []
    last_transaction_number = 0

    def __init__(self):
        pass

    def generate_hash(self):
        string_to_test = generate_random_string()
        hash = hashlib.sha256(string_to_test.encode()).hexdigest()

        if self.verify_hash(hash):
            add_block(hash)
        else:
            self.generate_hash()

    def verify_hash(self, hash_to_verify):
        print(hash_to_verify)
        if len(self.blocks) > 0:
            for i in self.blocks:
                if self.blocks[i].hash == hash_to_verify:
                    return False

        if not hash_to_verify[:4] == '0000':
            return False

        return True

    def add_block(self, base_hash, hash):
        path = 'content/blocks/' + hash + '.json'

        if not os.path.isfile(path):
            new_block = Block(base_hash, hash)
            new_block.save()

    def get_block(self, hash):
        path = 'content/blocks/' + hash + '.json'

        if os.path.isfile(path):
            block = open(path, 'r')

            return json.load(block)

        else:
            return 'Ce bloc n\'éxiste pas'

    def add_transaction(self):
        pass
