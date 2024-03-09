import streamlit as st
from st_pages import add_page_title
from algo.shs import new_weigh
import streamlit_extras as ste
add_page_title()

for k, v in st.session_state.items():
    st.session_state[k] = v
def app():

    st.write(

        st.session_state['weight'] 
        )
    #option = ste.selectbox("How would you like to be contacted?", range(100),key="selectbox")

   # st.write("You selected:", option)

 
app()