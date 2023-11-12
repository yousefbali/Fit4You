import streamlit as st
import pandas as pd
import pymongo
import requests
from streamlit_lottie import st_lottie

# Streamlit app
st.set_page_config(page_title="", page_icon=":tada:", layout="wide")
st.markdown('<h1 style="font-size: 50px;">Airo Auto</h1>', unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/19a10b2d-6de7-4a05-9c7a-bfe7ccfbad3e/v3V4DjqTTE.json")

st_lottie(lottie_coding, height=300, key="cargif")


st.markdown("<h1 style='text-align: center; color: white;'>Comparison of Automobile Aerodynamics</h1>", unsafe_allow_html=True)

# Load CSV data
csv_file_path = 'table_data.csv'  # Replace with the path to your CSV file
csv_data = pd.read_csv(csv_file_path)

# Helper function to display data based on selections
def display_data(data, Make, Model, Year, column):
    records = data[(data['Make'] == Make) & (data['Model'] == Model) & (data['Year'] == Year)]
    column.write(records)

def get_cda_value(data, Make, Model, Year):
    record = data[(data['Make'] == Make) & (data['Model'] == Model) & (data['Year'] == Year)]
    return float(record['CdA'].values[0]) if not record.empty else None

# Create columns
col1, col2 = st.columns(2)

# First column selections
with col1:
    st.write("Vehicle 1:")
    Make1 = st.selectbox('Select a Make:', csv_data['Make'].unique())
    Model1 = st.selectbox('Select a Model:', csv_data[csv_data['Make'] == Make1]['Model'].unique())
    Year1 = st.selectbox('Select a Year:', csv_data[(csv_data['Make'] == Make1) & (csv_data['Model'] == Model1)]['Year'].unique())
    if st.button('Show Data 1'):
        display_data(csv_data, Make1, Model1, Year1, col1)

# Second column selections
with col2:
    st.write("Vehicle 2:")
    Make2 = st.selectbox('Select a Make: ', csv_data['Make'].unique())
    Model2= st.selectbox('Select a Model: ', csv_data[csv_data['Make'] == Make2]['Model'].unique())
    Year2 = st.selectbox('Select a Year: ', csv_data[(csv_data['Make'] == Make2) & (csv_data['Model'] == Model2)]['Year'].unique())
    if st.button('Show Data 2'):
        display_data(csv_data, Make2, Model2, Year2, col2)
