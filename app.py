import streamlit as st
from joblib import load
import numpy as np

# Since the model and scaler files are in the same directory as this script,
# you don't need to specify a subdirectory path.
model = load('Grade_prediction.joblib')
scaler = load('Scaler.joblib')

# Define the prediction function
def predict_grade(G1, G2, failures, absences):
    # Preprocess inputs
    inputs = np.array([[G1, G2, failures, absences]])
    inputs_scaled = scaler.transform(inputs)
    
    # Predict the grade
    prediction = model.predict(inputs_scaled)
    return prediction[0]

# Streamlit app interface
st.title('Grade Prediction App')

st.write('''
         Use this app to predict student grades based on prior performance and other factors.
         ''')

# User inputs
G1 = st.number_input('G1: Grade in first term (0-20 scale)', min_value=0, max_value=20, value=10)
G2 = st.number_input('G2: Grade in second term (0-20 scale)', min_value=0, max_value=20, value=10)
failures = st.number_input('Number of Prior Failures', min_value=0, max_value=10, value=0)
absences = st.number_input('Number of Absences', min_value=0, value=0)

# Predict button
if st.button('Predict Final Grade'):
    prediction = predict_grade(G1, G2, failures, absences)
    st.write(f'The predicted final grade is {prediction:.2f} on a 0-20 scale.')
