import streamlit as st
from st_pages import add_page_title
from algo.shs import new_weight

add_page_title()

def app():

    st.write(

        st.session_state.get('current_weights',25) * 2
    )

 
app()