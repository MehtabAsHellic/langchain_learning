import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = apikey

st.title("🦜🔗 EngineeringGPT")
prompt = st.text_input("plug in your prompt here !")

llm = OpenAI(temperature=0.9)

if prompt:
    respone = llm(prompt)
    st.write(respone)
