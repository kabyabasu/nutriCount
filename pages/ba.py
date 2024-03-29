import streamlit as st
from st_pages import add_page_title
from streamlit_extras.switch_page_button import switch_page

add_page_title()


def app():
    with st.form("Body Assessment"):
        if ["pain"] in st.session_state:
            current_pain = st.session_state["pain"]
        else:

            current_pain = st.selectbox(
                "Do you have Pain in the body",
                [
                    "No",
                    "Yes",
                ],
            )
            st.session_state["pain"] = current_pain

        if ["pain_intensity"] in st.session_state:
            current_pain_intensity = st.session_state["pain_intensity"]
        else:
            current_pain_intensity = st.selectbox(
                "What is the intensity of Pain in the body",
                [
                    "No Pain",
                    "Mild (It doesn't bother me much but I feel it)",
                    "Moderate  (Feel it everday but I manage)",
                    "Severe (Daily activities are affected)",
                    "Life has no meaning (Need immediate relief)",
                ],
            )
            st.session_state["pain_intensity"] = current_pain_intensity

        if ["pain_location"] in st.session_state:
            current_pain_location = st.session_state["pain_location"]
        else:
            current_pain_location = st.multiselect(
                "Where do you have Pain in the body",
                [
                    "No Pain",
                    "Neck",
                    "Shoulder",
                    "Arm",
                    "Forearm",
                    "Elbow",
                    "Wrist + Hand",
                    "Upper Back",
                    "Lower Back",
                    "Hip & Thigh",
                    "Knee",
                    "Shin",
                    "Ankle",
                    "Foot",
                    "Chest",
                    "Groin",
                    "Stomach",
                ],
                default="No Pain",
            )
            st.session_state["pain_location"] = current_pain_location
        if ["tingling"] in st.session_state:
            current_tingling = st.session_state["tingling"]
        else:
            current_tingling = st.selectbox(
                "Do you have Tingling or Numbness in the body",
                [
                    "No",
                    "Yes",
                ],
            )
            st.session_state["tingling"] = current_tingling

        if ["tingling_intensity"] in st.session_state:
            current_tingling_intensity = st.session_state["tingling_intensity"]

        else:

            current_tingling_intensity = (
                st.selectbox(
                    "What is the intensity of Tingling or Numbness in the body",
                    [
                        "No Tingling or Numbness",
                        "Mild (It doesn't bother me much but I feel it)",
                        "Moderate  (Feel it everday but I manage)",
                        "Severe (Daily activities are affected)",
                        "Life has no meaning (Need immediate relief)",
                    ],
                ),
            )
            st.session_state["tingling_intensity"] = current_tingling_intensity

        if ["tingling_location"] in st.session_state:
            current_tingling_location = st.session_state["tingling_location"]

        else:
            current_tingling_location = st.multiselect(
                "Where do you have Tingling or Numbness in the body",
                [
                    "No Tingling or Numbness",
                    "Neck",
                    "Shoulder",
                    "Arm",
                    "Forearm",
                    "Elbow",
                    "Wrist + Hand",
                    "Upper Back",
                    "Lower Back",
                    "Hip & Thigh",
                    "Knee",
                    "Shin",
                    "Ankle",
                    "Foot",
                    "Chest",
                    "Groin",
                    "Stomach",
                ],
                default="No Tingling or Numbness",
            )
            st.session_state["tingling_location"] = current_tingling_location

        if ["weekness"] in st.session_state:
            current_weekness = st.session_state["weekness"]

        else:

            current_weekness = st.selectbox(
                "Do you have weekness in the body",
                [
                    "No",
                    "Yes",
                ],
            )
            st.session_state["weekness"] = current_weekness

        if ["weekness_intensity"] in st.session_state:
            current_weekness_intensity = st.session_state["weekness_intensity"]

        else:

            current_weekness_intensity = st.selectbox(
                "What is the intensity of weekness in the body",
                [
                    "No weekness",
                    "Mild (It doesn't bother me much but I feel it)",
                    "Moderate  (Feel it everday but I manage)",
                    "Severe (Daily activities are affected)",
                    "Life has no meaning (Need immediate relief)",
                ],
            )
            st.session_state["weekness_intensity"]= current_weekness_intensity

        if ["weekness_location"] in st.session_state:
            current_weekness_location = st.session_state["weekness_location"]

        else:

            current_weekness_location = st.multiselect(
                "Where do you have weekness in the body",
                [
                    "No weekness",
                    "Neck",
                    "Shoulder",
                    "Arm",
                    "Forearm",
                    "Elbow",
                    "Wrist + Hand",
                    "Upper Back",
                    "Lower Back",
                    "Hip & Thigh",
                    "Knee",
                    "Shin",
                    "Ankle",
                    "Foot",
                    "Chest",
                    "Groin",
                    "Stomach",
                ],
                default="No weekness",
            )
            st.session_state["weekness_location"] = current_weekness_location

        if ["tightness"] in st.session_state:
            current_tightness = st.session_state["tightness"]

        else:
            current_tightness = st.selectbox(
                "Do you have Tightness or Stiffness in muscles or joints in the body",
                [
                    "No",
                    "Yes",
                ],
            )
            st.session_state["tightness"] = current_tightness

        if ["tightness_intensity"] in st.session_state:
            current_tightness_intensity = st.session_state["tightness_intensity"]

        else:
            current_tightness_intensity = st.selectbox(
                "What is the intensity of Tightness or Stiffness in the body",
                [
                    "No Tightness or Stiffness",
                    "Mild (It doesn't bother me much but I feel it)",
                    "Moderate  (Feel it everday but I manage)",
                    "Severe (Daily activities are affected)",
                    "Life has no meaning (Need immediate relief)",
                ],
            )
            st.session_state["tightness_intensity"] = current_tightness_intensity

        if ["tightness_location"] in st.session_state:
            current_tightness_location = st.session_state["tightness_location"]
        else:
            current_tightness_location = st.multiselect(
                "Where do you have Tightness or Stiffness in the body",
                [
                    "No Tightness or Stiffness",
                    "Neck",
                    "Shoulder",
                    "Arm",
                    "Forearm",
                    "Elbow",
                    "Wrist + Hand",
                    "Upper Back",
                    "Lower Back",
                    "Hip & Thigh",
                    "Knee",
                    "Shin",
                    "Ankle",
                    "Foot",
                    "Chest",
                    "Groin",
                    "Stomach",
                ],
                default="No Tightness or Stiffness",
            )
            st.session_state["tightness_location"] = current_tightness_location
  
        
        submitted = st.form_submit_button("Submit To BankaiFit")
        if submitted:
            st.write("Thanks for Submitting Infomration")

            switch_page("life Style Information")


app()
