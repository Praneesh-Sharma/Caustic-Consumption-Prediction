#Importing libraries
import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title('Caustic Conusmption Prediction')

#User input for model parameters
st.markdown("<h2 style='text-align: left; color: black;'>Model Parameters</h2>", unsafe_allow_html=True)

nfccu = st.slider('NFCCU Feed Rate', 0.0, 220.0, 50.0)
ofccu = st.slider('OFCCU Feed Rate', 0.0, 120.0,  50.0)
ltu = st.slider('LTU Feed Rate', 0.0, 110.0,  50.0)  

st.text('')
st.write("#### Consumption: ")
result = predict(np.array([[nfccu, ofccu, ltu]]))


isom_chk = st.checkbox('Include ISOM Feed Rate')
if isom_chk:
    isom = st.number_input('Enter ISOM Consumption: ')
    st.text(result[0]+isom)
else:
    st.text(result[0])    
