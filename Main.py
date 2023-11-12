import streamlit as st
import pandas as pd
import requests

# Streamlit app
st.set_page_config(page_title="", page_icon=":tada:", layout="wide")
st.markdown('<h1 style="font-size: 50px;">Airo Auto</h1>', unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()




st.markdown("<h1 style='text-align: center; color: white;'>Comparison of Automobile Aerodynamics</h1>", unsafe_allow_html=True)



# Helper function to display data based on selections
def display_data(data, Make, Model, Year, column):
    records = data[(data['Make'] == Make) & (data['Model'] == Model) & (data['Year'] == Year)]
    column.write(records)

def get_cda_value(data, Make, Model, Year):
    record = data[(data['Make'] == Make) & (data['Model'] == Model) & (data['Year'] == Year)]
    return float(record['CdA'].values[0]) if not record.empty else None

# Create columns
col1, col2 = st.columns(2)
