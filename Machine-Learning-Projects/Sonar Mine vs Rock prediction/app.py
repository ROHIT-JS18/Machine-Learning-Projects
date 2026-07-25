import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Page settings
st.set_page_config(
    page_title="Sonar Rock vs Mine Prediction",
    page_icon="🌊",
    layout="wide"
)

st.title("🌊 Sonar Rock vs Mine Prediction")
st.write("Enter the 60 sonar feature values below and click **Predict**.")

# Create 60 input fields (5 columns)
input_data = []

cols = st.columns(5)

for i in range(60):
    with cols[i % 5]:
        value = st.number_input(
            f"Feature {i+1}",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            format="%.5f"
        )
        input_data.append(value)

# Prediction button
if st.button("🔍 Predict"):

    input_array = np.array(input_data).reshape(1, -1)

    prediction = model.predict(input_array)

    st.subheader("Prediction Result")

    if prediction[0] == "R":
        st.success("🪨 The object is predicted as **Rock**")
    else:
        st.error("💣 The object is predicted as **Mine**")