from web3 import Web3, HTTPProvider, IPCProvider, TestRPCProvider
import json
import configparser
import time

web3 = Web3(HTTPProvider("http://10.10.1.90:8545"))
#web3 = Web3(TestRPCProvider(host='127.0.0.1', port=8545))
config = configparser.ConfigParser()
config.read('config')
abiJsonString = config['Contract_info']['abi_json']
#abiJsonString ='[{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"sex","type":"string"}],"name":"changePatientSex","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"age","type":"uint8"}],"name":"changePatientAge","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"doctor","type":"address"}],"name":"getDoctorDetail","outputs":[{"components":[{"name":"age","type":"uint8"},{"name":"sex","type":"string"},{"name":"specialities","type":"string"}],"name":"","type":"tuple"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"}],"name":"getPatientDetail","outputs":[{"components":[{"name":"age","type":"uint8"},{"name":"sex","type":"string"},{"name":"currentDiseases","type":"string"},{"name":"currentTreatments","type":"string"},{"name":"treatmentRestrictions","type":"string"}],"name":"","type":"tuple"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"age","type":"uint8"}],"name":"changeAge","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"treatments","type":"string"},{"name":"treatmentStatus","type":"string"},{"name":"disease","type":"string"}],"name":"issueTreatmentRecord","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"currentDiseases","type":"string"}],"name":"changePatientCurrentDiseases","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"treatmentRestrictions","type":"string"}],"name":"changePatientTreatmentRestrictions","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"currentTreatments","type":"string"}],"name":"changePatientCurrentTreatments","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"age","type":"uint8"},{"name":"sex","type":"string"},{"name":"currentDiseases","type":"string"},{"name":"currentTreatments","type":"string"},{"name":"treatmentRestrictions","type":"string"}],"name":"addPatient","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"age","type":"uint8"},{"name":"sex","type":"string"},{"name":"specialities","type":"string"}],"name":"addDoctor","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"specialities","type":"string"}],"name":"changeSpecialities","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"disease","type":"string"},{"name":"symptomList","type":"string"}],"name":"addDisease","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"sex","type":"string"}],"name":"changeSex","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"doctor","type":"address"},{"indexed":false,"name":"patient","type":"address"},{"indexed":false,"name":"treatments","type":"string"},{"indexed":false,"name":"status","type":"string"},{"indexed":false,"name":"disease","type":"string"}],"name":"Treatment","type":"event"}]'
#print ('data'+abiJsonString)
contract_address = config['Contract_info']['contract_address']
#print ('asdf'+contract_address)
abi_json = json.loads(abiJsonString)
contract = web3.eth.contract(abi=abi_json, address=contract_address)


def vote_callback(r):
    print(r)

def getPatientDetails(public_key):
#contract.transact().someMethod()
    print(public_key)
    print(type((public_key)))
    #print(web3.toBytes(public_key))
    # print(web3.toText(public_key))
    # print(web3.toChecksumAddress(public_key))
    # print(web3.toHex(public_key))
    arg_list = contract.call().getPatientDetail(public_key)
    #filters = contract.on("Treatment", filter_params={'filter': { 'patient': public_key},'fromBlock':0, 'toBlock':'latest'})
#print(filter.filter_id)
    #print(filters.get(False))
    #data = filters.get(False)
    #arg_list=[]
    #for d in data:
     #   print (d['args'])
      #  if(d['args']['patient']==public_key):
       #     print(d['args'])
        #    arg_list.append(d['args'])
    if(str(arg_list[2])=='m'):
        arg_list[2]='Male'
    else:
        arg_list[2] = 'Female'
    arg_json={
        'age':arg_list[1],
        'sex':arg_list[2],
        'currentDisease':arg_list[3],
        'currentTreatment':arg_list[4],
        'treatmentConstraints':arg_list[5]
    }
    print (arg_json)
    return (arg_json)


def getPatientHistory(public_key):
    print(public_key)
    public_key=str(public_key)

