import hashlib
import os.path
from random import randint


def generate_random_string():
    return randint(0, 1000)


class Chain:
    blocks = []
    last_transaction_number = 0

    def __init__(self):
        pass

    def generate_hash(self):
        string_to_test = generate_random_string()
        hash = hashlib.sha256(string_to_test.encode()).hexdigest()

        if self.verify_hash(hash):
            return hash
        else:
            self.generate_hash()

    def verify_hash(self, hash_to_verify):
        for i in self.blocks:
            if self.blocks[i].hash == hash_to_verify:
                return False

        return hash_to_verify[:4] == '0000'

    def add_block(self):
        pass

    def get_block(self):
        pass

    def add_transaction(self):
        pass
