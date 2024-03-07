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
    return (
        pain,
        pain_intensity,
        pain_location,
        tingling,
        tingling_intensity,
        tingling_location,
    )


app()
