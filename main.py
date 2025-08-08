from fastapi import FastAPI #API keys can accept the input in json model
from pydantic import BaseModel #convert input into json format
import joblib
import numpy as np

ml=joblib.load("D:\\FASTAPI\\demo_iris.pkl")
class iris_inp(BaseModel):
    septal_length:float
    septal_width:float
    petal_length:float
    petal_width:float
app=FastAPI()
spec_clas=["Setosa","Versicolor","Virginica"]
@app.get('/')#Default page
def read_load():
    return "Welcome"
@app.post('/prd')
def prediction(data:iris_inp):
    features=np.array([[data.septal_length,data.septal_width,data.petal_length,data.petal_width]])
    pred_out=ml.predict(features)
    spec_names=spec_clas[int(pred_out[0])]
    return {"Predicted species":spec_names}#uvicorn main:app --reload
    
