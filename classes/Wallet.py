import uuid


class Wallet:
    unique_id = ''

    @classmethod
    def generate_unique_id(cls):
        self.unique_id = uuid.uuid1()
