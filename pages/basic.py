import streamlit as st
from st_pages import add_page_title

add_page_title()

def app():
    import streamlit as st

def app():
    # Initialize session_state for all variables if not already done
    if 'name' not in st.session_state:
        st.session_state['name'] = ""
    if 'occupation' not in st.session_state:
        st.session_state['occupation'] = ""
    if 'duration_of_workday' not in st.session_state:
        st.session_state['duration_of_workday'] = ""
    if 'gender' not in st.session_state:
        st.session_state['gender'] = ""
    if 'pregnant' not in st.session_state:
        st.session_state['pregnant'] = "No"
    if 'breastfeeding' not in st.session_state:
        st.session_state['breastfeeding'] = "No"
    if 'weight' not in st.session_state:
        st.session_state['weight'] = 70  # Assuming a default value

    # Define UI elements and bind them to session_state
    st.session_state['name'] = st.text_input("What is your Name?", value=st.session_state['name'])
    st.session_state['occupation'] = st.selectbox(
        "Pick your occupation",
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
        index=0 if st.session_state['occupation'] == "" else None,  # Keep selection if already made
    )
    st.session_state['duration_of_workday'] = st.selectbox(
        "How much time you spend on work",
        [
            "Light (Daily Average of up to 4 Hours)",
            "Moderate (Up to 8 Hours)",
            "Heavy (10+ Hours)",
            "Walking Zombie (12+ Hours)",
        ],
        index=0 if st.session_state['duration_of_workday'] == "" else None,
    )
    st.session_state['gender'] = st.selectbox("Insert Your Gender", ["Male", "Female"], index=0 if st.session_state['gender'] == "" else None)
    st.session_state['pregnant'] = st.selectbox("Are You Pregnant", ["No", "Yes"], index=0 if st.session_state['pregnant'] == "No" else 1)
    st.session_state['breastfeeding'] = st.selectbox("Are You Breastfeeding", ["No", "Yes"], index=0 if st.session_state['breastfeeding'] == "No" else 1)
    st.session_state['weight'] = st.slider("What is your weight in KG", 40, 170, key='weight')

    # Directly use the session_state values
    name = st.session_state['name']
    occupation = st.session_state['occupation']
    duration_of_workday = st.session_state['duration_of_workday']
    gender = st.session_state['gender']
    pregnant = st.session_state['pregnant']
    breastfeeding = st.session_state['breastfeeding']
    current_weights = st.session_state['weight']

    return name, occupation, duration_of_workday, gender, pregnant, breastfeeding, current_weights

name, occupation, duration_of_workday, gender, pregnant, breastfeeding, current_weights = app()

st.write(current_weights)