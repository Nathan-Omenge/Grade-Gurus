import streamlit as st
from joblib import load

# Load the trained model (ensure the 'model.joblib' file is in the same directory as this script)
model = load('model.joblib')

def predict_grade(absences, prior_grades, prior_failures, health):
    """
    Function to use the loaded model to predict the grade based on user inputs.
    Adjust this function based on how your model expects input.
    """
    # Example: Assuming the model expects a single array of inputs in the same order
    inputs = [[absences, prior_grades, prior_failures, health]]
    prediction = model.predict(inputs)
    return prediction[0]  # Returning the first prediction

def main():
    st.title("Grade Prediction App")

    # UI for getting inputs from the user
    st.header("Enter the student's details:")
    
    absences = st.number_input("Number of Absences", min_value=0, value=0)
    prior_grades = st.number_input("Average Prior Grades (0-100 scale)", min_value=0, max_value=100, value=75)
    prior_failures = st.number_input("Number of Prior Failures", min_value=0, max_value=10, value=0)
    health = st.select_slider("Health (1-5 scale, where 5 is very healthy)", options=[1, 2, 3, 4, 5], value=3)
    
    # Button to make prediction
    if st.button("Predict Grade"):
        prediction = predict_grade(absences, prior_grades, prior_failures, health)
        
        st.subheader("Predicted Grade:")
        st.write(f"The predicted grade is {prediction:.2f} on a 0-100 scale.")
        
if __name__ == "__main__":
    main()
