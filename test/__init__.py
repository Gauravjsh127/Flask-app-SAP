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

TestREST_APISs = Namespace('/Test', description='Test Microservices: CRUD operations')

REST_APIS.add_namespace(TestREST_APISs, path='/Test')

@TestREST_APISs.route("/")
class TestREST_APIS(Resource):
    def get(self):
        """Delete Data"""
        return "Got all Data successfully", 200


    @TestREST_APISs.expect(DATA_PARSER)
    @TestREST_APISs.response(200, 'Data added successfully')
    @TestREST_APISs.response(400, 'Bad request')
    def post(self):
        """Create Data"""
        return "Data added successfully", 200


    @TestREST_APISs.expect(DATA_PARSER)
    @TestREST_APISs.response(200, 'Data updated successfully')
    @TestREST_APISs.response(400, 'Bad request')
    def put(self):
        """Update Data"""
        return "Data updated successfully", 200


    @TestREST_APISs.expect(DATA_PARSER)
    @TestREST_APISs.response(200, 'Data deleted successfully')
    @TestREST_APISs.response(400, 'Bad request')
    def delete(self):
        """Deleted data"""
        return "Data deleted successfully", 200