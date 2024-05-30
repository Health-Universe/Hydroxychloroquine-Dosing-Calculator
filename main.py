import streamlit as st

# Title and description
st.title("Hydroxychloroquine (Plaquenil) Dosing Calculator")
st.write("""
### Welcome to the Hydroxychloroquine (Plaquenil) Dosing Calculator
This application helps healthcare providers calculate the appropriate dosing of Hydroxychloroquine (Plaquenil) based on patient weight, age, and the condition being treated. 
Enter the required information to get the dosing recommendation.
""")

# User inputs
weight_kg = st.number_input("Patient Weight (kg)", min_value=1, max_value=200, value=70)
age_years = st.number_input("Patient Age (years)", min_value=1, max_value=120, value=30)
condition = st.selectbox(
    "Condition Being Treated",
    ["Malaria", "Rheumatoid Arthritis", "Lupus"]
)

# Dosing guidelines based on condition
def calculate_dosing(weight_kg, age_years, condition):
    if condition == "Malaria":
        dose_mg = weight_kg * 13  # Example calculation for malaria prophylaxis
        dosing_schedule = "Single dose, repeated in 6-8 hours if needed."
    elif condition == "Rheumatoid Arthritis":
        dose_mg = weight_kg * 6.5  # Example calculation for rheumatoid arthritis
        if dose_mg > 400:
            dose_mg = 400  # Maximum daily dose
        dosing_schedule = "Once daily."
    elif condition == "Lupus":
        dose_mg = weight_kg * 6.5  # Example calculation for lupus
        if dose_mg > 400:
            dose_mg = 400  # Maximum daily dose
        dosing_schedule = "Once daily."
    else:
        dose_mg = 0
        dosing_schedule = "No dosing information available."
    
    return dose_mg, dosing_schedule

# Calculate and display dosing
dose_mg, dosing_schedule = calculate_dosing(weight_kg, age_years, condition)
st.subheader(f"Recommended Dose: {dose_mg:.2f} mg")
st.subheader(f"Dosing Schedule: {dosing_schedule}")

