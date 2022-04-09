#!pip install flask
from flask import Flask
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

# Intialization of Flask
app = Flask(__name__)# It takes care of your dir structure to render Html pages and css from specific folder

@app.route("/<name>") # It binds the wrbiste url with below fuction 
def radhika(name):
    return '<Html><h1>'+ "Hello "+name+" ahsjkd to the flask"

if __name__=="__main__":
    app.run(port=5001,debug=True)