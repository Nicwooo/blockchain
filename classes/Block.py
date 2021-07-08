import os


class Block:
    base_hash = 0
    hash = ''
    parent_hash = ''
    transactions = []

    def check_hash(self):
        pass

    def add_transaction(self):
        pass

    def get_transaction(self):
        pass

    def get_weight(self, block):
        path = 'content/blocs/' + block + '.json'
        file_stats = os.stat(path)

        return file_stats.st_size

    def save(self):
        pass

    def load(self):
        pass