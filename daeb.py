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
    cnom = st.number_input("How many meals you eat per day", min_value=1, max_value=6)
    cnom_detail = st.text_input("What are these meals", max_chars=130, help="breakfast")
    first_major_meal = st.selectbox(
        "What is your first major meal of the Day",
        [
            "Breakfast",
            "Morning Snack",
            "Brunch",
            "Lunch",
            "Afternoon Snack",
            "Evening Snack",
            "Dinner",
        ],
    )
    ci = st.number_input(
        "How Many Cups of Coffee you drink per day", min_value=0, max_value=10
    )
    water_intake = st.number_input(
        "How many Liters of Water you drink in a day", 0.5, 5.5
    )


app()
