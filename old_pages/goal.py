import streamlit as st
from st_pages import add_page_title

add_page_title()


def app():

    g1 = st.selectbox(
        "What is your Primary Goal",
        [
            "Weight Loss",
            "Maintain Weight",
            "Weight Gain",
            "Muscle Gain",
            "Fat Loss",
            "Improve Sleep",
            "Sugar Control",
        ],
    )
    g2 = st.selectbox(
        "What is your Secondary Goal",
        [
            "Weight Loss",
            "Maintain Weight",
            "Weight Gain",
            "Muscle Gain",
            "Fat Loss",
            "Improve Sleep",
            "Sugar Control",
        ],
    )

    g3 = st.selectbox(
        "What is your Tertiary Goal",
        [
            "Weight Loss",
            "Maintain Weight",
            "Weight Gain",
            "Muscle Gain",
            "Fat Loss",
            "Improve Sleep",
            "Sugar Control",
        ],
    )
    return g1, g2, g3


app()
