from web3 import Web3
import codecs

# Connect to a Web3 provider
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545',request_kwargs={'timeout':100}))

# Address of the smart contract
contract_address = "0x627511636204bcbA27C9E3Ee819b983E1Af969D2"

if contract_address == "0x627511636204bcbA27C9E3Ee819b983E1Af969D2":
    print("Please change the contract address to the one deployed in your local blockchain.")
    exit()

# ABI of the smart contract
contract_abi = [{"stateMutability": "nonpayable", "type": "function", "name": "setNumber", "inputs": [{"name": "_number", "type": "uint256"}], "outputs": []}, {"stateMutability": "nonpayable", "type": "function", "name": "getNumber", "inputs": [], "outputs": [{"name": "", "type": "uint256"}]}, {"stateMutability": "view", "type": "function", "name": "storedNumber", "inputs": [], "outputs": [{"name": "", "type": "uint256"}]}]

# Create a contract instance
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Call a function of the contract
print(contract.functions.getNumber().call())

# Send a transaction to the contract
tx_hash = contract.functions.setNumber(20).transact({'from': w3.eth.accounts[0]})
hex_string = codecs.encode(tx_hash, 'hex')
final_tx_hash = '0x' + hex_string.decode()
print("Transaction Hash : ", final_tx_hash)

# Call a function of the contract
print(contract.functions.getNumber().call())