from web3 import Web3, HTTPProvider, IPCProvider, TestRPCProvider
web3 = Web3(TestRPCProvider(host="127.0.0.1", port="8545"))

#web3.eth.blockNumber

abi = json.joads("<abi-json-string>")
ContractFactory = web3.eth.contract(abi, code="0x...")
ContractFactory.deploy()
contract = web3.eth.contract(abi, address="0x...")
#contract.transact().someMethod()
#contract.call().return13()
filter = MyContract.on("Transfer", {})
filter.watch(transfer_callback)