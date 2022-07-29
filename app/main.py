from flask import Flask, jsonify,request,make_response
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
#google_cloud_stuff
PASSWORD ="sahi666"
PUBLIC_IP_ADDRESS ="35.222.14.19"
DBNAME ="sensor_data"
PROJECT_ID ="AQ-CLOUD"
INSTANCE_NAME ="flask-esp"
app.config["SECRET_KEY"] = "yoursecretkey"
app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql + mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket =/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
 
db = SQLAlchemy(app)
 

class Sensors(db.Model):
    sensor_id=db.Column(db.String(50), nullable=False)
    aq1_pm10=db.Column(db.Integer, nullable=False)
    aq1_pm75=db.Column(db.Integer, nullable=False)
    aq1_pm25=db.Column(db.Integer,nullable=False)
 
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
    # content=request.get_json()
    # print(content)
    # print(validateJSON(content))
    
    content=request.get_json()
    print(content['aq1']['pm10'])
    
    aq1_pm10=content['aq1']['pm10']
    aq1_pm75=content['aq1']['pm75']
    aq1_pm25=content['aq1']['pm25']
    try:
        sensor=Sensors(
        sensor_id="aq1",
        aq1_pm10=aq1_pm10,
        aq1_pm75=aq1_pm75,
        aq1_pm25=aq1_pm25
        )
        db.session.add(sensor)
        db.session.commit()
        responseObject = {
                'status' : 'success',
                'message': 'Successfully registered.'
            }
 
        return make_response(responseObject, 200)
    except:
            responseObject = {
                'status' : 'fail',
                'message': 'Some error occured !!'
            }
 
            return make_response(responseObject, 400)
@app.route('/view',methods=['GET'])
def show():
    response=list()
    sensors=Sensors.query.all()
    for sensor in sensors:
        response.append({
            "sensor_id":sensor.sensor_id,
            "aq1_pm10":sensor.aq1_pm10,
            "aq1_pm75":sensor.aq1_pm75,
            "aq1_pm25":sensor.aq1_pm25
        })
        return make_response({
        'status' : 'success',
        'message': response
        }, 200)




