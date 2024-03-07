import streamlit as st
from st_pages import add_page_title
import algo.shs as alsh

add_page_title()

def app():

    st.write(

        "The weight is"
    )
    print(alsh.printa_data())


 
app()