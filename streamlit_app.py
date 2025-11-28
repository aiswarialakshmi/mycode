import streamlit as st
import pandas as pd
import numpy as np

st.title('My First Streamlit App')

st.header('Random Number Generator')

if st.button('Generate Random Number'):
    random_number = np.random.randint(1, 101)
    st.write(f'Random Number: {random_number}')

st.header('Sample Data Chart')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.text_input("Your name", key="name")

if st.session_state.name:
    st.write(f"Hello, {st.session_state.name}!")
