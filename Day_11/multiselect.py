import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
    'What are your favourite fotball teams?',
    ['Manchester United', 'Chelsea', 'Manchester City', 'Arsenal', 'Liverpool'],
    ['Chelsea', 'Manchester City'])

st.write('You selected:', options)