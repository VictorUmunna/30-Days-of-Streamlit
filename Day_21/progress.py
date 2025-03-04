import streamlit as st
import time

st.title('st.progress')

with st.expander('About this app'):
    st.write('You can now display the progress of your calculations in a Streamlit app using the st.progress() function.')

my_bar = st.progress(0)

while True:
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
    st.balloons()
    
