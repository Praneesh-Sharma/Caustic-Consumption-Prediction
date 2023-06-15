#Importing libraries
import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title('Caustic Conusmption Prediction')

#User input for model parameters
st.markdown("<h2 style='text-align: left; color: black;'>Model Parameters</h2>", unsafe_allow_html=True)
st.write("###### Specify Input Parameters: ")

def user_input():
    isom = st.slider('ISOM Feed Rate', 0.0, 45.0, 1.0)
    nfccu = st.slider('NFCCU Feed Rate', 0.0, 250.0, 150.0)
    ofccu = st.slider('OFCCU Feed Rate', 0.0, 200.0,  50.0)
    ltu = st.slider('LTU Feed Rate', 0.0, 150.0,  50.0)
    data = { 'ISOM': isom,
             'NFCCU': nfccu,
             'ofccu': ofccu,
             'LTU': ltu}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input()

#Displaying given input parameters
st.write("###### Specified Input Parameters")
st.write(df)
st.write('---')

#model
prediction = predict(df.to_numpy())

st.write("###### Predicted House Price Value based on the given parameters: ")
st.code(float(prediction))
st.write('---')
