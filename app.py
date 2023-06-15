#Importing libraries
import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title('Caustic Conusmption Prediction')

#User input for model parameters
st.markdown("<h2 style='text-align: left; color: black;'>Model Parameters</h2>", unsafe_allow_html=True)
st.write("###### Specify Input Parameters: ")

st.header("Feed Rates:")
col1, col2 = st.columns(2)

with col1:
    isom = st.slider('ISOM Feed Rate', 0.0, 45.0, 1.0)
    nfccu = st.slider('NFCCU Feed Rate', 0.0, 250.0, 150.0)

with col2:
    ofccu = st.slider('OFCCU Feed Rate', 0.0, 200.0,  50.0)
    ltu = st.slider('LTU Feed Rate', 0.0, 150.0,  50.0)

st.text('')
st.write("#### Consumption: ")
result = predict(np.array([[isom, nfccu, ofccu, ltu]]))
st.text(result[0])
