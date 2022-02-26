# Sample Flask microservice Example

This sample flask microservice is to add/readone/readall conditions from sqlitedatabase.

## Setup Locally : conditions microservice (For debug purpose only)

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