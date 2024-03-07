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
    water_intake = st.number_input("How many Liters of Water you drink in a day", 1, 6)
    daily_calories = st.slider(
        "What is your daily Cal Consumption (best guess)", 500, 5000, value=3500
    )
    dails_carbs = st.slider(
        "What % of your total calories from Carb consumption (best guess)",
        0,
        100,
        value=70,
    )
    dails_fat = st.slider(
        "What % of your total calories from Fat consumption (best guess)",
        0,
        100,
        value=15,
    )
    dails_protein = st.slider(
        "What % of your total calories from Protein consumption (best guess)",
        0,
        100,
        value=15,
    )
    allergens = st.multiselect(
        "Choose the food item or items to which you are allergic",
        ["None", "Milk", "Egg", "Fish", "Shellfish", "Peanuts", "Wheat", "Soy"],
    )
    diet_observation = st.multiselect(
        "Choose the item or items that align with your dietary Observation ",
        [
            "None",
            "Primarily Carbs",
            "High Sugar Consumption",
            "Lack of Protein",
            "Erratic Meal Times",
            "Insufficient Balance of Macros",
            "Balanced Meals",
            "Unnecessary supplements",
            "High Fat Intake",
        ],
    )
    return diet_style,cnom,cnom_detail,first_major_meal,ci,water_intake,daily_calories,dails_carbs,dails_fat,dails_protein,allergens,diet_observation


app()
