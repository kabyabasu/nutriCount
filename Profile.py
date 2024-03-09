import streamlit as st
from st_pages import add_page_title
import streamlit-extras as ste

add_page_title()

def app():

    Test = st.selectbox(
        "Are you Ready to Incorporate Exercise in your Daily routine", ["Yes", "No"]
    ),
    option = ste.selectbox("How would you like to be contacted?", range(100),key="selectbox")

    st.write("You selected:", option)


app()
 
