import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('model_diabetes.pkl')

st.title("Prediksi Diabetes")

# Input user
pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
glucose = st.number_input("Glucose", min_value=0.0)
blood_pressure = st.number_input("Blood Pressure", min_value=0.0)
skin_thickness = st.number_input("Skin Thickness", min_value=0.0)
insulin = st.number_input("Insulin", min_value=0.0)
bmi = st.number_input("BMI", min_value=0.0, format="%.2f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
age = st.number_input("Age", min_value=0, step=1)

# Prediksi
if st.button("Prediksi"):
    input_data = np.array([[pregnancies, glucose, blood_pressure,
                            skin_thickness, insulin, bmi, dpf, age]])
    
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("Terindikasi Diabetes")
    else:
        st.success("Tidak Diabetes")