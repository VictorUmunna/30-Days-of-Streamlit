import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

st.write('Hello, *World!* :smile:')

st.write(1234)

data = pd.DataFrame({
    'first': ['John', 'Mary', 'Paul', 'Jane'],
    'last': ['Doe', 'Smith', 'Johnson', 'Doe'],
    'age': [25, 26, 27, 25]
    })

st.write(data)

st.write('Below is a dataframe with a table', data, 
            'And a chart', alt.Chart(data).mark_bar().encode(x='first', y='age'))

data2 = pd.DataFrame(
    np.random.randn(200,3),
    columns = ['a', 'b', 'c'])
c = alt.Chart(data2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)