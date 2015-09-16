from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
	    return render_template("index.html")
    else: 
        number = request.form['phoneNumber'] 
        message = request.form['message'] 
        payload = {'number': number, 'message': message}
        r = requests.post("http://textbelt.com/text", data=payload)
        return render_template("submit.html")
	
app.run(host=os.environ['IP'],port=int(os.environ['PORT']))
app.run(debug=True)
	


   
   
	

