import streamlit as st
import joblib
import numpy as np

# Load the trained model
loaded_model = joblib.load("house_price_model.pkl")

# Title
st.title("🏡 House Price Prediction App")

# Description
st.write("Enter the house details below to predict its price.")

# Create two columns for input fields
col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
    bathrooms = st.number_input("Bathrooms", min_value=1.0, max_value=5.0, value=2.0)
    sqft_living = st.number_input("Sqft Living Area", min_value=500, max_value=10000, value=2000)
    sqft_lot = st.number_input("Sqft Lot", min_value=500, max_value=50000, value=5000)
    floors = st.number_input("Floors", min_value=1.0, max_value=3.0, value=1.0)
    waterfront = st.selectbox("Waterfront", [0, 1])
    view = st.slider("View Score (0-4)", 0, 4, 0)
    condition = st.slider("Condition (1-5)", 1, 5, 3)
    grade = st.slider("Grade (1-13)", 1, 13, 7)

with col2:
    sqft_above = st.number_input("Sqft Above", min_value=500, max_value=5000, value=1500)
    sqft_basement = st.number_input("Sqft Basement", min_value=0, max_value=3000, value=0)
    yr_built = st.number_input("Year Built", min_value=1900, max_value=2023, value=2000)
    yr_renovated = st.number_input("Year Renovated", min_value=0, max_value=2023, value=0)
    lat = st.number_input("Latitude", value=47.5)
    long = st.number_input("Longitude", value=-122.2)
    sqft_living15 = st.number_input("Sqft Living (15 Nearest)", min_value=500, max_value=10000, value=2000)
    sqft_lot15 = st.number_input("Sqft Lot (15 Nearest)", min_value=500, max_value=50000, value=5000)
    years = st.number_input("Years Since Built/Renovation", min_value=0, max_value=100, value=10)

# Convert input into numpy array for model prediction
features = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view,
                      condition, grade, sqft_above, sqft_basement, yr_built, yr_renovated,
                      lat, long, sqft_living15, sqft_lot15, years]])

# Predict Button
if st.button("Predict Price"):
    prediction = loaded_model.predict(features)[0]
    st.success(f"🏠 Estimated House Price: **${prediction:,.2f}**")


