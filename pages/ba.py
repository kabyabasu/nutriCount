import streamlit as st
from st_pages import add_page_title

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
        pain_location = st.multiselect(
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
        tingling = st.selectbox(
            "Do you have Tingling or Numbness in the body",
            [
                "No",
                "Yes",
            ],
        )
        tingling_intensity = (
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

        tingling_location = st.multiselect(
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
        weekness = st.selectbox(
            "Do you have weekness in the body",
            [
                "No",
                "Yes",
            ],
        )
        weekness_intensity = st.selectbox(
            "What is the intensity of weekness in the body",
            [
                "No weekness",
                "Mild (It doesn't bother me much but I feel it)",
                "Moderate  (Feel it everday but I manage)",
                "Severe (Daily activities are affected)",
                "Life has no meaning (Need immediate relief)",
            ],
        )
        weekness_location = st.multiselect(
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
        tightness = st.selectbox(
            "Do you have Tightness or Stiffness in muscles or joints in the body",
            [
                "No",
                "Yes",
            ],
        )
        tightness_intensity = st.selectbox(
            "What is the intensity of Tightness or Stiffness in the body",
            [
                "No Tightness or Stiffness",
                "Mild (It doesn't bother me much but I feel it)",
                "Moderate  (Feel it everday but I manage)",
                "Severe (Daily activities are affected)",
                "Life has no meaning (Need immediate relief)",
            ],
        )
        tightness_location = st.multiselect(
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
  
        
        st.form_submit_button("submit")


app()
