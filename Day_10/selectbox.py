import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
    'Who is your favourite superhero?',
    ('Ironman', 'Hulk', 'Thor', 'Captain America', 'Spiderman',
     'Black Panther', 'Black Widow', 'Ant')
)
st.write('Your favourite superhero is:', option)