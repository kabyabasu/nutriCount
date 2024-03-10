import streamlit as st
from st_pages import add_page_title
import streamlit_extras as ste
add_page_title()

# for k, v in st.session_state.items():
#     st.session_state[k] = v
def app():
    #col1,col2 = st.columns([1,1])

    raw_sources = ["Severe Thinness","Moderate Thinness","Mild Thinness","Normal","Overweight","Obese Class I","Obese Class II","Obese Class III"]
    
    thresholds_height = [
        147, 149, 152, 154, 157, 159, 162, 164, 167, 169, 172, 174, 177, 179, 182, 185, 187, 190, 192
    ]
    
    # Defining return values (ranges) and calculating medians
    return_values = [
        (41.4, 52.3), (42.8, 54.1), (44.1, 56.0), (45.5, 57.8), (47.3, 59.6),
        (48.7, 61.4), (50.0, 63.7), (51.9, 65.5), (53.7, 67.3), (55.0, 69.6),
        (56.9, 71.9), (58.2, 73.7), (60.0, 76.0), (61.9, 78.2), (63.7, 80.5),
        (65.5, 82.8), (67.3, 84.6), (69.1, 87.3), (71.0, 89.6)
    ]
    
    # Creating a list of tuples, each with a threshold, return range, and median
    thresholds_and_values = [
        (thresholds_height, val, (val[0] + val[1]) / 2) for threshold, val in zip(thresholds_height, return_values)
    ]

    st.markdown("#Summary Health Status")

    if ["bmi"] in st.session_state:
        current_bmi = st.session_state["bmi"]
    else:
        current_bmi = (st.session_state["height"]/ (st.session_state["weight"]/100) ** 2)
        st.session_state["bmi"] = current_bmi

    if ["bmi_Prime"] in st.session_state:
        current_bmi_prime = st.session_state["bmi_prime"]
    else:
        current_bmi_prime = (st.session_state["height"]/ (st.session_state["weight"]/100) ** 2)/25
        st.session_state["bmi_prime"] = current_bmi_prime


    if ["health_category"] in st.session_state:
        current_health_category = st.session_state["health_category"]

    else:
    
        if current_bmi < 16:
             current_health_category = raw_sources[0]
        elif current_bmi < 17:
            current_health_category = raw_sources[1]
        elif current_bmi < 18.5:
            current_health_category = raw_sources[2]
        elif current_bmi < 25:
            current_health_category = raw_sources[3]
        elif current_bmi < 30:
            current_health_category = raw_sources[4]
        elif current_bmi < 35:
            current_health_category = raw_sources[5]
        elif current_bmi < 40:
            current_health_category = raw_sources[6]
        else:
            current_health_category = raw_sources[7]
        
        st.session_state["health_category"] = current_health_category

    if ["healthy_weight_range"] in st.session_state:
        current_healthy_weight_range = st.session_state["healthy_weight_range"]

    else:
        for thresholds_height, value_range, median in thresholds_and_values:
            if st.session_state['height'] <= thresholds_height:
                current_healthy_weight_range = value_range
        st.session_state["healthy_weight_range"] = current_healthy_weight_range
            

        



    




    
    st.write("Your BMI is ",int(current_bmi))
    st.write("Your BMI Prime is ",int(st.session_state["bmi_prime"]))
    st.write("Your Health Category according to BankaiFit is ", current_health_category)
    st.write("Your ideal weight Range",current_healthy_weight_range)




    



    # try:
    
    # st.write(
    #     "Hey",st.session_state['name'],"  \n",

    #     "Your weight is", st.session_state['weight'],".  \n",
    #     "Your Height is" ,st.session_state['height'],'  \n',
    #     "Your current Occupation is", st.session_state['occupation'],".  \n",
    #     "Your current number of work hour is", st.session_state['duration_of_workday'],".  \n",
    #     "Your Gender is ",st.session_state['gender'],".  \n",
    #     "You are", st.session_state["pregnant"], "pregnent",".  \n",
    #     "You are", st.session_state["breastfeeding"], "breastfeeding",".  \n",
    #     "You have pain",st.session_state["pain"],".  \n",
    #     "Your pain intesity is", st.session_state["pain_intensity"],".  \n",
    #     "Your Pain Location is ", st.session_state["pain_location"][0],".  \n",
    #     "Your have tingling sension", st.session_state["tingling"],".  \n",
    #     "Your tignling intensity is ",st.session_state["tingling_intensity"],".  \n",
    #     "Your current tingling location is ", st.session_state["tingling_location"][0],".  \n",
    #     "You have weekness in", st.session_state["weekness"],".  \n",
    #     "Your weekness intensity is ",st.session_state["weekness_intensity"],".  \n",
    #     "Your current weekness location is ", st.session_state["weekness_location"][0],".  \n",
    #     "You have tightness in", st.session_state["tightness"],".  \n",
    #     "Your tightness intensity is ",st.session_state["tightness_intensity"],".  \n",
    #     "Your current tightness location is ", st.session_state["tightness_location"][0],".  \n",
    #     "Your diet style is ",st.session_state["diet_style"],".  \n",
    #     "How many meals you eat per day",st.session_state["cnom"],".  \n",
    #     "What are these meals",st.session_state["cnom_detail"],".  \n",
    #     "what is your first meal", st.session_state["first_major_meal"],"  \n",
    #     "How many cups of coffee you drink", st.session_state["ci"],"  \n",
    #     "How many Lt. of water you drink" ,st.session_state["water_intake"],"  \n" ,
    #     "What is your daily Cal Consumption (best guess)",st.session_state["daily_calories"],"  \n",
    #     "What % of your total calories from Carb consumption (best guess)",st.session_state["dails_carbs"],"  \n",
    #     "What % of your total calories from fat consumption (best guess)",st.session_state["dails_fat"],"  \n",
    #     "What % of your total calories from Protein consumption (best guess)",st.session_state["dails_protein"],"  \n",
    #     # "Choose the food item or items to which you are allergic",[st.session_state["allergens"][i] for i in st.session_state["allergens"]],"  \n",
    #     # "Choose the item or items that align with your dietary Observation ",[st.session_state["diet_observation"][i] for i in st.session_state["diet_observation"]]
    #     "Your primary Goal",st.session_state["g1"],
    #     "Your secondary Goal",st.session_state["g2"],
    #     "Your Teritary Goal",st.session_state["g3"],
    #     "Do you have any of these medical Conditions",st.session_state["mc"][0],"  \n",
    #     "If you have any medical condition that is not mentioned above, please give details",st.session_state["mc_add"],"  \n",
    #     "Do you have any of the following Special Conditions",st.session_state["md"][0],"  \n",
    #     "If you have any Special condition that is not mentioned above, please give details",st.session_state["md_ad"],"  \n",
    #     "What is the level of your physical Activity",st.session_state["lifeStyle"],"  \n",
    #     "Chose the best option that suggest your current fitness Level",st.session_state["Fitness_Level"],"  \n",
    #     "Are you a smoker",st.session_state["smoker"],"  \n",
    #     "How much alcohol do you consume",st.session_state["alcohol"],"  \n",
    #     "Are you Ready to Incorporate Exercise in your Daily routine",st.session_state["otie"],"  \n",
    #     "Do you take any health supplements",st.session_state["supply"],"  \n"



    # except:
    #     st.write("Well! You need to finish Giving Us Input","Go Back to Profile Settings and Procvide Us required Input")
    #option = ste.selectbox("How would you like to be contacted?", range(100),key="selectbox")

   # st.write("You selected:", option)


app()