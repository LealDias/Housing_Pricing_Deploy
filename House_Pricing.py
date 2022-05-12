# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:34:18 2022

@author: Diego Leal
"""

import streamlit as st
import pickle
from sklearn.preprocessing import RobustScaler
import numpy as np

model = pickle.load(open('RF_model.pkl', 'rb'))


#-----------------------------------------------------------------------------------------------#

def predict_pricing(Income, Ocean_Prox, Population, lg, Bed_per_room, lt):
    
    args = Income, Ocean_Prox, Population, lg, Bed_per_room, lt
    
    array = np.array(args).reshape(1, -1)
    
    transformer = RobustScaler()
    transformer.fit(array)
    transformer.transform(array)
    
    pred = model.predict(array)
    
    return pred
    
#-----------------------------------------------------------------------------------------------#    

def main():
    st.title("Pricing Calculator")
    
    Income = st.text_input("Median Income")
    Ocean_Prox = st.selectbox("Ocean Proximity in Land?", ('Yes', 'No'))
    Population = st.text_input("Population per Household")
    lg = st.text_input("Longitude")
    lt = st.text_input("Latitude")
    Bed_per_room = st.text_input("Bed Rooms per Room")
    
    if Ocean_Prox == 'Yes':
        Ocean_Prox = 1
    else:
        Ocean_Prox = 0    
    
    #st.selectbox("Frutas", ("Morango", "Uva", "Abacaxi"))
    
    res=""
    
    if st.button("Predict"):
        res = predict_pricing(Income, Ocean_Prox, Population, lg, Bed_per_room, lt)
        
        st.success("The Estimated Pricing is {}: " .format(res))
    
    
    else:
        st.success("Waiting for Prediction...")


if __name__=='__main__':
    main()