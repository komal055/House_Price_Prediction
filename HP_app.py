import pandas as pd
import pickle as pk
import streamlit as st

with open(r'C:\Users\komal tiwari\Desktop\HOUSE_PRICE_PREDICTION SYSTEM\House_prediction_model.pkl', 'rb') as file:
    model = pk.load(file)

st.header('House Price Predictor')
df = pd.read_csv(r'C:\Users\komal tiwari\Desktop\HOUSE_PRICE_PREDICTION SYSTEM\Cleaned_dataset.csv')

loc = st.selectbox('Choose the location',df['location'].unique())
sqft = st.number_input('Enter total sqft')
beds = st.number_input('Enter number of bedroom')
bath = st.number_input('Enter number of bathrooms')
balc = st.number_input('Enter number of balconies')

input = pd.DataFrame([[loc,sqft,bath,balc,beds]], columns=['location','total_sqft','bath','balcony','bedroom'])

if st.button('Predict Price'):
    output= model.predict(input)
    out_str = "Price of the House is: "+ str(output[0]*100000)
    st.success(out_str)
