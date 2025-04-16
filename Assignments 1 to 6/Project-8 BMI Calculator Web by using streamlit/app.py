import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Height (cm)", min_value=50, max_value=250, value=170, step=1)
weight = st.slider("Weight (kg)", min_value=20, max_value=200, value=70, step=1)

bmi = weight / ((height / 100) ** 2)
st.write(f"Your BMI is {bmi:.2f}")
st.write("BMI Categories:")
st.write("Underweight: < 18.5")
st.write("Normal weight: 18.5 - 24.9")
st.write("Overweight: 25 - 29.9")
st.write("Obese: BMI >= 30")