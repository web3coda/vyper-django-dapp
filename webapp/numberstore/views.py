# Import required libraries
from django.http import HttpResponse
from django.shortcuts import render
from web3 import Web3
import codecs

# Connect to a Web3 provider
web3 = Web3(Web3.HTTPProvider('http://localhost:8545',request_kwargs={'timeout':100}))

# Address of the smart contract
contract_address = "0x8A73F2E91968D0eD571E135d0e0031f18f8EAce7"
address = "0x5C0b07b93526CD047C193fAc6d7C0F321AA8901F"
contract_abi = [{"stateMutability": "nonpayable", "type": "function", "name": "setNumber", "inputs": [{"name": "_number", "type": "uint256"}], "outputs": []}, {"stateMutability": "nonpayable", "type": "function", "name": "getNumber", "inputs": [], "outputs": [{"name": "", "type": "uint256"}]}, {"stateMutability": "view", "type": "function", "name": "storedNumber", "inputs": [], "outputs": [{"name": "", "type": "uint256"}]}]

# Instantiate the contract object
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Define the server view function
def server(request):
    # For POST Requests
    if request.method == 'POST':
        # Handle form submission
        text_input = request.POST.get('text_input')

        # Construct the transaction parameters
        tx_params = {
            'from': address,
            'gas': 200000,
            'gasPrice': web3.toWei('5', 'gwei')
        }

        # Call the contract method and construct the transaction
        tx_data = contract.functions.setNumber(int(text_input)).buildTransaction(tx_params)

        # Send the transaction request to Metamask
        try:
            result = web3.eth.send_transaction(tx_data)
        except ValueError as e:
            # Handle any errors that occur
            return render(request, 'server.html', {'error': str(e)})

        # Calling getNumber() function of the Smart Contract and setting retrieved value to storedNumber
        storedNumber = contract.functions.getNumber().call()

        # Return server.html template alongwith storedNumber and transaction hash value
        return render(request, 'server.html', {'storedNumber': storedNumber, 'txhash' : 'tx hash : '+str(result.hex()) })

    # For GET Requests
    else:
        # Calling getNumber() function of the Smart Contract and setting retrieved value to storedNumber
        storedNumber = contract.functions.getNumber().call()

        # Return server.html template alongwith storedNumber value
        return render(request, 'server.html', {'storedNumber': storedNumber})

def client(request):
    return render(request,'client.html',{'storedNumber':''})

def home(request):
    return render(request,'home.html')