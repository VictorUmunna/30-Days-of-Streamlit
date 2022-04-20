import streamlit as st

st.set_page_config(layout='wide')

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
    st.write('This app shows some details about you')
    st.image('https://i.ytimg.com/vi/v56aN7ivjjc/maxresdefault.jpg', width=250)

st.sidebar.header('Your details')
user_name = st.sidebar.text_input('What is your name')
user_country = st.sidebar.selectbox('Where are you from?', ('Nigeria', 'USA', 'Canada', 'Mexico', 'Brazil', 'United Kingdom', 'Germany', 'India', 'Austrailia', 'China', 'South Africa'))
user_age = st.sidebar.slider('How old are you?', min_value=18, max_value=100, value=30)
user_emoji = st.sidebar.selectbox('What is your favourite emoji?', ('', '🤓', '😎', '🤩', '😍', '🤑', '😘', '😍', '😍', '😍', '😍', '😍'))
user_food = st.sidebar.selectbox('What is your favourite food?', ('', 'Jollof Rice', 'Pizza', 'Burger', 'Fries', 'Noodles', 'Sushi', 'Steak', 'Chicken', 'Fish', 'Pasta', 'Soup', 'Cake'))

st.header('Output')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if user_name != '':
        st.write(f'👋 Hello {user_name}!')
    else:
        st.write('👈  Please enter your **name**!')

with col2:
    if user_country != '':
        st.write(f'🗺 You are from {user_country}')
    else:
        st.write('👈 Please enter your **country**!')

with col3:
    if user_age != '':
        st.write(f'🎂 You are {user_age} years old')
    else:
        st.write('👈 Please enter your **age**!')

with col4:
    if user_emoji != '':
        st.write(f'{user_emoji} is your favorite **emoji**!')
    else:
        st.write('👈 Please choose an **emoji**!')


with col5:
    if user_food != '':
        st.write(f'🍽 Your favorite food is {user_food}')
    else:
        st.write('👈 Please choose your favourite **food**!')


