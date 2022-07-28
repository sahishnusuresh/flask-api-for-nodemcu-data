from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
#google_cloud_stuff
PASSWORD ="sahi666"
PUBLIC_IP_ADDRESS ="35.222.14.19"
DBNAME ="sensor_data"
PROJECT_ID ="AQ-CLOUD"
INSTANCE_NAME ="flask-esp"
# app.config["SECRET_KEY"] = "yoursecretkey"
# app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql + mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket =/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
 
db = SQLAlchemy(app)
 
# # User ORM for SQLAlchemy
# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key = True, nullable = False)
#     name = db.Column(db.String(50), nullable = False)
#     email = db.Column(db.String(50), nullable = False, unique = True)
 
@app.route("/",methods=['GET'])
def home_view():
        return "hello"
@app.route('/sensor/data',methods=['GET','POST'])
def posting():
    def validateJSON(jsonData):
        try:
            json.loads(json.dumps(jsonData))
        except ValueError as err:
            print("False")
        print("True")
    content=request.get_json()
    print(content)
    print(validateJSON(content))
    return type(content)