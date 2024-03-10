import streamlit as st
from st_pages import add_page_title

add_page_title()

def app():
    with st.form("Life style Condition"):

        # For the level of physical activity
        if ["current_lifeStyle"] in st.session_state:
            current_lifeStyle = st.session_state["current_lifeStyle"]
        else:
            current_lifeStyle = st.selectbox(
                "What is the level of your physical Activity",
                [
                    "No Physical Activity",
                    "Minimal Activity (<2 hours per week)",
                    "Moderately Active (4 - 5 hours per week)",
                    "Very Active (5+ hours per week)",
                    "Extra Active",
                ],
                key='current_lifeStyle'  # Unique key for widget
            )
            st.session_state["current_lifeStyle"] = current_lifeStyle

        # For current fitness level
        if ["Current_Fitness_Level"] in st.session_state:
            Current_Fitness_Level = st.session_state["Current_Fitness_Level"]
        else:
            Current_Fitness_Level = st.selectbox(
                "Chose the best option that suggest your current fitness Level",
                [
                    "Never Worked Out",
                    "Actively working out under supervision",
                    "Actively work out without supervision",
                    "Used to work out under supervision",
                    "Used to work out without supervision",
                ],
                key='Current_Fitness_Level'  # Unique key for widget
            )
            st.session_state["Current_Fitness_Level"] = Current_Fitness_Level

        # For smoker status
        if ["smoker"] in st.session_state:
            smoker = st.session_state["smoker"]
        else:
            smoker = st.selectbox("Are you a smoker", ["No", "Yes"], key='smoker')  # Unique key for widget
            st.session_state["smoker"] = smoker

        # For alcohol consumption
        if ["alcohol"] in st.session_state:
            alcohol = st.session_state["alcohol"]
        else:
            alcohol = st.selectbox(
                "How much alcohol do you consume",
                [
                    "Teetotaler",
                    "Occasional Drinker (Less than 2 drinks a week)",
                    "Moderate Consumer (Up to 5 drinks a week)",
                    "Heavy Drinker (5+ drinks weekly)",
                ],
                key='alcohol'  # Unique key for widget
            )
            st.session_state["alcohol"] = alcohol

        # For willingness to incorporate exercise
        if ["otie"] in st.session_state:
            otie = st.session_state["otie"]
        else:
            otie = st.selectbox(
                "Are you Ready to Incorporate Exercise in your Daily routine", ["Yes", "No"], key='otie'  # Unique key for widget
            )
            st.session_state["otie"] = otie

        # For health supplements intake
        if ["supply"] in st.session_state:
            supply = st.session_state["supply"]
        else:
            supply = st.selectbox("Do you take any health supplements", ["Yes", "No"], key='supply')  # Unique key for widget
            st.session_state["supply"] = supply








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