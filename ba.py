import streamlit as st
from st_pages import add_page_title

add_page_title()


def app():
    pain = st.selectbox(
        "Do you have Pain in the body",
        [
            "No",
            "Yes",
        ],
    )
    pain_intensity = st.selectbox(
        "What is the intensity of Pain in the body",
        [
            "No Pain",
            "Mild (It doesn't bother me much but I feel it)",
            "Moderate  (Feel it everday but I manage)",
            "Severe (Daily activities are affected)",
            "Life has no meaning (Need immediate relief)",
        ],
    )
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


app()
