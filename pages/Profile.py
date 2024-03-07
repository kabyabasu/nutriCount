import streamlit as st
from st_pages import add_page_title

add_page_title()

def app():

    Test = st.selectbox(
        "Are you Ready to Incorporate Exercise in your Daily routine", ["Yes", "No"]
    )
 
