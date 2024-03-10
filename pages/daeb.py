import streamlit as st
from st_pages import add_page_title

add_page_title()


def app():
    with st.form("DAEB"):
        if ["diet_style"] in st.session_state:
            current_diet_style = st.session_state["diet_style"]
        else:
            current_diet_style = st.selectbox(
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
            st.session_state["diet_style"] = current_diet_style

        if ["cnom"] in st.session_state:
            current_cnom = st.session_state["cnom"]
        else:
            current_cnom = st.number_input("How many meals you eat per day", min_value=1, max_value=6)
            st.session_state["cnom"] =current_cnom

        if ["cnom_detail"] in st.session_state:
            current_cnom_detail = st.session_state["cnom_detail"]
        else:
            current_cnom_detail = st.text_input("What are these meals", max_chars=130, help="breakfast")
            st.session_state["cnom_detail"] = current_cnom_detail

        if ["first_major_meal"] in st.session_state:
            current_first_major_meal = st.session_state["first_major_meal"]
        else:
            current_first_major_meal = st.selectbox("What is your first major meal of the Day",["Breakfast","Morning Snack","Brunch","Lunch","Afternoon Snack","Evening Snack","Dinner"])
            st.session_state["first_major_meal"] = current_first_major_meal

        if ["ci"] in st.session_state:
            current_ci = st.session_state["ci"]
        else:
            current_ci = st.number_input("How Many Cups of Coffee you drink per day", min_value=0, max_value=10)
            st.session_state["ci"] = current_ci

        if ["water_intake"] in st.session_state:
            current_water_intake = st.session_state["water_intake"]
        else:
            current_water_intake = st.number_input("How many Liters of Water you drink in a day", min_value=1, max_value=6)
            st.session_state["water_intake"] = current_water_intake
            
        if ["daily_calories"] in st.session_state:
            current_daily_calories = st.session_state["daily_calories"]
        else:
            current_daily_calories = st.slider("What is your daily Cal Consumption (best guess)", 500, 5000, value=3500)
            st.session_state["daily_calories"] = current_daily_calories
                
        if ["dails_carbs"] in st.session_state:
            current_dails_carbs = st.session_state["dails_carbs"]
        else:
            current_dails_carbs = st.slider("What % of your total calories from Carb consumption (best guess)", 0, 100, value=70)
            st.session_state["dails_carbs"] = current_dails_carbs
        
        if ["dails_fat"] in st.session_state:
            current_dails_fat = st.session_state["dails_fat"]
        else:
            current_dails_fat = st.slider("What % of your total calories from Fat consumption (best guess)",0,100,value=15)
            st.session_state["dails_fat"] = current_dails_fat

        if ["dails_protein"] in st.session_state:
            current_dails_protein = st.session_state["dails_protein"]
        else:
            current_dails_protein = st.slider("What % of your total calories from Protein consumption (best guess)",0,100,value=15)
            st.session_state["dails_protein"] = current_dails_protein

        
        if ["allergens"] in st.session_state:
            current_allergens = st.session_state["allergens"]
        else:
            current_allergens = st.multiselect("Choose the food item or items to which you are allergic",["None", "Milk", "Egg", "Fish", "Shellfish", "Peanuts", "Wheat", "Soy"])
            st.session_state["allergens"] = current_allergens
            
        if ["diet_observation"] in st.session_state:
            current_diet_observation = st.session_state["diet_observation"]
        else:
            current_diet_observation = st.multiselect("Choose the item or items that align with your dietary Observation ",["None","Primarily Carbs","High Sugar Consumption","Lack of Protein","Erratic Meal Times","Insufficient Balance of Macros","Balanced Meals","Unnecessary supplements","High Fat Intake",],)
            st.session_state["diet_observation"] = current_diet_observation

        if ["diet_observation_values"] in st.session_state:
            current_diet_observation_values = st.session_state["diet_observation_values"]
        else:
            if current_diet_observation == "None":
                current_diet_observation_value = 1
            elif current_diet_observation == "Primarily Carbs":
                current_diet_observation_value = 2
            elif current_diet_observation == "High Sugar Consumption":
                current_diet_observation_value = 3
            elif current_diet_observation == "Lack of Protein":
                current_diet_observation_value = 4
            elif current_diet_observation == "Erratic Meal Times":
                current_diet_observation_value = 5
            elif current_diet_observation == "Insufficient Balance of Macros":
                current_diet_observation_value = 6
            elif current_diet_observation == "Balanced Meals":
                current_diet_observation_value = 7
            elif current_diet_observation == "Unnecessary supplements":
                current_diet_observation_value = 8
            elif current_diet_observation == "High Fat Intake":
                current_diet_observation_value = 9

            st.session_state["diet_observation_values"] = current_diet_observation_value

            





# Repeat for dails_fat and dails_protein with their respective values and text.




        # daily_calories = st.slider(
        #     "What is your daily Cal Consumption (best guess)", 500, 5000, value=3500
        # )
        # dails_carbs = st.slider(
        #     "What % of your total calories from Carb consumption (best guess)",
        #     0,
        #     100,
        #     value=70,
        # )
        # dails_fat = st.slider(
        #     "What % of your total calories from Fat consumption (best guess)",
        #     0,
        #     100,
        #     value=15,
        # )
        # dails_protein = st.slider(
        #     "What % of your total calories from Protein consumption (best guess)",
        #     0,
        #     100,
        #     value=15,
        # )
        # allergens = st.multiselect(
        #     "Choose the food item or items to which you are allergic",
        #     ["None", "Milk", "Egg", "Fish", "Shellfish", "Peanuts", "Wheat", "Soy"],
        # )
        # diet_observation = st.multiselect(
        #     "Choose the item or items that align with your dietary Observation ",
        #     [
        #         "None",
        #         "Primarily Carbs",
        #         "High Sugar Consumption",
        #         "Lack of Protein",
        #         "Erratic Meal Times",
        #         "Insufficient Balance of Macros",
        #         "Balanced Meals",
        #         "Unnecessary supplements",
        #         "High Fat Intake",
        #     ],
        # )
        st.form_submit_button("Submit To BankaiFit")


app()
