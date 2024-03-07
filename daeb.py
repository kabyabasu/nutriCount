import streamlit as st
from st_pages import add_page_title

add_page_title()


def app():
    diet_style = st.selectbox(
        "What is your Diet Style",
        [
            "Vegan",
            "Eggetarian",
            "Vegetarian",
            "Piscetarian",
            "Non Vegetarian",
            "Keto",
            "Gluten Free",
        ],
    )
    cnom = st.number_input("How many meals you eat per day",min_value=1,max_value=4)
    cnom_detail = st.text_input("What are these meals",max_chars=130,help="breakfast")

app()
