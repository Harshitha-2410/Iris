import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
df=load_iris()
data=df.data
label=df.target
x_train,x_test,y_train,y_test=train_test_split(data,label,test_size=0.2)
ml=RandomForestClassifier()
ml.fit(x_train,y_train)
joblib.dump(ml,"D:\\FASTAPI\\demo_iris.pkl")#save the model(pickle file)