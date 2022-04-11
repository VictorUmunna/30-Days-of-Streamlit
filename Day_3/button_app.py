import streamlit as st

st.title('Button App')

st.header('st.button')

if st.button('Say Hello'):
    st.write('Why hello there :smile:' )
else:
    st.write('Goodbye :wave:')