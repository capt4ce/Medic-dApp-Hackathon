from web3 import Web3, HTTPProvider, IPCProvider, TestRPCProvider
import json
import configparser
import operator
import time
web3 = Web3(HTTPProvider("http://10.10.1.90:8545"))
#web3 = Web3(TestRPCProvider(host='127.0.0.1', port=8545))
#print(web3.eth.blockNumber)
config = configparser.ConfigParser()
config.read('config')
abiJsonString = config['Contract_info']['abi_json']
#abiJsonString = '[{"constant":false,"inputs":[],"name":"getCandidates","outputs":[{"name":"","type":"bytes32[]"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"candidate","type":"bytes32"}],"name":"totalVotesFor","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"candidate","type":"bytes32"}],"name":"validCandidate","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"votesReceived","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"candidateList","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"candidate","type":"bytes32"}],"name":"voteForCandidate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"candidateNames","type":"bytes32[]"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"name","type":"bytes32"},{"indexed":true,"name":"voter","type":"address"}],"name":"Vote","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"timestamp","type":"uint256"}],"name":"TotalVotes","type":"event"}]'
abi_json = json.loads(abiJsonString)
#ContractFactory = web3.eth.contract(abi, code="0x00a795bc0a9795be6b97e64a6e21d0185e3db3c5")
#ContractFactory.deploy()
contract_address = config['Contract_info']['contract_address']
contract = web3.eth.contract(abi=abi_json, address=contract_address)
def vote_callback(r):
    print(r)

def getDoctorDetails(public_key):
#print (contract)
#contract.transact().someMethod()
    print(public_key)
    print(type((public_key)))
    arg_list=contract.call().getDoctorDetail(public_key)
#print(contract.call().validCandidate('Rama'))
    #filter = contract.on("Vote", filter_params={'filter':{'name':'Nick\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'},'fromBlock':0, 'toBlock':'latest'})
#print(filter.filter_id)
    #print(filter.get(False))
    #data = filter.get(False)
    #for d in data:
    #    print (d)
    if(str(arg_list[2])=='m'):
        arg_list[2]='Male'
    else:
        arg_list[2] = 'Female'
    arg_json={
        'age':arg_list[1],
        'sex':arg_list[2],
        'speciality':arg_list[3]
    }
    print (arg_json)
    return (arg_json)
#filter.watch(vote_callback)
#print(web3.eth.getFilterLogs(filter.filter_id))
def issueTreatmentRecord(doctor, patient, treatments, treatmentStatus, disease ):

    #function as made in solidity
    contract.transact({'from':doctor}).issueTreatmentRecord(patient, treatments, treatmentStatus, disease)
    return ({'status':'OK', 'code':'200'})

def displayUnattendedPatientsDetails(public_key):
    filters = contract.on("Treatment", filter_params={'fromBlock': 0, 'toBlock': 'latest'})
    # print(filter.filter_id)
    # print(filters.get(False))
    data = filters.get(False)
    print('data')
    print (data)
    arg_list = []
    for d in data:
        # print (d['args'])
        doctor = d['args']['doctor']
        print(doctor)
        # print(patient,public_key,patient==public_key)
        patients=[]
        if (doctor == public_key):
            if(d['args']['patient'] not in patients):
                patients.append(d['args']['patient'])
        print(patients)
        for patient in patients:
            data = contract.call().getPatientDetail(patient)
            print(data)
            if (str(data[2]) == 'm'):
                data[2] = 'Male'
            else:
                data[2] = 'Female'
            arg_json = {
                'age': data[1],
                'sex': data[2],
                'currentDisease': data[3],
                'currentTreatment': data[4],
                'treatmentConstraints': data[5],
                'diseaseSeverity':data[6]
            }
            arg_list.append(arg_json)
        print(arg_list)
    arg_list =sorted(arg_list, key=lambda k: k['diseaseSeverity'])
    return arg_list