import streamlit as st


class basicInfo:
    def __init__(self):
        pass

    def intro():
        name = st.text_input("What is you Name")
        occupation = st.selectbox(
            "Pick you occupation",
            [
                "Homebody (Housepersons/maids/Stay at home parents)",
                "Student",
                "Desk Worker (Any job including long duration of stationary sitting/standing)",
                "Field Worker (Any job that requires manual practice)",
                "Professional Athletes",
                "Retired Desk Worker",
                "Retired Field Worker",
                "Retired Athlete",
            ],
        )

        Duration_of_WorkDay = st.selectbox(
            "How much time you spend on work",
            [
                "Light (Daily Average of upto 4 Hours)",
                "Moderate (Upto 8 Hours)",
                "Heavy (10+ Hours)",
                "Walking Zombie (12+ Hours)",
            ],
        )
        gender = st.selectbox("Insert Your Gender", ["Male", "Female"])
        pregnent = st.selectbox("Are You Pregnent", ["No", "Yes"])
        breastfeed = st.selectbox("Are You breast Fedding", ["No", "Yes"])
        current_weights = st.slider("What is your weight n KG", 40, 170)
        return name, occupation, gender
