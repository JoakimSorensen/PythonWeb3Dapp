from web3 import Web3


#Prints list elements with newline
def pr_list(l):
    [print(el) for el in l]


#gets balance from specified account index in ether
def get_ethbal(w3, ind):
    return w3.fromWei(w3.eth.getBalance(w3.eth.accounts[ind]), 'ether')


def send_eth(w3, from_acc, to_acc, val, gas=21000):
    tx_hash = w3.eth.sendTransaction({
        'from': w3.eth.accounts[from_acc],
        'to': w3.eth.accounts[to_acc],
        'value': w3.toWei(val, 'ether'),
        'gas': gas
        })
    return tx_hash


if __name__=='__main__':
    print('starting w3_test...')
    w3 = Web3(Web3.EthereumTesterProvider())
    print('Web3 connected to chain: %r'%(w3.isConnected()))
    print('List of Accounts: ')
    pr_list(w3.eth.accounts)

    print(w3.eth.getTransaction(send_eth(w3, 0, 1, 3)))
    print('Balance Account 0: %d'%(get_ethbal(w3, 0)))
    print('Balance Account 1: %d'%(get_ethbal(w3, 1)))

