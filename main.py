import pandas as pd
import streamlit as st


st.title("Once upon a time")

uploaded_file = st.file_uploader("https://github.com/mel291295/onceuponatime/blob/main/fairytales.xlsx")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(dataframe)
