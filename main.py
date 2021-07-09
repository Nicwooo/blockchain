from classes.Wallet import Wallet
from classes.Block import Block
from classes.Chain import Chain
import hashlib

# --------- WALLET TESTS ---------
wallet1 = Wallet()
print('First wallet1 id: ' + str(wallet1.unique_id))

wallet1.generate_unique_id()  # The unique_id attribute should be different
print('wallet1 id after using generate_unique_id(): ' + str(wallet1.unique_id))

wallet1.save()  # Check inside content/wallets to see the new saved wallet
print('wallet1 starting balance: ' + str(wallet1.balance))

wallet1.add_balance(40)  # The balance should have increased by 40
print("wallet1 balance (after using add_balance(40)): " + str(wallet1.balance))

wallet1.sub_balance(20)  # The balance should have been reduced by 20
print('wallet1 balance (after using sub_balance(20)): ' + str(wallet1.balance))

wallet1.load(str(wallet1.unique_id)) # We should have the first balance back (= 100)
print('wallet1 balance (after using load() on itself): ' + str(wallet1.balance))

# Made another wallet for later
wallet2 = Wallet()
wallet2.save()

# --------- BLOCK TESTS ---------

# To explicitly test the entire Block class, we need to manually create a new Block
# In a normal way, the base_hash, the hash and the parent_hash would be incorrect
block1 = Block(
    'base_hash test',
    str(hashlib.sha256('base_hash test'.encode()).hexdigest()),
    'parent_hash test',
    list()
)

block1.save() # Watch the content/blocks files to see if it worked

print("Is the hash correct ? " + str(block1.check_hash()))  # It should returns "True"

# To see this result, you should watch the wallets balances and the block transactions list
block1.add_transaction(str(wallet1.unique_id), str(wallet2.unique_id), 15, 24)

# It should returns the previous transaction
print("Transaction number 24: " + str(block1.get_transaction(24)))

# It should returns the block1 file weight
print('block1 file weight: ' + str(block1.get_weight()) + ' bytes')

block2 = Block(
    'load test',
    str(hashlib.sha256('load test'.encode()).hexdigest()),
    'parent_hash test',
    list()
)

print('block1 hash: ' + str(block1.hash))

# The hash must be different from the hash in block 1
print('block2 hash: ' + str(block2.hash))

block2.load(str(block1.hash))
# Now the hash should be the same as the hash in block 1
print('new block2 hash: ' + str(block2.hash))

# --------- CHAIN TESTS ---------
chain = Chain()

# It should generate a new block in content/blocks
chain.generate_hash()

# This hash already exists : the method should returns False
print('Is this hash correct ? ' + str(chain.verify_hash(str(chain.blocks[0].hash))))

# It should create a new block in content/blocks
chain.add_block(
    'test_hash',
    hashlib.sha256('test_hash'.encode()).hexdigest()
)

# It should returns a new Block instance with the asked block data
new_block = str(chain.get_block(str(chain.blocks[0].hash)))
print('Block: ' + new_block)

# It should add a new transaction
# you can see the result in the corresponding block in content.block
chain.add_transaction(
    str(chain.blocks[0].hash),
    str(wallet1.unique_id),
    str(wallet2.unique_id),
    15
)

# Here is another way to see if the transaction worked
# It also allows us to test the find_transaction() method
print('Previous transaction: ' + str(chain.find_transaction(1)))

# It should returns the last transaction number (here, 1)
print('Last transaction number: ' + str(chain.get_last_transaction_number()))
