import streamlit as st
import basic
import lifestyleInformation

PAGES = {"Basic Information": basic, "Life Style Information": lifestyleInformation}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]

page.app()
