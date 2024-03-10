# import streamlit as st
# from st_pages import add_page_title
# #from algo.shs import call_back

# add_page_title()

# def save_data():
#     st.session_state["_weight"] = st.session_state["weight"]
#     new_weight = st.session_state['weight']
# def get_value(key):
#             st.session_state["weight"] = st.session_state[_weight]


# def app():
#     form_1 = {}
#     with st.form("basic_form"):
#         # Define UI elements and use them to update session_state
#         name = st.text_input("What is your Name?", value=st.session_state.get('name', ''))
#         occupation = st.selectbox(
#             "Pick your occupation",
#             [
#                 "Homebody (Housepersons/maids/Stay at home parents)",
#                 "Student",
#                 "Desk Worker (Any job including long duration of stationary sitting/standing)",
#                 "Field Worker (Any job that requires manual practice)",
#                 "Professional Athletes",
#                 "Retired Desk Worker",
#                 "Retired Field Worker",
#                 "Retired Athlete",
#             ],
#             index=st.session_state.get('occupation', 0)
#         )
#         duration_of_workday = st.selectbox(
#             "How much time you spend on work",
#             [
#                 "Light (Daily Average of up to 4 Hours)",
#                 "Moderate (Up to 8 Hours)",
#                 "Heavy (10+ Hours)",
#                 "Walking Zombie (12+ Hours)",
#             ],
#             index=st.session_state.get('duration_of_workday', 0)
#         )
#         gender = st.selectbox("Insert Your Gender", ["Male", "Female"], index=st.session_state.get('gender', 0))
#         pregnant = st.selectbox("Are You Pregnant", ["No", "Yes"], index=0 if st.session_state.get('pregnant', 'No') == 'No' else 1)
#         breastfeeding = st.selectbox("Are You Breastfeeding", ["No", "Yes"], index=0 if st.session_state.get('breastfeeding', 'No') == 'No' else 1)
#         # For the slider, just create it without manually setting session_state
#         st.session_state["weight"] = st.session_state["_weight"]


#         get_value("_weight")
#         current_weights = st.slider("What is your weight in KG", 40, 170, key='weight',on_change=save_data)


#         # No need to manually set session_state['weight'], Streamlit does it automatically
#         submit_button = st.form_submit_button("Submit")
#         # if st.session_state["FormSubmitter:basic_form-Submit"] == True:

#         #     for key in st.session_state:
#         #         form_1[key] = st.session_state[key]


#         return name, occupation, duration_of_workday, gender, pregnant, breastfeeding, current_weights


# name, occupation, duration_of_workday, gender, pregnant, breastfeeding, current_weights = app()
# #st.write["_weight"]

# import streamlit as st

# # Initialize '_weight' if not in session_state
# if "_weight" not in st.session_state:
#     st.session_state["_weight"] = 70  # Default weight

# def app():
#     with st.form("basic_form"):
#         # Other form elements...

#         # Use the slider without an on_change callback
#         current_weight = st.slider("What is your weight in KG", 40, 170, value=st.session_state.get("_weight", 70), key='weight')

#         submit_button = st.form_submit_button("Submit")
#         if submit_button:
#             # Perform actions after submission, e.g., saving the weight
#             st.session_state["_weight"] = st.session_state["weight"]
#             # Additional actions based on form input...

#         # Return values are not impacted by the removal of on_change
#         return current_weight

# current_weight = app()
# # Optionally display the current weight
# st.write(f"Your current weight is: {st.session_state.weight} kg")

import streamlit as st


# @st.cache_data
def wt():
    with st.form("Basic Information"):

        if ["name"] in st.session_state:
            current_name = session_state["name"]
        else:
            current_name = st.text_input("What is your Name?")
            st.session_state["name"] = current_name


        if ["age"] in st.session_state:
            current_age = session_state["age"]
        else:
            current_age = st.number_input("What is your Age?",5,90)
            st.session_state["age"] = current_age

        if ["weight"] in st.session_state:
            current_weight = st.session_state["weight"]

        else:
            current_weight = st.slider("What is your weight in KG", 40, 170, value=70)
            st.session_state["weight"] = current_weight

        if ["height"] in st.session_state:
            current_height = st.session_state["height"]

        else:
            current_height = st.slider("What is your height in CM", 147, 191, value=130)
            st.session_state["height"] = current_height

        if ["occupation"] in st.session_state:
            current_occupation = st.session_state["occupation"]

        else:
            current_occupation = st.selectbox("Pick your Occupdation", ["Housepersons","Student","Desk Worker","Field Worker","Professional Athletes","Retired Desk Worker","Retired Field Worker","Retired Athletesr"])
            st.session_state["occupation"] = current_occupation

        if ["duration_of_workday"] in st.session_state:
            current_duration_of_workday = st.session_state["duration_of_workday"]

        else:
            current_duration_of_workday = st.selectbox("Pick your Occupdation", ["Light 4 hours","Moderate 8 Hours","Heavy 10+ Hours","Walking Zombie 12+"])
            st.session_state["duration_of_workday"] = current_duration_of_workday



        # if "duration_of_workday" in st.session_state:
        #     current_duration_of_workday = st.session_state["duration_of_workday"]

        # else:

        #     current_duration_of_workday = st.selectbox("How much time you spend on work",["Light 4 hours","Moderate 8 Hours","Heavy 10+ Hours","Walking Zombie 12+"])
        #     st.session_state["duration_of_workday"] = current_duration_of_workday

        if ["gender"] in st.session_state:
            current_gender = session_state["gender"]
        else:
            current_gender = st.selectbox("Insert Your Gender", ["Male", "Female"])
            st.session_state["gender"] = current_gender

        if ["pregnant"] in st.session_state:
            current_pregnant = session_state["pregnant"]
        else:
            current_pregnant = st.selectbox("Are You Pregnant", ["No", "Yes"])
            st.session_state["pregnant"] = current_pregnant

    
        if ["breastfeeding"] in st.session_state:
            current_breastfeeding = session_state["breastfeeding"]
        else:
            current_breastfeeding = st.selectbox("Are You Breastfeeding", ["No", "Yes"])
            st.session_state["breastfeeding"] = current_breastfeeding

        st.form_submit_button("Submit To BankaiFit")

    # if ["heigh"] in st.session_state:

   # st.write(st.session_state.weight)


wt()
