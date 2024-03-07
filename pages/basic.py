import streamlit as st
from st_pages import add_page_title

add_page_title()

def app():
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
    if 'weight' not in st.session_state:
        st.session_state['weight'] = 70
    current_weights = st.slider("What is your weight n KG", 40, 170,key="weight")
    return name,occupation,Duration_of_WorkDay,gender,pregnent,breastfeed,current_weights

name,occupation,Duration_of_WorkDay,gender,pregnent,breastfeed,current_weights = app()
st.write(current_weights)