import streamlit as st
from st_pages import add_page_title

add_page_title()





def app():
    form_1 = {}
    with st.form("basic_form"):
        # Define UI elements and use them to update session_state
        name = st.text_input("What is your Name?", value=st.session_state.get('name', ''))
        occupation = st.selectbox(
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
            index=st.session_state.get('occupation', 0)
        )
        duration_of_workday = st.selectbox(
            "How much time you spend on work",
            [
                "Light (Daily Average of up to 4 Hours)",
                "Moderate (Up to 8 Hours)",
                "Heavy (10+ Hours)",
                "Walking Zombie (12+ Hours)",
            ],
            index=st.session_state.get('duration_of_workday', 0)
        )
        gender = st.selectbox("Insert Your Gender", ["Male", "Female"], index=st.session_state.get('gender', 0))
        pregnant = st.selectbox("Are You Pregnant", ["No", "Yes"], index=0 if st.session_state.get('pregnant', 'No') == 'No' else 1)
        breastfeeding = st.selectbox("Are You Breastfeeding", ["No", "Yes"], index=0 if st.session_state.get('breastfeeding', 'No') == 'No' else 1)
        # For the slider, just create it without manually setting session_state
        current_weights = st.slider("What is your weight in KG", 40, 170, key='weight')

        # No need to manually set session_state['weight'], Streamlit does it automatically
        submit_button = st.form_submit_button("Submit")
        if st.session_state["FormSubmitter:basic_form-Submit"] == True:

            for key in st.session_state:
                form_1[key] = st.session_state[key]


        return name, occupation, duration_of_workday, gender, pregnant, breastfeeding, current_weights,form_1


name, occupation, duration_of_workday, gender, pregnant, breastfeeding, current_weights,form_1 = app()
st.write(form_1["FormSubmitter:basic_form-Submit"])

