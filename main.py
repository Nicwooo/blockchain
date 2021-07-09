from classes.Wallet import Wallet
from classes.Block import Block
from classes.Chain import Chain
import os.path


chain = Chain()
chain.add_transaction(
    '0b918943df0962bc7a1824c0555a389347b4febdc7cf9d1254406d80ce44e3f9',
    'ed3465d4-e092-11eb-b49f-8091331df61a',
    'ed34b3e2-e092-11eb-8f29-8091331df61a',
    25
)
