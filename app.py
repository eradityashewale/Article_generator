import os
from apikey import apikey

import streamlit as st
from langchain.llms import openai

os.environ['OPENAI_API_KEY'] = apikey

st.title('Medium article generator')
topic = st.text_input('Enter your topic which want to explore')