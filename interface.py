from flask import Flask, render_template, jsonify, render_template_string,request
import config
from Diabetes_Final.utils import Diabetes_Data

app = Flask(__name__)

@app.route('/')     # Home API

def hello_flask():
    print('Welcome to Data Science')
    return 'asdf'

@app.route('/Diabetes_predict')

def Diabetes_status():
    Glucose = 148
    BloodPressure = 50
    SkinThickness = 35
    Insulin       = 0
    BMI           = 33.6
    DiabetesPedigreeFunction = 0.627
    Age                      = 50

    Diabetes_status_pred = Diabetes_Data(Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
    Diabetes_status_pred.Diabetes_model()
    
    
    return jsonify({'Result':f'Diabetes prediction is{Diabetes_status_pred}'})


if __name__ == '__main__':
    app.run()
