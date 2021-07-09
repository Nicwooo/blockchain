from classes.Wallet import Wallet
from classes.Block import Block
from classes.Chain import Chain

wallet1 = Wallet()
wallet1.save()

wallet2 = Wallet()
wallet2.save()


block = Block('test', 'test', 'test')
block.save()

chain = Chain()
chain.add_transaction(str(block.hash), str(wallet1.unique_id), str(wallet2.unique_id), 15)