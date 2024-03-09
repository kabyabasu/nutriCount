import streamlit as st
from st_pages import add_page_title
#from algo.shs import new_weigh
import streamlit_extras as ste
add_page_title()

# for k, v in st.session_state.items():
#     st.session_state[k] = v
def app():
    try:

        st.write(
            "Hey",st.session_state['name'],".\n"

            "Your weight is", st.session_state['weight'],".\n",
            "Your Height is" ,st.session_state['height'], 
            "Your current Occupation is st.session_state['occupation']"
            )

    except:
        st.write("Well! You need to finish Giving Us Input","Go Back to Profile Settings and Procvide Us required Input")
    #option = ste.selectbox("How would you like to be contacted?", range(100),key="selectbox")

   # st.write("You selected:", option)

 
app()