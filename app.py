import streamlit as st
from joblib import load

# Load the trained model (ensure the model file is in the same directory as this script)
model = load('grades_predictive_model.joblib')

def predict_grade(absences, G1, G2, prior_failures, health):
    """
    Function to use the loaded model to predict the grade based on user inputs.
    This function assumes the model expects the features in the order: absences, G1, G2, prior_failures, health.
    """
    inputs = [[absences, G1, G2, prior_failures, health]]
    prediction = model.predict(inputs)
    return prediction[0]  # Returning the first prediction

def main():
    st.title("Grade Gurus Prediction App")

    # UI for getting inputs from the user
    st.header("Enter the student's details:")
    
    absences = st.number_input("Number of Absences", min_value=0, value=0, key="absences")
    G1 = st.number_input("G1: Grade in first term (0-20 scale)", min_value=0, max_value=20, value=10, key="G1")
    G2 = st.number_input("G2: Grade in second term (0-20 scale)", min_value=0, max_value=20, value=10, key="G2")
    prior_failures = st.number_input("Number of Prior Failures", min_value=0, max_value=10, value=0, key="prior_failures")
    health = st.select_slider("Health (1-5 scale, where 5 is very healthy)", options=[1, 2, 3, 4, 5], value=3, key="health")
    
    # Button to make prediction
    if st.button("Predict Grade"):
        prediction = predict_grade(absences, G1, G2, prior_failures, health)
        
        st.subheader("Predicted Final Grade:")
        st.write(f"The predicted final grade is {prediction:.2f} on a 0-20 scale.")
        
if __name__ == "__main__":
    main()
