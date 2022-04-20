import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Upload CSV file')
file_upload = st.file_uploader('Upload a CSV file', type=['csv'])

if file_upload is not None:
    df = pd.read_csv(file_upload)
    st.header('DataFrame')
    st.write(df)
    st.subheader('Descriptive Statistics')
    st.write(df.describe())
    st.subheader('DataFrame Shape')
    st.write(df.shape)
else:
    st.info('☝️ Upload a CSV file')