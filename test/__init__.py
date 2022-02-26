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

TestREST_APISs = Namespace('/Test', description='Endpoints available to manage Test Micro services')

REST_APIS.add_namespace(TestREST_APISs, path='/Test')

@TestREST_APISs.route("/")
class TestREST_APIS(Resource):
    def get(self):
        """Endpoint to get all the Data"""
        return "Test", 200


    @TestREST_APISs.expect(DATA_PARSER)
    @TestREST_APISs.response(200, 'Data added successfully')
    @TestREST_APISs.response(400, 'Bad request')
    def post(self):
        """Add a new Post request"""
        return "Test", 200


