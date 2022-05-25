import pandas as pd
import streamlit as st


st.title("Once upon a time")

import os
from gtts import gTTS
from googletrans import Translator
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import jieba
from xpinyin import Pinyin

try:
    os.mkdir("temp_folder")
except:
    pass

#Add a logo (optional) in the sidebar
logo = Image.open(r'"C:\Users\ASUS\Desktop\Project LAB\Multilingual2x.webp"')
st.sidebar.image(logo,  width=120)

#Add the expander to provide some basic information about the app
st.sidebar.markdown("### My Little Language learning App")
with st.sidebar.expander("About the App"):
     st.write("""
        This language learning App is built by Sharone Li using Streamlit. Check out her medium article for more details about the app and source code.
     """)
st.sidebar.markdown("You can build your own language learning app using streamlit and Google Translate API. \n\n I only showed a few languages in this app, but you can certainly expand to other languages as well. Have fun!")

