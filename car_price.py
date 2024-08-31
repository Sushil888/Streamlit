import streamlit as st
import pandas as pd
import datetime
import pickle

cars_df = pd.read_csv('./cars24.csv')

st.write('''# Cars 24 Data''')

st.dataframe(cars_df)

col1, col2 = st.columns(2)

with col1:
    fuel_type = st.selectbox("Fuel_Type", ["Diesel", "Petrol", "CNG", 'LPG', 'Electric'])

with col2:
    transmission_type = st.selectbox("Transmission Type", ["Manual", "AUtomatic"])

engine_size = st.slider("Engine Power", 500, 5000, step=100)



