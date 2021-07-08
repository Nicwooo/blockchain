from classes.Wallet import Wallet
from classes.Block import Block

block = Block()
block.add_transaction('013269d8-dff0-11eb-a7df-8091331df61a', 'fffb22a4-dfef-11eb-a859-8091331df61a', 30)
block.add_transaction('013269d8-dff0-11eb-a7df-8091331df61a', 'fffb22a4-dfef-11eb-a859-8091331df61a', 20)


trans = block.get_transaction(1)

print(trans)
