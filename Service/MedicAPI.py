from flask import Flask,request
from flask_restful import Resource, Api, reqparse
import os
import Patient
import Doctor
app = Flask(__name__)
api = Api(app)
@app.route('/')
class MedicPatientDetails (Resource):
    def post(self):
        id = 999011
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        if (args['id']):
            id = args['id']
        print('aaa' + str(id))
        data = Patient.getPatientDetails(id)
        return (data)
class MedicDoctorDetails (Resource):
    def post(self):
        id = 9990
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        if (args['id']):
            id = args['id']
        data = Doctor.getDoctorDetails(id)
        return (data)

class MedicPatientHistory (Resource):
    def post(self):
        id='33444444'
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        print(args['id'])
        if(args['id']):
               id = args['id']
        data = Patient.getPatientHistory(id)
        return  (data)
class MedicCreatePrescription (Resource):
    def post(self):
        patientPublicKey=0
        doctorPublicKey=0
        treatments=''
        treatmentStatus=''
        disease=''
        arguments=['patientPublicKey','doctorPublicKey','treatments','treatmentStatus','disease']
        parser = reqparse.RequestParser()
        for argument in arguments:
            parser.add_argument(argument)
        args = parser.parse_args()
        if(args['patientPublicKey']):
            patientPublicKey = args['patientPublicKey']
        if(args['doctorPublicKey']):
               doctorPublicKey = args['doctorPublicKey']
        if(args['treatments']):
               treatments = args['treatments']
        if(args['treatmentStatus']):
               treatmentStatus = args['treatmentStatus']
        if(args['disease']):
               disease = args['disease']
        return (Doctor.issueTreatmentRecord(doctorPublicKey, patientPublicKey, treatments, treatmentStatus, disease ))
class MedicDisplayUnattendedPatientsDetails (Resource):
    def post(self):
        id='33444444'
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        print(args['id'])
        if(args['id']):
               id = args['id']
        data = Doctor.displayUnattendedPatientsDetails(id)
        return  (data)

class Test (Resource):
    def post(self):
        data = Patient.testFunc()
        return (data)
    def get(self):
        data = Patient.testFunc()
        return (data)
api.add_resource(MedicDoctorDetails, '/doctorDetails')
api.add_resource(MedicPatientDetails,'/patientDetails')
api.add_resource(MedicPatientHistory,'/patientHistory')
api.add_resource(MedicCreatePrescription,'/createPrescription')
api.add_resource(MedicDisplayUnattendedPatientsDetails,'/unattendedPatients')
api.add_resource(Test,'/test')


if __name__ == '__main__':
       port = int(os.environ.get('PORT', 5000))
app.run("0.0.0.0",port=port)
