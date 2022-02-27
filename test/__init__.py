import os
from flask import Flask
from flask_restx import Api, Resource, Namespace

Test = Flask(__name__)

REST_APIS = Api(
    app=Test,
    title='Sample Test Microservice : Rest APIs description',
    version='1.0',
    doc='/docs',
    # All REST_APIS metadatas
)

DATA_PARSER = REST_APIS.parser()
DATA_PARSER.add_argument('name', location='form', type=str, required=True)
DATA_PARSER.add_argument('description', location='form', type=str, required=True)

CRUD_APISs = Namespace('/crud', description='Test Microservices: CRUD operations')
REST_APIS.add_namespace(CRUD_APISs, path='/crud')

@CRUD_APISs.route("/")
class TestREST_APIS(Resource):
    def get(self):
        """Delete Data"""
        return "Got all Data successfully", 200


    @CRUD_APISs.expect(DATA_PARSER)
    @CRUD_APISs.response(200, 'Data added successfully')
    @CRUD_APISs.response(400, 'Bad request')
    def post(self):
        """Create Data"""
        return "Data added successfully", 200


    @CRUD_APISs.expect(DATA_PARSER)
    @CRUD_APISs.response(200, 'Data updated successfully')
    @CRUD_APISs.response(400, 'Bad request')
    def put(self):
        """Update Data"""
        return "Data updated successfully", 200


    @CRUD_APISs.expect(DATA_PARSER)
    @CRUD_APISs.response(200, 'Data deleted successfully')
    @CRUD_APISs.response(400, 'Bad request')
    def delete(self):
        """Deleted data"""
        return "Data deleted successfully", 200