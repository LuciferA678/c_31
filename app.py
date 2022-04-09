#!pip install flask
from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
'''
# import numpy as np
# from sklearn.linear_model import LinearRegression 
---------------------------
# reg = LinearRegression() Instance
-----------------------------
# reg.fit(X, y) Method
# reg.predict(np.array([[3, 5]]))
This is just for your refrence 
'''
model = pickle.load(open("c_31_lr_model.pkl","rb"))
# Intialization of Flask
app = Flask(__name__)# It takes care of your dir structure to render Html pages and css from specific folder

#@app.route("/<name>") # It binds the wrbiste url with below fuction 
#def radhika(name):
#    return '<Html><h1>'+ "Hello "+name+" ahsjkd to the flask"

@app.route("/") # It binds the wrbiste url with below fuction 
def homepage():
    return render_template('index.html')

@app.route("/predict",methods=['POST']) # It binds the wrbiste url with below fuction 
def predict():
    int_features = [np.array([int(x) for x in request.form.values()])]
    pred = model.predict(int_features)
    return render_template('index.html',prediction_text=pred)

if __name__=="__main__":
    app.run(port=5001,debug=True)