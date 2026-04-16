import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('model_diabetes.pkl')

st.title("Prediksi Diabetes")

# Input user
pregnancies = st.number_input("Pregnancies")
glucose = st.number_input("Glucose")
blood_pressure = st.number_input("Blood Pressure")
skin_thickness = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
dpf = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")

# Prediksi
if st.button("Prediksi"):
    input_data = np.array([[pregnancies, glucose, blood_pressure,
                            skin_thickness, insulin, bmi, dpf, age]])
    
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("Terindikasi Diabetes")
    else:
        st.success("Tidak Diabetes")