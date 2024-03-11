import streamlit as st
from st_pages import add_page_title
from streamlit_extras.switch_page_button import switch_page

add_page_title()


def app():
    with st.form("Lifestyle condition"):

        if ["mc"] in st.session_state:
            current_mc = st.session_state["mc"]
        else:
            current_mc = st.multiselect(
                "Do you have any of these medical Conditions",
                [
                    "None",
                    "HyperTension",
                    "High Pressure",
                    "Low Pressure",
                    "Heart Disease",
                    "Diabetes",
                    "Obesity",
                    "Malnourishment",
                    "Migraines",
                    "Thyroid",
                    "PCOS",
                    "Insomnia",
                ],
                default="None",
            )
            st.session_state["mc"] = current_mc

        if ["mc_add"] in st.session_state:
            current_mc_add = st.session_state["mc_add"]
        else:
            current_mc_add = st.text_input("If you have any medical condition that is not mentioned above, please give details", max_chars=130, placeholder="None")
            st.session_state["mc_add"] = current_mc_add

### Modifying for Special Conditions (`md` and `md_ad`)
        if ["md"] in st.session_state:
            current_md = st.session_state["md"]
        else:
            current_md = st.multiselect("Do you have any of the following Special Conditions", [
                "None",
                "Limb Loss",
                "Cerebral Palsy",
                "Stroke",
                "Spinal Cord Injury",
                "Epilepsy",
                "Spina Bifida"
            ], default="None")
            st.session_state["md"] = current_md

        if ["md_ad"] in st.session_state:
            current_md_ad = st.session_state["md_ad"]
        else:
            current_md_ad = st.text_input("If you have any Special condition that is not mentioned above, please give details", max_chars=130, placeholder="None")
            st.session_state["md_ad"] = current_md_ad

        submitted = st.form_submit_button("Submit To BankaiFit")
        if submitted:
            st.write("Thanks for Submitting Infomration")

            switch_page("Your Goal")


#     mc = st.multiselect(
#         "Do you have any of these medical Condition",
#         [
#             "None",
#             "HyperTension",
#             "High Pressure",
#             "Low Pressure",
#             "Heart Disease",
#             "Diabetes",
#             "Obesity",
#             "Malnourishment",
#             "Migraines",
#             "Thyroid",
#             "PCOS",
#             "Insomnia",
#         ],
#         default="None",
#     )
#     mc_add = st.text_input("If you have any medical condtion that is not mentioned above please give details",max_chars=130,disabled=False,placeholder="None")
#     md = st.multiselect("Do you any of the following Special Condition",[
#     "None",
#     "Limb Loss",
#     "Cerebral Palsy",
#     "Stroke",
#     "Spinal Cord Injury",
#     "Epilepsy",
#     "Spina Bifida"
# ],default="None")
#     md_ad = st.text_input("If you have any Special condtion that is not mentioned above please give details",max_chars=130,disabled=False,placeholder="None")






app()