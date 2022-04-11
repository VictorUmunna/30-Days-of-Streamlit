import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 99, 15)
st.write("I'.m ", age, " years old")

# Example 2

st.subheader('Range slider')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Example 3

st.subheader('Range time slider')

appointment = st.slider(
    'Schedule your appointment?',
    value = (time(12,0), time(14, 30)))
st.write('You are scheduled for:', appointment) 

# Example 4

st.subheader('Datetime slider')

start_time = st.slider(
    "When do you want to start?",
    value = datetime(2020, 1, 1, 12, 30),
    format = "MM/DD/YYYY hh:mm")
st.write("Start time:", start_time)