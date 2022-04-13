import streamlit as st

st.header('st.checkbox')

st.write ('What would you like to order?')

boli = st.checkbox('Boli')
guguru = st.checkbox('Guguru')
nsala = st.checkbox('Nsala')

if boli:
    st.write('Great! Here is your Boli')

if guguru:
    st.write("Okay! Here's some Guguru")

if nsala:
    st.write("Enjoy your Nsala")