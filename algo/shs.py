import streamlit as st
from pages.basic import form_1

def call_back():
    new_weight = st.session_state["weight"] *2
    return new_weight
