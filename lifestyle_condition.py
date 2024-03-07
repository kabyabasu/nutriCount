import streamlit as st
from st_pages import add_page_title

add_page_title()


def app():
    mc = st.multiselect(
        "Do you have any of these medical Condition",
        [
            "None",
            "HyperTension",
            "High Pressure",
            "Low Pressure",
            "Heart Disease",
            "Diabetes",
            "Obesity",
            "Malnourishment",
            "Migraines",
            "Thyroid",
            "PCOS",
            "Insomnia",
        ],
        default="None",
    )
    mc_add = st.text_input("If you have any medical condtion that is not mentioned above please give details",max_chars=130,disabled=False,placeholder="None")

app()