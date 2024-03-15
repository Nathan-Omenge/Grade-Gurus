import streamlit as st
from joblib import load
import numpy as np

# Assume these are already in your script:
model = load('Grade_prediction.joblib')
scaler = load('Scaler.joblib')

# Define the prediction function with the output capping logic
def predict_grade(G1, G2, failures, absences):
    # Preprocess inputs
    inputs = np.array([[G1, G2, failures, absences]])
    inputs_scaled = scaler.transform(inputs)
    
    # Predict the grade
    prediction = model.predict(inputs_scaled)
    
    # Cap the prediction to a max of 20 marks and min of 0
    capped_prediction = max(min(prediction[0], 20), 0)
    
    return capped_prediction

# Streamlit app interface setup (assuming this is already in your script)
st.title('Grade Prediction App')
# Your code to collect user inputs goes here...

# When the Predict button is pressed:
if st.button('Predict Final Grade'):
    # Collect inputs and predict
    prediction = predict_grade(G1, G2, failures, absences)
    
    # Display the capped prediction
    st.write(f'The predicted final grade is {prediction:.2f} on a 0-20 scale.')

