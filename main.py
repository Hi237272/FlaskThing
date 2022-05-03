from flask import Flask,render_template,request,jsonify
from flask_cors import cross_origin
import time
messagesList=[]  
app=Flask(__name__,template_folder='templates')

@app.route('/a',methods=['GET'])
def open():
  return render_template("modal.html")



@app.route('/',methods=['POST'])
@cross_origin(headers=['Content-Type'])
def post():
  recieve = request.get_json()
  print(recieve['Message'])
  return jsonify({"Request":"Completed"})
  
app.run(host='0.0.0.0',port=5640,debug="True")



