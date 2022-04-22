import streamlit as st

st.title('st.form')

#Full example using the with notation
st.header('1. Example of using the "with" notation')
st.subheader('Coffee machine order form')


with st.form('my form'):
    st.write('***Order your coffee***')

    #input widgets
    coffee_bean_val = st.selectbox('Coffee Bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee Roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    water_temp_val = st.selectbox('Water temperature', ['Hot', 'Cold'])
    serving_type_val = st.selectbox('Serving Format Type', ['Hot', 'Iced', 'Frappe'])
    serving_size_val = st.selectbox('Serving Size', ['Small', 'Medium', 'Large'])
    milk_val = st.selectbox('Milk', ['Skim', 'Soy', 'Almond', 'Oat', 'Coconut', 'Whole'])
    milk_intensity_val = st.selectbox('Milk Intensity', ['None', 'Light', 'Medium', 'Heavy'])
    owncup_val = st.checkbox('Bring own cup')
    extra_sugar_val = st.checkbox('Extra sugar')

    #every form mst have a submiit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
    ☕ You have ordered:
    - Coffee bean: `{coffee_bean_val}`
    - Coffee roast: `{coffee_roast_val}`
    - Brewing method: `{brewing_val}`
    - Water temperature: `{water_temp_val}`
    - Serving type: `{serving_type_val}`
    - Serving size: `{serving_size_val}`
    - Milk: `{milk_val}`
    - Milk intensity: `{milk_intensity_val}`
    - Own cup: `{owncup_val}`
    - Extra sugar: `{extra_sugar_val}`
    ''')
else:
    st.write('☝️ Place your order!')


# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)