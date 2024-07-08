import pickle
import streamlit as st

# Load the trained model
Heart_disease_model = pickle.load(open('Cvd_prediction.sav', 'rb'))

# Mapping for General Health options
general_health_mapping = {'Excellent': 0, 'Fair': 1, 'Good': 2, 'Poor': 3, 'Very Good': 4}

# Mapping for Checkup options
checkup_mapping = {'5 or more years ago': 0, 'Never': 1, 'Within the past 2 years': 2, 'Within the past 5 years': 3, 'Within the past year': 4}

# Mapping for Exercise options
exercise_mapping = {'No': 0, 'Yes': 1}

# Mapping for Yes/No options
yes_no_mapping = {'No': 0, 'Yes': 1}

# Mapping for sex options
sex_mapping = {'Female': 0, 'Male': 1}

# Mapping for Diabetes options
diabetes_mapping = {'No': 0, 'Yes': 1 , 'Yes, but female told only during pregnancy': 2}


# Mapping for Age categories
age_category_mapping = {'18-24': 0, '25-29': 1, '30-34': 2, '35-39': 3, '40-44': 4, '45-49': 5, '50-54': 6,
                        '55-59': 7, '60-64': 8, '65-69': 9, '70-74': 10, '75-79': 11, '80+': 12}


# Streamlit UI
st.title('Heart Disease Prediction System')


st.markdown("### Please fill in the following details to predict the risk of heart disease.")

# Input fields
with st.form(key='input_form'):
    General_Health = st.selectbox('General Health', options=['Select an option'] + list(general_health_mapping.keys()))
    Checkup = st.selectbox('Frequency of Checkup', options=['Select an option'] + list(checkup_mapping.keys()))
    Exercise = st.selectbox('Exercise', options=['Select an option'] + list(exercise_mapping.keys()))
    Skin_Cancer = st.selectbox('Skin Cancer', options=['Select an option'] + list(yes_no_mapping.keys()))

    Other_Cancer = st.selectbox('Other Cancer', options=['Select an option'] + list(yes_no_mapping.keys()))
    Depression = st.selectbox('Depression', options=['Select an option'] + list(yes_no_mapping.keys()))
    Diabetes = st.selectbox('History of Diabetes', options=['Select an option'] + list(diabetes_mapping.keys()))
    Arthritis = st.selectbox('Arthritis', options=['Select an option'] + list(yes_no_mapping.keys()))

    Sex = st.selectbox('Sex', options=['Select an option'] + list(sex_mapping.keys()))
    Age_Category = st.selectbox('Age', options=['Select an option'] + list(age_category_mapping.keys()))
    Height_cm = st.text_input('Height (In Cm)')
    Weight_kg = st.text_input('Weight (In Kgs)')

    # Add another row for additional input fields
    st.subheader('Additional Information')
    with st.expander('Click to expand'):
        BMI = st.text_input('Body Mass Index (Weight/Square of height(in meter))')
        Smoking_History = st.selectbox('Smoking History', options=['Select an option'] + list(yes_no_mapping.keys()))
        Alcohol_Consumption = st.text_input('Alcohol Consumption (0-30)')
        Fruit_Consumption = st.text_input('Fruit Consumption (0-120)')
        Green_Vegetables_Consumption = st.text_input('Green Vegetables Consumption (0-128)')
        FriedPotato_Consumption = st.text_input('Fried Potato Consumption (0-128)')

    # Prediction button
    submit_button = st.form_submit_button(label='Predict')


# Code to clear all input fields
if st.button('Clear'):
    st.session_state.General_Health = None
    st.session_state.Checkup = None
    st.session_state.Exercise = None
    st.session_state.Skin_Cancer = None
    st.session_state.Other_Cancer = None
    st.session_state.Depression = None
    st.session_state.Diabetes = None
    st.session_state.Arthritis = None
    st.session_state.Sex = None
    st.session_state.Age_Category = None
    st.session_state.Height_cm = ''
    st.session_state.Weight_kg = ''
    st.session_state.BMI = ''
    st.session_state.Smoking_History = None
    st.session_state.Alcohol_Consumption = ''
    st.session_state.Fruit_Consumption = ''
    st.session_state.Green_Vegetables_Consumption = ''
    st.session_state.FriedPotato_Consumption = ''
    st.session_state.submit_button = False  # Reset submit button state

# Code for prediction
Heart_diagnosis = ''
if submit_button:
    # Validate input field
    # Convert input data to appropriate numerical format
     General_Health = general_health_mapping[General_Health]
     Checkup = checkup_mapping[Checkup]
     Exercise = exercise_mapping[Exercise]
     Skin_Cancer = yes_no_mapping[Skin_Cancer]
     Other_Cancer = yes_no_mapping[Other_Cancer]
     Depression = yes_no_mapping[Depression]
     Diabetes = diabetes_mapping[Diabetes]
     Arthritis = yes_no_mapping[Arthritis]
     Sex = sex_mapping[Sex]
     Age_Category = age_category_mapping[Age_Category]
     Height_cm = float(Height_cm)
     Weight_kg = float(Weight_kg)
     BMI = float(BMI)
     Smoking_History = yes_no_mapping[Smoking_History]
     Alcohol_Consumption = float(Alcohol_Consumption)
     Fruit_Consumption = float(Fruit_Consumption)
     Green_Vegetables_Consumption = float(Green_Vegetables_Consumption)
     FriedPotato_Consumption = float(FriedPotato_Consumption)

    # Make prediction
Heart_DiseaseRisk_pred = Heart_disease_model.predict([[General_Health, Checkup, Exercise, Skin_Cancer, Other_Cancer, Depression, Diabetes, Arthritis,
                                                           Sex, Age_Category, Height_cm, Weight_kg, BMI, Smoking_History, Alcohol_Consumption, Fruit_Consumption,
                                                           Green_Vegetables_Consumption, FriedPotato_Consumption]])

    # Interpret prediction
if Heart_DiseaseRisk_pred[0] == 'No':
        Heart_diagnosis = 'The person is not at heart disease risk'
else:
        Heart_diagnosis = 'The person is at heart disease risk'
        
# Display result
st.success(Heart_diagnosis)
