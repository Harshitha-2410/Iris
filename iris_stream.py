import streamlit as st
import requests

st.title("Iris Flower Prediction")
sl=st.sidebar.slider("Sepal Length",0.0,10.0)
sw=st.sidebar.slider("Sepal width",0.0,10.0)
pl=st.sidebar.slider("Petal Length",0.0,10.0)
pw=st.sidebar.slider("Petal width",0.0,10.0)
sub=st.sidebar.button("Submit")

if sub:
    st.write("Sepal Length",sl)
    st.write("Sepal width",sw)
    st.write("Petal Length",pl)
    st.write("Petal width",pw)

p=st.button("Predict")
if p:
    data={
    "septal_length":sl,
    "septal_width":sw,
    "petal_length":pl,
    "petal_width":pw
    }
    res=requests.post("http://127.0.0.1:8000",json=data)
    result=res.json()
    st.write(result)