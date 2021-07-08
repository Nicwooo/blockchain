from classes.Wallet import Wallet

first = Wallet()
first.save()

second = Wallet()
second.load(str(first.unique_id))

print(second.unique_id)
