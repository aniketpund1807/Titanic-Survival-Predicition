# Program for the Output page :
import streamlit as st
import math
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.header("Titanic Survival Prediction !")
col1,col2,col3 = st.columns(3)

with col1:
    Pclass = st.selectbox("class of Passenger",("Premiere","Executive","Economy"))

with col2:
    Sex = st.selectbox("Gender",("Male","Female"))

with col3:
    Age = st.number_input("Age of Passenger")


col4,col5 = st.columns(2)

with col4:
    SibSp = st.number_input("Sibling/Spouses")

with col5:
    Parch = st.number_input("Parents/Childern")


col6,col7 = st.columns(2)

with col6:
    Fare = st.number_input("Fare of Journey")

with col7:
    Embarked = st.selectbox("Pickup Point",("Cherbourg","Queenstown","Southampton"))

if st.button("Predict"):
    Pclass = 1
    if Pclass == "Economy":
        Pclass = 3

    elif Pclass =="Executive":
        Pclass = 2

    gender = 0
    if Sex == "Female":
        gender = 1

    age = math.ceil(Age)
    sibsp = math.ceil(SibSp)
    Parch = math.ceil(Parch)
    fare = math.ceil(Fare)

    Embarked = 0
    if Embarked == "Cherbourg":
        Embarked = 1
    
    elif Embarked == "Queenstown":
        Embarked = 2

    result = model.predict([[Pclass,gender,age,SibSp,Parch,fare,Embarked]])
    output_label = {1:"The Passenger  will Survive",
                    0: "The Passenger will not Survive"}
    st.markdown(f"{output_label[result[0]]}")

