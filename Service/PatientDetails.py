from web3 import Web3, HTTPProvider, IPCProvider, TestRPCProvider
import json
import time
web3 = Web3(HTTPProvider("http://10.10.1.90:8545"))
#web3 = Web3(TestRPCProvider(host='127.0.0.1', port=8545))
def vote_callback(r):
    print(r)
print(web3.eth.blockNumber)

abiJsonString = '[{"constant":false,"inputs":[],"name":"getCandidates","outputs":[{"name":"","type":"bytes32[]"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"candidate","type":"bytes32"}],"name":"totalVotesFor","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"candidate","type":"bytes32"}],"name":"validCandidate","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"votesReceived","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"candidateList","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"candidate","type":"bytes32"}],"name":"voteForCandidate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"candidateNames","type":"bytes32[]"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"name","type":"bytes32"},{"indexed":true,"name":"voter","type":"address"}],"name":"Vote","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"timestamp","type":"uint256"}],"name":"TotalVotes","type":"event"}]'
abi_json = json.loads(abiJsonString)
#ContractFactory = web3.eth.contract(abi, code="0x00a795bc0a9795be6b97e64a6e21d0185e3db3c5")
#ContractFactory.deploy()
contract = web3.eth.contract(abi=abi_json, address="0x72e8a0d6dfbe5932474432575837a3e2593b994f")
print (contract)
#contract.transact().someMethod()
#contract.call().return13()
#print(contract.call().validCandidate('Rama'))
filter = contract.on("Vote", filter_params={'filter':{'voter':'0x7c5c8e42f98ad66e05d81f1ca21174521430284a'},'fromBlock':0, 'toBlock':'latest'})
print(filter.filter_id)
print(filter.get(False))
#filter.watch(vote_callback)
#print(web3.eth.getFilterLogs(filter.filter_id))