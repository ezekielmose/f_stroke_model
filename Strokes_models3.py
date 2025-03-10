
import numpy as np
import pandas as pd
import streamlit as st
import requests
import pickle
import joblib
import io



#model_url = "https://github.com/ezekielmose/Stroke_model/blob/main/strock_model_new.sav"


model_url = 'https://raw.githubusercontent.com/ezekielmose/f_stroke_model/refs/heads/main/strock_model_new2.pkl'


# Fetch the model file from GitHub
response = requests.get(model_url)
response.raise_for_status()  # Ensure we notice bad responses (404, etc.)

# Load the model using pickle
model = pickle.load(io.BytesIO(response.content))


def main():
#input Variables
    
    st.title ("Stroke Prediction Model")

    # Apply custom CSS
    # Apply custom CSS to style the dropdown field and menu
    st.markdown("""
        <style>
            /* Style the dropdown field (where the selected value appears) */
            div[data-baseweb="select"] > div {
                background-color: #ffcccb !important; /* Light Red */
                color: black !important;
                border-radius: 5px;
                padding: 5px;
            }
            
            /* Style the dropdown menu */
            ul {
                background-color: lightblue !important;
            }
    
            /* Style dropdown options */
            li {
                color: black !important;
                font-weight: bold;
            }
    
            /* Change the hover effect on dropdown options */
            li:hover {
                background-color: yellow !important;
                color: red !important;
            }
        </style>
    """, unsafe_allow_html=True)
     
    gender = int(st.selectbox(label = "What is the Gender (0 - Female and 1 - Male)", options = [1, 0]))
    age = float(st.text_input("Enter the age", "0"))
    hypertension = int(st.text_input("Hypertension 0 for -ve and 1 for +ve", "0"))
    heart_disease = int(st.text_input("Heart disease 0 for has and 1 for not", "0"))
    ever_married = int(st.text_input("Ever married 0 for No and 1 for Yes", "0"))
    work_type = int(st.selectbox( label = "Work type 0-private. 1-self-employed, 2-children, 3-gov_job, and 4-never worked", options = [0, 1,2,3,4]))
    Residence_type = int(st.text_input("Residence type 0 for urban and 1 for rural", "0"))
    avg_glucose_level = float(st.text_input("Enter any value of avg_glucose_level as per the measurements", "0"))
    bmi = float(st.text_input("Enter any value of BMI as per the measurements", "0"))
    smoking_status = int(st.text_input("Smoking status 0 for never smoked, 1 for unknown, 2 for formerly smoked, 3 for smokes", "0"))
    
    
#prediction code



    if st.button('CLICK HERE TO PREDICT'):
        makeprediction = model.predict([[gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status]])
        output = round(makeprediction[0])  # Ensure it's an integer (0 or 1)
    
        if output == 0:
            st.success("The patient is **not at risk** of stroke.")
        else:
            st.warning("The patient **is at risk** of stroke. Please consult a doctor.")        


if __name__ == '__main__':
    main()
