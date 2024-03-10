import streamlit as st
from st_pages import add_page_title

add_page_title()

def app():
    with st.form("Life style Condition"):

        # For the level of physical activity
        if ["lifeStyle"] in st.session_state:
            current_lifeStyle = st.session_state["lifeStyle"]
        else:
            current_lifeStyle = st.selectbox(
                "What is the level of your physical Activity",
                [
                    "No Physical Activity",
                    "Minimal Activity (<2 hours per week)",
                    "Moderately Active (4 - 5 hours per week)",
                    "Very Active (5+ hours per week)",
                    "Extra Active",
                ], # Unique key for widget
            )
            st.session_state["lifeStyle"] = current_lifeStyle

        # For current fitness level
        if ["Fitness_Level"] in st.session_state:
            Current_Fitness_Level = st.session_state["Fitness_Level"]
        else:
            Current_Fitness_Level = st.selectbox(
                "Chose the best option that suggest your current fitness Level",
                [
                    "Never Worked Out",
                    "Actively working out under supervision",
                    "Actively work out without supervision",
                    "Used to work out under supervision",
                    "Used to work out without supervision",
                ], # Unique key for widget
            )
            st.session_state["Fitness_Level"] = Current_Fitness_Level

        # For smoker status
        if ["smoker"] in st.session_state:
            current_smoker = st.session_state["smoker"]
        else:
            current_smoker = st.selectbox("Are you a smoker", ["No", "Yes"])  # Unique key for widget
            st.session_state["smoker"] = current_smoker

        # For alcohol consumption
        if ["alcohol"] in st.session_state:
            current_alcohol = st.session_state["alcohol"]
        else:
            current_alcohol = st.selectbox(
                "How much alcohol do you consume",
                [
                    "Teetotaler",
                    "Occasional Drinker (Less than 2 drinks a week)",
                    "Moderate Consumer (Up to 5 drinks a week)",
                    "Heavy Drinker (5+ drinks weekly)",
                ]  # Unique key for widget
            )
            st.session_state["alcohol"] = current_alcohol

        # For willingness to incorporate exercise
        if ["otie"] in st.session_state:
            current_otie = st.session_state["otie"]
        else:
            current_otie = st.selectbox(
                "Are you Ready to Incorporate Exercise in your Daily routine", ["Yes", "No"] # Unique key for widget
            )
            st.session_state["otie"] = current_otie

        # For health supplements intake
        if ["supply"] in st.session_state:
            current_supply = st.session_state["supply"]
        else:
            current_supply = st.selectbox("Do you take any health supplements", ["Yes", "No"])  # Unique key for widget
            st.session_state["supply"] = current_supply








        st.form_submit_button("Submit To BankaiFit")

    # current_lifeStyle = st.selectbox(
    #     "What is the level of your physical Activity",
    #     [
    #         "No Physical Activity",
    #         "Minimal Activity (<2 hours per week)",
    #         "Moderately Active (4 - 5 hours per week)",
    #         "Very Active (5+ hours per week)",
    #         "Extra Active",
    #     ],
    # )
    # Current_Fitness_Level = st.selectbox(
    #     "Chose the best option that suggest your current fitness Level",
    #     [
    #         "Never Worked Out",
    #         "Actively working out under supervision",
    #         "Actively work out without supervision",
    #         "Used to work out under supervision",
    #         "Used to work out without supervision",
    #     ],
    # )
    # smoker = st.selectbox("Are you a smoker", ["No", "Yes"])
    # alcohol = st.selectbox(
    #     "How much alcohol do you consume",
    #     [
    #         "Teetotaler",
    #         "Occasional Drinker (Less than 2 drinks a week)",
    #         "Moderate Consumer (Up to 5 drinks a week)",
    #         "Heavy Drinker (5+ drinks weekly)",
    #     ],
    # )
    # otie = st.selectbox(
    #     "Are you Ready to Incorporate Exercise in your Daily routine", ["Yes", "No"]
    # )
    # supply = st.selectbox("Do you take any health supplements", ["Yes", "No"])


app()