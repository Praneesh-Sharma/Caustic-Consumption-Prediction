#Importing libraries
import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title('Caustic Consumption Prediction')

#User input for model parameters
st.markdown("<h3 style='text-align: left; color: black;'>Model Parameters</h3>", unsafe_allow_html=True)

nfccu = st.slider('NFCCU Feed Rate', 0.0, 220.0, 80.0)
ofccu = st.slider('OFCCU Feed Rate', 0.0, 120.0,  80.0)
ltu = st.slider('LTU Feed Rate', 0.0, 110.0,  80.0)  

option = st.selectbox(
    'Time period',
    ('Daily', 'Weekly', 'Fortnightly', 'Monthly', 'Quarterly'))
    # label_visibility="hidden")

st.write('---')

if nfccu>=80 and ofccu>=80 and ltu>=80:
    result = predict(np.array([[nfccu, ofccu, ltu]]))
    isom_chk = st.checkbox('Include ISOM consumption')
    if isom_chk:
        isom = st.number_input('Enter ISOM Consumption: ')
        # st.code(3.14*(result[0]+isom)*0.01*2.50*2.50*1.495*1.4*1.25)
        ans = 3.14*(result[0]+isom)*0.01*2.50*2.50*1.495*1.4*1.25
    else:
        # st.code(3.14*(result[0])*0.01*2.50*2.50*1.495*1.4*1.25)
        ans = 3.14*(result[0])*0.01*2.50*2.50*1.495*1.4*1.25
    
    if option=='Daily':
        st.text("Predicted output in tonne(Daily):")
        st.code(round(ans/7,2))
    elif option=='Weekly':
        st.text("Predicted output in tonne(Weekly):")
        st.code(round(ans,2))
    elif option=='Fortnightly':
        st.text("Predicted output in tonne(Fortnightly):")
        st.code(round(ans*15/7,2))
    elif option=='Monthly':
        st.text("Predicted output in tonne(Monthly):")
        st.code(round(ans*30/7,2))
    elif option=='Quarterly':
        st.text("Predicted output in tonne(Quarterly):")
        st.code(round(ans*12,2))
else:
    st.text("Start-up Phase")

   
