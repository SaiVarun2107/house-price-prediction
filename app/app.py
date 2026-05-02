import streamlit as st
import pandas as pd
import pickle
import os

# Load trained model
model_path = os.path.join("models", "house_price_model.pkl")
model = pickle.load(open(model_path, "rb"))

# App title
st.title("🏠 House Price Prediction App")

st.write("Enter house details to predict the price.")

# User Inputs
house_id = st.number_input("House ID", min_value=1, value=1)

area = st.number_input("Area (sq ft)", min_value=500, max_value=10000, value=2500)

bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)

bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)

floors = st.number_input("Floors", min_value=1, max_value=5, value=2)

year_built = st.number_input("Year Built", min_value=1900, max_value=2025, value=2005)

location = st.selectbox(
    "Location",
    ["Rural", "Suburban", "Urban"]
)

condition = st.selectbox(
    "Condition",
    ["Fair", "Good", "Poor"]
)

garage = st.selectbox(
    "Garage",
    ["Yes", "No"]
)

# Convert categorical values into encoded values

location_rural = 1 if location == "Rural" else 0
location_suburban = 1 if location == "Suburban" else 0
location_urban = 1 if location == "Urban" else 0

condition_fair = 1 if condition == "Fair" else 0
condition_good = 1 if condition == "Good" else 0
condition_poor = 1 if condition == "Poor" else 0

garage_yes = 1 if garage == "Yes" else 0

# Prepare data for prediction
sample_data = [[
    house_id,
    area,
    bedrooms,
    bathrooms,
    floors,
    year_built,
    location_rural,
    location_suburban,
    location_urban,
    condition_fair,
    condition_good,
    condition_poor,
    garage_yes
]]

# Column names
columns = [
    "Id",
    "Area",
    "Bedrooms",
    "Bathrooms",
    "Floors",
    "YearBuilt",
    "Location_Rural",
    "Location_Suburban",
    "Location_Urban",
    "Condition_Fair",
    "Condition_Good",
    "Condition_Poor",
    "Garage_Yes"
]

sample_df = pd.DataFrame(sample_data, columns=columns)

# Prediction Button
if st.button("Predict House Price"):

    prediction = model.predict(sample_df)

    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")