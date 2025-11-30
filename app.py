import streamlit as st
import pandas as pd
import joblib


model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")


st.title("Heart stroke  Prediction App")
st.markdown("Provide the following details to predict the  heart stroke.")
age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex", ["Male", "Female"])
chest_pain_type = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
resting_blood_pressure = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dl)", 100, 600, 200)
fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0,1])
rest_ecg = st.selectbox("Resting ECG", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
max_heart_rate = st.slider("Maximum Heart Rate Achieved", 60, 220, 150)
exercise_induced_angina = st.selectbox("Exercise Induced Angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak (St Depression ", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])

if st.button("Predict"):

    # Create a raw input dictionary
    raw_input = {
        'Age': age,
        'RestingBP': resting_blood_pressure,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_blood_sugar,
        'MaxHR': max_heart_rate,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain_type: 1,
        'RestingECG_' +  rest_ecg : 1,
        'ExerciseAngina_' +exercise_induced_angina : 1,
        'ST_Slope_' + slope: 1
    }

    # Initialize all expected columns to 0
    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    
    input_df = input_df[expected_columns]

    # Scale the input data
    scaled_input = scaler.transform(input_df)
    # Make prediction
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error("🤧The model predicts that you are at risk of heart stroke.")    
    else:
        st.success("🤗You are not at risk of heart stroke.")