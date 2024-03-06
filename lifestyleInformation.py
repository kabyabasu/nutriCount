import streamlit as st


def app():
    current_lifeStyle = st.selectbox(
        "What is the level of your physical Activity",
        [
            "No Physical Activity",
            "Minimal Activity (<2 hours per week)",
            "Moderately Active (4 - 5 hours per week)",
            "Very Active (5+ hours per week)",
            "Extra Active",
        ],
    )
    Current_Fitness_Level = st.selectbox(
        "Chose the best option that suggest your current fitness Level",
        [
            "Never Worked Out",
            "Actively working out under supervision",
            "Actively work out without supervision",
            "Used to work out under supervision",
            "Used to work out without supervision",
        ],
    )
    smoker = st.selectbox("Are you a smoker", ["No", "Yes"])
    alcohol = st.selectbox(
        "How much alcohol do you consume",
        [
            "Teetotaler",
            "Occasional Drinker (Less than 2 drinks a week)",
            "Moderate Consumer (Up to 5 drinks a week)",
            "Heavy Drinker (5+ drinks weekly)",
        ],
    )
    otie = st.selectbox(
        "Are you Ready to Incorporate Exercise in your Daily routine", ["Yes", "No"]
    )
    supply = st.selectbox("Do you take any health supplements", ["Yes", "No"])
