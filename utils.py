import numpy as np
import pickle
import config
import json

class Diabetes_Data():
    def __init__(self, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
     self.Glucose = Glucose
     self.BloodPressure = BloodPressure
     self.SkinThickness = SkinThickness
     self.Insulin = Insulin
     self.BMI = BMI
     self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
     self.Age = Age

    def load_model(self):
        with open(config.PKL_FILE,'rb') as f:
            self.PKL = pickle.load(f)

        with open(config.JSON_FILE,'r') as f:
            self.JSON = json.load(f)

    def Diabetes_model(self):
        self.load_model()

        test_array=np.zeros(len(self.JSON['columns']))
        

        Diabetes_predict = self.PKL.predict([test_array])


        return Diabetes_predict

if __name__ == '__main__':
    Glucose = 148
    BloodPressure = 50
    SkinThickness = 35
    Insulin       = 0
    BMI           = 33.6
    DiabetesPedigreeFunction = 0.627
    Age                      = 50 

    Diabetes_predicted = Diabetes_Data(Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
    Diabetes_predicted.Diabetes_model                  