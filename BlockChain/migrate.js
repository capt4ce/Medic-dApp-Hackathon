Web3 = require('web3')
fs = require('fs')

contractAddress = '0x72e8a0d6dfbe5932474432575837a3e2593b994f';
abi = JSON.parse('[{"constant":false,"inputs":[],"name":"getCandidates","outputs":[{"name":"","type":"bytes32[]"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"candidate","type":"bytes32"}],"name":"totalVotesFor","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"candidate","type":"bytes32"}],"name":"validCandidate","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"votesReceived","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"candidateList","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"candidate","type":"bytes32"}],"name":"voteForCandidate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"candidateNames","type":"bytes32[]"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"name","type":"bytes32"},{"indexed":true,"name":"voter","type":"address"}],"name":"Vote","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"timestamp","type":"uint256"}],"name":"TotalVotes","type":"event"}]')


doctorGenerator = JSON.parse(fs.readFileSync('../data_dump/doctorgen.json').toString())
patientGenerator = JSON.parse(fs.readFileSync('../data_dump/doctorgen.json').toString())
treatmentGenerator = JSON.parse(fs.readFileSync('../data_dump/doctorgen.json').toString())

web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
contract = web3.eth.contract(abi);
contractInstance = contract.at(contractAddress);

//generating 5 doctors
console.log('Doctor data is being generated...')
for (var i = 0; i < 5; i++) {
    contractInstance.addDoctor(doctorGenerator[i].age, doctorGenerator[i].sex, doctorGenerator[i].specialities, { from: web3.eth.accounts[i] }, function () {
    })
}

//generating 5 patients
console.log('Patient data is being generated...')
for (var i = 0; i < 10; i++) {
    startFrom = 5
    contractInstance.addPatient(patientGenerator[i].patient, patientGenerator[i].age, patientGenerator[i].sex, patientGenerator[i].currentDiseases, patientGenerator[i].currentTreatments, patientGenerator[i].treatmentRestrictions, { from: web3.eth.accounts[i + startFrom] }, function () {

    })
}

//generating treatments
console.log('treatment data is being generated...')
treatmentGenerator.forEach(function (val, i) {
    contractInstance.issueTreatmentRecord(web3.eth.accounts[i + startFrom], treatments, treatmentStatus, disease, { from: web3.eth.accounts[i] }, function () {

    })
})
