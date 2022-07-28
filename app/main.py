from flask import Flask,request
 
app = Flask(__name__)
#google_cloud_stuff
PASSWORD ="sahi666"
PUBLIC_IP_ADDRESS ="34.173.189.62"
DBNAME ="database name"
PROJECT_ID ="gcp project id"
INSTANCE_NAME ="instance name"
 
@app.route("/",methods=['GET'])
def home_view():
        return "hello"
@app.route('/sensor/data',methods=['GET','POST'])
def posting():
    content=request.get_json()
    print(content)
    return content