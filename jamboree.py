import streamlit as st
import pandas as pd
import datetime
import pickle
import sklearn
from sklearn.preprocessing import StandardScaler

jamboree = pd.read_csv('./Jamboree_Admission.csv')
st.write('''# Jamboree Admission Data''')
st.dataframe(jamboree.head())

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

col1, col2 = st.columns(2)

with col1:
    GRE_Score = st.number_input("GRE Score", min_value=0, max_value=340, step=1, value=320)
    University_Rating = st.number_input("University Rating", min_value=1, max_value=5, step=1, value=3)
    CGPA = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.01, value=8.5)

with col2:
    TOEFL_Score = st.number_input("TOEFL Score", min_value=0, max_value=120, step=1, value=110)
    LOR = st.number_input("LOR (Letter of Recommendation)", min_value=0.0, max_value=5.0, step=0.5, value=4.0)
    Research = st.selectbox("Research Experience (Yes=1, No=0)", [1, 0])

# input_features = ['GRE Score', 'TOEFL Score', 'University Rating', 'LOR', 'CGPA', 'research']
def model_pred(GRE_Score, TOEFL_Score, University_Rating, LOR, CGPA, Research):
    with open('jamboree_model.pkl', 'rb') as file:
        reg_model = pickle.load(file)
        input_features = pd.DataFrame([[GRE_Score, TOEFL_Score, University_Rating, LOR, CGPA, Research]], 
                                  columns=['GRE Score', 'TOEFL Score', 'University Rating', 'LOR', 'CGPA', 'Research'])
        
        input_features_scaled = scaler.transform(input_features)
        return reg_model.predict(input_features_scaled)

if (st.button('Predict the Chance of Admission')):
    Admission_Probability = model_pred(GRE_Score, TOEFL_Score, University_Rating, LOR, CGPA, Research)

    st.text(f'The probability of admission is {Admission_Probability}%')



