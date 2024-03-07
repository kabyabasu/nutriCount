import streamlit as st
from st_pages import add_page_title

add_page_title()


def app():
    pain = st.selectbox(
        "Do you have Pain in the body",
        [
            "Yes",
            "No",
        ],
    )

app()