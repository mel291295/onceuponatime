import pandas as pd
import streamlit as st


st.title("Once upon a time")


uploaded_file = st.file_uploader(“"C:\Users\ASUS\Documents\fairytales.xlsx"”)
if uploaded_file is not None:
#read csv
df1=pd.read_csv(uploaded_file)
