from flask import Flask,request
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__)
api = Api(app)
@app.route('/')
class PatientsAttendDetails (Resource):
    def post(self):
        id = 9990
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        if (args['id']):
            id = args['id']
        return {'Patient': 'Nick', 'Disease': 'Influenza', 'id': id}
    def get(self):
        id=9990
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        if(args['id']):
               id=args['id']
        return { 'Patient': 'Nick','Disease': 'Influenza','id':id}
api.add_resource(MedicPatientDetails,'/patientDetails')
class MedicDoctorDetails (Resource):
    def post(self):
        id = 9990
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        if (args['id']):
            id = args['id']
        return {'Doctor': 'Nick', 'Disease': 'Influenza', 'id': id}
    def get(self):
        id=9990
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        if(args['id']):
               id=args['id']
        return { 'Doctor': 'Nick','Disease': 'Influenza','id':id}
api.add_resource(MedicDoctorDetails,'/doctorDetails')
if __name__ == '__main__':
       port = int(os.environ.get('PORT', 5000))
app.run("0.0.0.0",port=port)
