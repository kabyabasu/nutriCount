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
            "Hey",st.session_state['name'],"  \n",

            "Your weight is", st.session_state['weight'],".  \n",
            "Your Height is" ,st.session_state['height'],'  \n',
            "Your current Occupation is", st.session_state['occupation'],".  \n",
            "Your current number of work hour is", st.session_state['duration_of_workday'],".  \n",
            "Your Gender is ",st.session_state['gender'],".  \n",
            "You are", st.session_state["pregnant"], "pregnent",".  \n",
            "You are", st.session_state["breastfeeding"], "breastfeeding",".  \n",
            "You have pain",st.session_state["pain"],".  \n",
            "Your pain intesity is", st.session_state["pain_intensity"],".  \n",
            "Your Pain Location is ", st.session_state["pain_location"][0],".  \n",
            "Your have tingling sension", st.session_state["tingling"],".  \n",
            "Your tignling intensity is ",st.session_state["tingling_intensity"],".  \n",
            "Your current tingling location is ", st.session_state["tingling_location"][0],".  \n",
            "You have weekness in", st.session_state["weekness"],".  \n",
            "Your weekness intensity is ",st.session_state["weekness_intensity"],".  \n",
            "Your current weekness location is ", st.session_state["weekness_location"][0],".  \n",
            "You have tightness in", st.session_state["tightness"],".  \n",
            "Your tightness intensity is ",st.session_state["tightness_intensity"],".  \n",
            "Your current tightness location is ", st.session_state["tightness_location"][0],".  \n",
            "Your diet style is ",st.session_state["diet_style"],".  \n",
            "How many meals you eat per day",st.session_state["cnom"],".  \n",
            "What are these meals",st.session_state["cnom_detail"],".  \n",
            "what is your first meal", st.session_state["first_major_meal"],"  \n",
            "How many cups of coffee you drink", st.session_state["ci"],"  \n",
            "How many Lt. of water you drink" ,st.session_state["water_intake"],"  \n" ,
            "What is your daily Cal Consumption (best guess)",st.session_state["daily_calories"],"  \n",
            "What % of your total calories from Carb consumption (best guess)",st.session_state["dails_carbs"],"  \n",
            "What % of your total calories from fat consumption (best guess)",st.session_state["dails_fat"],"  \n",
            "What % of your total calories from Protein consumption (best guess)",st.session_state["dails_protein"],"  \n",
            # "Choose the food item or items to which you are allergic",[st.session_state["allergens"][i] for i in st.session_state["allergens"]],"  \n",
            # "Choose the item or items that align with your dietary Observation ",[st.session_state["diet_observation"][i] for i in st.session_state["diet_observation"]]
            "Your primary Goal",st.session_state["g1"],"  \n",
            "Your secondary Goal",st.session_state["g2"],"  \n",
            "Your Teritary Goal",st.session_state["g3"],"  \n",
            "Do you have any of these medical Conditions",st.session_state["mc"][0],"  \n",
            "If you have any medical condition that is not mentioned above, please give details",st.session_state["mc_add"],"  \n",
            "Do you have any of the following Special Conditions",st.session_state["md"],"  \n",
            "If you have any Special condition that is not mentioned above, please give details",st.session_state["md_ad"],"  \n"




            )

    except:
        st.write("Well! You need to finish Giving Us Input","Go Back to Profile Settings and Procvide Us required Input")
    #option = ste.selectbox("How would you like to be contacted?", range(100),key="selectbox")

   # st.write("You selected:", option)

 
app()