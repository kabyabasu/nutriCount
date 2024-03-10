import streamlit as st
from st_pages import add_page_title

add_page_title()


def app():

    # g1 = st.selectbox(
    #     "What is your Primary Goal",
    #     [
    #         "Weight Loss",
    #         "Maintain Weight",
    #         "Weight Gain",
    #         "Muscle Gain",
    #         "Fat Loss",
    #         "Improve Sleep",
    #         "Sugar Control",
    #     ],
    # )
    # g2 = st.selectbox(
    #     "What is your Secondary Goal",
    #     [
    #         "Weight Loss",
    #         "Maintain Weight",
    #         "Weight Gain",
    #         "Muscle Gain",
    #         "Fat Loss",
    #         "Improve Sleep",
    #         "Sugar Control",
    #     ],
    # )

    # g3 = st.selectbox(
    #     "What is your Tertiary Goal",
    #     [
    #         "Weight Loss",
    #         "Maintain Weight",
    #         "Weight Gain",
    #         "Muscle Gain",
    #         "Fat Loss",
    #         "Improve Sleep",
    #         "Sugar Control",
    #     ],
    # )
    # return g1, g2, g3
    # For Primary Goal
    with st.form("Goal"):
        if ["g1"] in st.session_state:
            current_g1 = st.session_state["g1"]
        else:
            current_g1 = st.selectbox(
                "What is your Primary Goal",
                [
                    "Weight Loss",
                    "Maintain Weight",
                    "Weight Gain",
                    "Muscle Gain",
                    "Fat Loss",
                    "Improve Sleep",
                    "Sugar Control",
                ],
                key='g1'  # Ensure unique key for this widget
            )
            st.session_state["g1"] = current_g1

    # For Secondary Goal
        if ["g2"] in st.session_state:
            current_g2 = st.session_state["g2"]
        else:
            current_g2 = st.selectbox(
                "What is your Secondary Goal",
                [
                    "Weight Loss",
                    "Maintain Weight",
                    "Weight Gain",
                    "Muscle Gain",
                    "Fat Loss",
                    "Improve Sleep",
                    "Sugar Control",
                ],
                key='g2'  # Ensure unique key for this widget
            )
            st.session_state["g2"] = current_g2

    # For Tertiary Goal
        if ["g3"] in st.session_state:
            current_g3 = st.session_state["g3"]
        else:
            current_g3 = st.selectbox(
                "What is your Tertiary Goal",
                [
                    "Weight Loss",
                    "Maintain Weight",
                    "Weight Gain",
                    "Muscle Gain",
                    "Fat Loss",
                    "Improve Sleep",
                    "Sugar Control",
                ],
                key='g3'  # Ensure unique key for this widget
            )
            st.session_state["g3"] = current_g3
        
        st.form_submit_button("Submit To BankaiFit")



app()
