import pandas as pd
import numpy as np
import joblib
import streamlit as st

household_income_model_pkl = r"C:\Users\Lenovo\OneDrive\Desktop\Juypter_projects\household_income_model.pkl"
loaded_model = joblib.load(household_income_model_pkl)


# Min-Max normalization parameters(replace with actual values used in training)
income_min = 10000  # Replace with the minimum value used during normalization
income_max = 100000  # Replace with the maximum value used during normalization


st.header("Household Income Analysis")

Age=st.number_input("Enter the Age ")/75

Education_Level = st.selectbox("Enter your Education Level ", ("High School", "Bachelor's", "Master's", "Doctorate"))
Education_Level_dict = {"High School":0, "Bachelor's":1, "Master's":2, "Doctorate":3}
Education_Level = Education_Level_dict[Education_Level]

Occupation = st.selectbox("Enter your Occupation ", ("Healthcare", "Education", "Technology", "Finance", "Others"))
Occupation_dict = {"Healthcare":0, "Education":1, "Technology":2, "Finance":3, "Others":4}
Occupation = Occupation_dict[Occupation]

Number_of_Dependents = st.number_input("Enter the Number of Dependents")

Location = st.selectbox("Enter your location ", ("Urban", "Suburban", "Rural"))
Location_dict = {"Urban":0, "Suburban":1, "Rural":2}
Location = Location_dict[Location]

Work_Experience = st.number_input("Enter your work experience in year")


Employment_Status = st.selectbox("Enter your Occupation ", ("Full-time", "Part-time", "Self-employed"))
Employment_Status_dict = {"Full-time":0, "Part-time":1, "Self-employed":2}
Employment_Status = Employment_Status_dict[Employment_Status]

Household_Size = st.number_input("Enter the size of your house")


Home_ownership_Status = st.selectbox("Enter your house type ", ("Own", "Rent"))
Home_ownership_Status_dict = {"Own":0, "Rent":1}
Home_ownership_Status = Home_ownership_Status_dict[Home_ownership_Status]

Type_of_Housing = st.selectbox("Enter the type of house have", ("Apartment", "Single-family home", "Townhouse"))
Type_of_Housing_dict = {"Apartment":0, "Single-family home":1, "Townhouse":2}
Type_of_Housing = Type_of_Housing_dict[Type_of_Housing]

Gender = st.selectbox("Enter the Sex ", ("Male", "Female"))
Gender_dict = {"Male":0, "Female":1}
Gender = Gender_dict[Gender ]

Primary_Mode_of_Transportation = st.selectbox("Enter your location ", ("Car", "Public transit", "Biking", "Walking"))
Primary_Mode_of_Transportation_dict = {"Car":0, "Public transit":1, "Biking":2, "Walking":3}
Primary_Mode_of_Transportation = Primary_Mode_of_Transportation_dict[Primary_Mode_of_Transportation]


X_new = np.array([[Age, Education_Level, Occupation, Number_of_Dependents, Location, Work_Experience, Employment_Status, Household_Size, Home_ownership_Status, Type_of_Housing, Gender, Primary_Mode_of_Transportation]])

button = st.button("Submit")

if button:
    # st.write("Input Features:", X_new) 
    raw_result = loaded_model.predict(X_new)
    st.write("Normalized Prediction:", raw_result)  
    
    # Inverse normalization for Min-Max scaling
    scaled_result = raw_result[0] * (income_max - income_min) + income_min
    
    # Round the result to two decimal places
    result = np.round(scaled_result, 2)
    st.info(f"Predicted Household Income: ${result:,.2f}")




