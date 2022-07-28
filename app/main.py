from flask import Flask,request
 
app = Flask(__name__)
 
@app.route("/",methods=['GET'])
def home_view():
        return "hello"
@app.route('/sensor/data',methods=['POST'])
def posting():
    content=request.get_json()
    print(content)
    return content