# Sample Flask Test microservice Example

This sample flask microservice to perform CRUD operations.

## Setup Locally : Test microservice: Crud operations (For debug purpose only)

- Install python(3+), pip ,venv and vscode(or you can also choose editor of your choice like vscode) 
- checkout the source code.
- cd FLASK-APP-SAP
- virtualenv venv
- .\venv\Scripts\activate
- pip install -r requirements.txt
- python run.py
- Visit the URL for conditions microservice documentation : http://127.0.0.1:5000/docs

Ref: https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-windows-10/

Note: All command on windows command prompt and not power shell

## Deploy App to SAP BTP cloudfoundry

 - cf8 login -a <API_POINT> -o <ORG> -s <SPACE> -u <EMAIL_ID>
 - cf8 push


 ## How to control scaling

 - Horizontal scaling : Creating multiple instance

    cf8 scale <App Name> -i <INSTANCES>

- Vertical scaling: UP/DOWN : Increasing disck space or RAM

    - memory : cf8 scale <APP_NAME> -m 512M
    - diskspace : cf8 scale <APP_NAME> -k 512M

Use quota to increase multiple instance/memory/disk space

All mapping routing is handled internally