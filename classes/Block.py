import os
import hashlib


class Block:
    base_hash = 0
    hash = ''
    parent_hash = ''
    transactions = []

    def check_hash(self):
        expected_hash = hashlib.sha256(base_hash.encode()).hexdigest()

        return expected_hash == self.hash

    def add_transaction(self):
        pass

    def get_transaction(self):
        pass

    def get_weight(self):
        path = 'content/blocs/' + self.hash + '.json'
        file_stats = os.stat(path)

        return file_stats.st_size

    def save(self):
        data = {
            'base_hash': self.base_hash,
            'hash': self.hash,
            'parent_hash': self.parent_hash,
            'transactions': self.transactions
        }

        path = 'content/blocs/' + self.hash + '.json'

        with open(path, 'w') as jsonFile:
            json.dump(data, jsonFile)

    def load(self, block_hash):
        path = 'content/blocs/' + block_hash + '.json'

        if os.path.isfile(path):
            block = open(path, 'r')

            block = json.load(block)

            self.base_hash = block['base_hash']
            self.hash = block['hash']
            self.parent_hash = block['parent_hash']
            self.transactions = block['transactions']