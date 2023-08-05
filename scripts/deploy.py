from brownie import NumberStorage, accounts
from brownie.network import gas_price

def main():
    # Use a higher gas price, for example, 50 Gwei (in Wei format)
    return NumberStorage.deploy({'from': accounts[0], 'gas_price': gas_price('50 gwei')})
