import streamlit as st
from st_pages import add_page_title
from algo.shs import new_weigh
add_page_title()

def app():

    st.write(

        new_weigh 
        )
    option = ste.selectbox("How would you like to be contacted?", range(100),key="selectbox")

    st.write("You selected:", option)

 
app()