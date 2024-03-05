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
        return name, occupation