#contract.transact().someMethod()
#contract.call().return13()
    filters = contract.on("Treatment", filter_params={'filter': { 'patient': public_key},'fromBlock':0, 'toBlock':'latest'})
#print(filter.filter_id)
    #print(filters.get(False))
    data = filters.get(False)
    arg_list=[]
    for d in data:
        #print (d['args'])
        patient = d['args']['patient']
        #print(patient,public_key,patient==public_key)

        if(patient==public_key):
            #print(d['args'])
            #print('asdf'+d['args']['patient'])
            d['args'].pop('patient')
            d['args'].pop('doctor')
            arg_list.append(d['args'])
    #print (arg_list)
    return (arg_list)

def testFunc():
    web3 = Web3(HTTPProvider("http://10.10.1.90:8545"))
    # web3 = Web3(TestRPCProvider(host='127.0.0.1', port=8545))
    config = configparser.ConfigParser()
    config.read('config')
    abiJsonString = config['Contract_info']['abi_json']
    # abiJsonString ='[{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"sex","type":"string"}],"name":"changePatientSex","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"age","type":"uint8"}],"name":"changePatientAge","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"doctor","type":"address"}],"name":"getDoctorDetail","outputs":[{"components":[{"name":"age","type":"uint8"},{"name":"sex","type":"string"},{"name":"specialities","type":"string"}],"name":"","type":"tuple"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"}],"name":"getPatientDetail","outputs":[{"components":[{"name":"age","type":"uint8"},{"name":"sex","type":"string"},{"name":"currentDiseases","type":"string"},{"name":"currentTreatments","type":"string"},{"name":"treatmentRestrictions","type":"string"}],"name":"","type":"tuple"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"age","type":"uint8"}],"name":"changeAge","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"treatments","type":"string"},{"name":"treatmentStatus","type":"string"},{"name":"disease","type":"string"}],"name":"issueTreatmentRecord","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"currentDiseases","type":"string"}],"name":"changePatientCurrentDiseases","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"treatmentRestrictions","type":"string"}],"name":"changePatientTreatmentRestrictions","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"patient","type":"address"},{"name":"currentTreatments","type":"string"}],"name":"changePatientCurrentTreatments","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"age","type":"uint8"},{"name":"sex","type":"string"},{"name":"currentDiseases","type":"string"},{"name":"currentTreatments","type":"string"},{"name":"treatmentRestrictions","type":"string"}],"name":"addPatient","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"age","type":"uint8"},{"name":"sex","type":"string"},{"name":"specialities","type":"string"}],"name":"addDoctor","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"specialities","type":"string"}],"name":"changeSpecialities","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"disease","type":"string"},{"name":"symptomList","type":"string"}],"name":"addDisease","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"sex","type":"string"}],"name":"changeSex","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"doctor","type":"address"},{"indexed":false,"name":"patient","type":"address"},{"indexed":false,"name":"treatments","type":"string"},{"indexed":false,"name":"status","type":"string"},{"indexed":false,"name":"disease","type":"string"}],"name":"Treatment","type":"event"}]'
    # print ('data'+abiJsonString)
    contract_address = config['Contract_info']['contract_address']
    # print ('asdf'+contract_address)
    abi_json = json.loads(abiJsonString)
    contract = web3.eth.contract(abi=abi_json, address=contract_address)
    arg_list = contract.call().test()
    # filters = contract.on("Treatment", filter_params={'filter': { 'patient': public_key},'fromBlock':0, 'toBlock':'latest'})
    # print(filter.filter_id)
    # print(filters.get(False))
    # data = filters.get(False)
    # arg_list=[]
    # for d in data:
    #   print (d['args'])
    #  if(d['args']['patient']==public_key):
    #     print(d['args'])
    #    arg_list.append(d['args'])
    print(arg_list)
    return (arg_list)

#getPatientDetails('0x3De99db1247032bD78C73094A45d89708047D894')
#filter.watch(vote_callback)
#print(web3.eth.getFilterLogs(filter.filter_id))
