import numpy as np
import pandas as pd
import pickle as pkl 
import streamlit as st

model = pkl.load(open('MIPM.pkl', 'rb'))

st.header('Medical Insurance Premium Predictor')
st.image(r"C:\Users\Asus\Desktop\Medical_Insurance_Premium\depositphotos_673217396-stock-photo-health-care-costs-stethoscope-calculator.jpg")
st.subheader("""This project can help insurance companies in pricing strategies and individuals in understanding""")
st.subheader("""their potential insurance costs based on their personal and health characteristics""")

gender = st.selectbox('Choose Gender',['Female','Male'])
smoker = st.selectbox('Are you a smoker ?',['Yes','No'])
region = st.selectbox('Choose Region', ['SouthEast','SouthWest','NorthEast','NorthWest'])
age = st.slider('Enter Age', 5 , 80)
bmi = st.slider('Enter BMI', 5 , 100)
children = st.slider('Choose No of Childrens', 0, 5)


if st.button('Predict'):
    if gender == 'Female':
     gender = 0
    else:
        gender = 1

    if smoker == 'Yes':
        smoker = 1
    elif smoker == 'No':
        smoker = 0
    if region == 'SouthEast':
        region = 0
    if region == 'SouthWest':
        region = 1
    if region == 'NorthEast':
        region = 2
    else:
        smoker = 3

    input_data = (age, gender, bmi, children,smoker, region)
    input_data_array = np.asarray(input_data)
    input_data_array = input_data_array.reshape(1,-1)
    predicted_prem = model.predict(input_data_array)
    display_string = 'Insurance Premium will be '+ str(round(predicted_prem[0],2)) + ' USD Dollars'
    st.balloons()

    st.markdown(display_string)