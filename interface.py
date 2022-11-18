import numpy
import pandas
import Project_app.utils
from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def Home():
    print("This is Boston House Prediction")
    return "Get the price prediction here"

@app.route("/House")
def price_prediction():
    CRIM = 0.06263
    ZN = 0.0
    INDUS = 11.93
    CHAS = 0.0
    NOX = 0.573
    RM = 6.593
    AGE = 69.1
    DIS = 2.4786
    RAD = 1.0
    TAX = 273.0
    PTRATIO = 21.0
    B = 391.99
    LSTAT = 9.67

    value = Project_app.utils.BostonHousePrediction(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
    predicted_value = value.get_price()
    return f'The Predicted House Price is {predicted_value}'

if __name__=='__main__':
    app.run()