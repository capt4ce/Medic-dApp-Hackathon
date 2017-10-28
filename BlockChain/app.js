Web3 = require('web3')
fs = require('fs')
solc = require('solc')

web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
code = fs.readFileSync('./contracts/Medic.sol').toString()
compiledCode = solc.compile(code)
// console.log(compiledCode.contracts)
abiDefinition = JSON.parse(compiledCode.contracts[':Medic'].interface)
VotingContract = web3.eth.contract(abiDefinition)
byteCode = compiledCode.contracts[':Medic'].bytecode
deployedContract = VotingContract.new([], { data: byteCode, from: web3.eth.accounts[0], gas: 4700000 })


var process = require('process')
var stop = false;
var f = function () { if (!stop) process.nextTick(f) }
f()
console.log(JSON.stringify(abiDefinition))
console.log('from: ' + web3.eth.accounts[0])
console.log('account [0] balance: ' + web3.eth.getBalance(web3.eth.accounts[0]))
console.log('web3 ready...')
