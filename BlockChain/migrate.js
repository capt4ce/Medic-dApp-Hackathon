Web3 = require('web3')
fs = require('fs')
config = require('./config.js')

contractAddress = '0x43f472684368e2051bdfbb230d3ba104ecd9409f'
abi = JSON.parse('[{"constant":false,"inputs":[{"name":"patient","type":"address"}],"name":"getPatientRenalProfile","outputs":[{"components":[{"name":"Creatinine","type":"uint8"},{"name":"Sodium","type":"uint8"},{"name":"Potassium","type":"uint8"},{"name":"eGFR","type":"uint8"},{"name":"Urea","type":"uint8"}],"name":"","type":"tuple"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"diseaseHash","type":"string"},{"name":"name","type":"string"},{"name":"symptomList","type":"string"}],"name":"getDiseaseDetail","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"sex","type":"string"}],"name":"changePatientSex","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"age","type":"uint8"}],"name":"changePatientAge","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"doctor","type":"address"}],"name":"getDoctorDetail","outputs":[{"components":[{"name":"identityHash","type":"string"},{"name":"age","type":"uint8"},{"name":"sex","type":"string"},{"name":"specialities","type":"string"}],"name":"","type":"tuple"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"}],"name":"getPatientDetail","outputs":[{"name":"","type":"string"},{"name":"","type":"uint8"},{"name":"","type":"string"},{"name":"","type":"string"},{"name":"","type":"string"},{"name":"","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"age","type":"uint8"}],"name":"changeAge","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"Creatinine","type":"uint8"},{"name":"Sodium","type":"uint8"},{"name":"Potassium","type":"uint8"},{"name":"eGFR","type":"uint8"},{"name":"Urea","type":"uint8"}],"name":"setPatientRenalProfile","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"treatments","type":"string"},{"name":"treatmentStatus","type":"string"},{"name":"disease","type":"string"}],"name":"issueTreatmentRecord","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"drugHash","type":"string"}],"name":"drugBuy","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"currentDiseases","type":"string"}],"name":"changePatientCurrentDiseases","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"treatmentRestrictions","type":"string"}],"name":"changePatientTreatmentRestrictions","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"diseaseHash","type":"string"},{"name":"name","type":"string"},{"name":"symptomList","type":"string"}],"name":"addDisease","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"identityHash","type":"string"},{"name":"age","type":"uint8"},{"name":"sex","type":"string"},{"name":"specialities","type":"string"}],"name":"addDoctor","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"currentTreatments","type":"string"}],"name":"changePatientCurrentTreatments","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"specialities","type":"string"}],"name":"changeSpecialities","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"drugHash","type":"string"},{"name":"name","type":"string"},{"name":"qty","type":"int256"},{"name":"price","type":"uint8"}],"name":"sellDrug","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"identityHash","type":"string"},{"name":"age","type":"uint8"},{"name":"sex","type":"string"},{"name":"currentDiseases","type":"string"},{"name":"currentTreatments","type":"string"},{"name":"treatmentRestrictions","type":"string"}],"name":"addPatient","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"sex","type":"string"}],"name":"changeSex","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"test","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"doctor","type":"address"},{"indexed":false,"name":"patient","type":"address"},{"indexed":false,"name":"treatments","type":"string"},{"indexed":false,"name":"status","type":"string"},{"indexed":false,"name":"disease","type":"string"}],"name":"Treatment","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"patient","type":"address"},{"indexed":false,"name":"Creatinine","type":"uint8"},{"indexed":false,"name":"Sodium","type":"uint8"},{"indexed":false,"name":"Potassium","type":"uint8"},{"indexed":false,"name":"eGFR","type":"uint8"},{"indexed":false,"name":"Urea","type":"uint8"}],"name":"RenalTest","type":"event"}]')

doctorGenerator = JSON.parse(fs.readFileSync('../DataDump/DoctorGen.json').toString())
patientGenerator = JSON.parse(fs.readFileSync('../DataDump/PatientGen.json').toString())
treatmentGenerator = JSON.parse(fs.readFileSync('../DataDump/TreatmentGen.json').toString())

web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
contract = web3.eth.contract(abi);
contractInstance = contract.at(contractAddress);

// generating 5 doctors
console.log('Doctor data is being generated...')
for (var i = 0; i < 5; i++) {
    contractInstance.addDoctor('abc', doctorGenerator[i].age, doctorGenerator[i].sex, doctorGenerator[i].specialities, { from: web3.eth.accounts[i], gas: 3000000 }, function (e, r) {
        console.log(e)
    })
}

//generating 5 patients
console.log('Patient data is being generated...')
for (var i = 0; i < 5; i++) {
    startFrom = 5
    console.log(web3.eth.accounts[i + startFrom])
    console.log(patientGenerator[i])

    contractInstance.addPatient('abc', patientGenerator[i].age, patientGenerator[i].sex, patientGenerator[i].currentDisease, patientGenerator[i].currentTreatment, patientGenerator[i].treatmentConstraints, { from: web3.eth.accounts[i + startFrom], gas: 3000000 }, function (e, r) {
        console.log(e)
        console.log(r)
    })
}

// generating treatments
console.log('treatment data is being generated...')
treatmentGenerator.forEach(function (val, i) {
    startFrom = 5
    contractInstance.issueTreatmentRecord(web3.eth.accounts[i + startFrom], val.treatment, val.status, val.disease, { from: web3.eth.accounts[i], gas: 3000000 }, function () {

    })
    contractInstance.issueTreatmentRecord(web3.eth.accounts[startFrom], val.treatment, val.status, val.disease, { from: web3.eth.accounts[i], gas: 3000000 }, function () {

    })
})
