import streamlit as st
from pages.basic import current_weights

new_weight = st.session_state.get('current_weights', 80) * 2
