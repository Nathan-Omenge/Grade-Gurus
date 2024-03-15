import streamlit as st
from joblib import load
import numpy as np

# Load the model and scaler
model = load('Grade_prediction.joblib')
scaler = load('Scaler.joblib')

# Streamlit app interface setup
st.title('Grade Prediction App')

st.write('''
         Use this app to predict student grades based on prior performance and other factors.
         ''')

# Define the prediction function
def predict_grade(G1, G2, failures, absences):
    # Preprocess inputs
    inputs = np.array([[G1, G2, failures, absences]])
    inputs_scaled = scaler.transform(inputs)
    
    # Predict the grade
    prediction = model.predict(inputs_scaled)
    
    # Cap the prediction to a max of 20 marks and min of 0
    capped_prediction = max(min(prediction[0], 20), 0)
    
    return capped_prediction

# Collecting user inputs
G1 = st.number_input('G1: Grade in first term (0-20 scale)', min_value=0, max_value=20, value=10)
G2 = st.number_input('G2: Grade in second term (0-20 scale)', min_value=0, max_value=20, value=10)
failures = st.number_input('Number of Prior Failures', min_value=0, max_value=10, value=0)
absences = st.number_input('Number of Absences', min_value=0, value=0)

# When the Predict button is pressed:
if st.button('Predict Final Grade'):
    prediction = predict_grade(G1, G2, failures, absences)  # This line uses the variables collected from user input
    st.write(f'The predicted final grade is {prediction:.2f} on a 0-20 scale.')


