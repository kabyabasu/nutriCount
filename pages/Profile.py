import streamlit as st
from st_pages import add_page_title
import streamlit_extras as ste
import math

add_page_title()

# for k, v in st.session_state.items():
#     st.session_state[k] = v
def app():
    #col1,col2 = st.columns([1,1])

    raw_sources = ["Severe Thinness","Moderate Thinness","Mild Thinness","Normal","Overweight","Obese Class I","Obese Class II","Obese Class III"]
    thresholds_values_dict = {147: {'range': (41.4, 52.3), 'median': 46.85},149: {'range': (42.8, 54.1), 'median': 48.45},152: {'range': (44.1, 56.0), 'median': 50.05},154: {'range': (45.5, 57.8), 'median': 51.65},157: {'range': (47.3, 59.6), 'median': 53.45},159: {'range': (48.7, 61.4), 'median': 55.05},162: {'range': (50.0, 63.7), 'median': 56.85},164: {'range': (51.9, 65.5), 'median': 58.7},167: {'range': (53.7, 67.3), 'median': 60.5},169: {'range': (55.0, 69.6), 'median': 62.3},172: {'range': (56.9, 71.9), 'median': 64.4},174: {'range': (58.2, 73.7), 'median': 65.95},177: {'range': (60.0, 76.0), 'median': 68.0},179: {'range': (61.9, 78.2), 'median': 70.05},182: {'range': (63.7, 80.5), 'median': 72.1},185: {'range': (65.5, 82.8), 'median': 74.15},187: {'range': (67.3, 84.6), 'median': 75.95},190: {'range': (69.1, 87.3), 'median': 78.2},192: {'range': (71.0, 89.6), 'median': 80.3}}


    


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
        # Your height for comparison

        # Loop through the dictionary to find the matching range and median based on your height
        for threshold, details in thresholds_values_dict.items():
            if st.session_state['height'] <= threshold:
                current_healthy_weight_range = details['range']
                break
        st.session_state["healthy_weight_range"] = current_healthy_weight_range

    if ["weight_change_category"] in st.session_state:
        current_weight_change_category = st.session_state["weight_change_category"]

    else:
        if current_bmi <= -500:
            current_weight_change_category = "Rapid Weight Loss"
        elif current_bmi <= -250:
            current_weight_change_category = "Easy Weight Loss"
        elif current_bmi <= -100:
            current_weight_change_category = "Slow Weight Loss"
        elif current_bmi == 0:
            current_weight_change_category = "Maintains Weight"
        elif current_bmi <= 100:
            current_weight_change_category = "Slow Weight Gain"
        elif current_bmi <= 250:
            current_weight_change_category = "Easy Weight Gain"
        else:
            current_weight_change_category = "Rapid Weight Gain"
    
    st.session_state["weight_change_category"] = current_weight_change_category


    if ["healthy_weight_median"] in st.session_state:
        current_healthy_weight_median = st.session_state["healthy_weight_median"]

    else:
        # Your height for comparison

        # Loop through the dictionary to find the matching range and median based on your height
        for threshold, details in thresholds_values_dict.items():
            if st.session_state['height'] <= threshold:
                current_healthy_weight_median = details['median']
                break
        st.session_state["healthy_weight_median"] = current_healthy_weight_median

    if ["required_weight_change"] in st.session_state:
        current_required_weight_change = st.session_state["required_weight_change"]

    else:
        current_required_weight_change = st.session_state['weight']-current_healthy_weight_median
        st.session_state["required_weight_change"] = current_required_weight_change

    if ["required_min_weight_change"] in st.session_state:
        current_required_min_weight_change = st.session_state["required_min_weight_change"]

    else:
        current_required_min_weight_change = st.session_state['weight']-max(st.session_state["healthy_weight_range"])
        st.session_state["required_min_weight_change"] = current_required_min_weight_change

    
    if ["maintainance_calorific_intake"] in st.session_state:
        current_maintainance_calorific_intake = st.session_state["maintainance_calorific_intake"]

    else:
        if st.session_state["gender"] == "Male":
            current_maintainance_calorific_intake = (66.5 + (13.75 * st.session_state['weight']) + (5 * st.session_state['height']) - (6.76 * st.session_state["age"])) * st.session_state["lifeStyle_value"]

        else:

            current_maintainance_calorific_intake = (655.1 + (9.56 * st.session_state['weight']) + (1.85 * st.session_state['height']) - (4.7 * st.session_state["age"])) * st.session_state["lifeStyle_value"]

        st.session_state["maintainance_calorific_intake"] = current_maintainance_calorific_intake


    if ["recommended_calorific_intake"] in st.session_state:
        current_recommended_calorific_intake = st.session_state["recommended_calorific_intake"]

    else:
        if st.session_state["gender"] == "Male":
            current_recommended_calorific_intake = (66.5 + (13.75 * current_healthy_weight_median) + (5 * st.session_state['height']) - (6.76 * st.session_state["age"])) * st.session_state["lifeStyle_value"]

        else:

            current_recommended_calorific_intake = (655.1 + (9.56 * current_healthy_weight_median) + (1.85 * st.session_state['height']) - (4.7 * st.session_state["age"])) * st.session_state["lifeStyle_value"]

        st.session_state["recommended_calorific_intake"] = current_recommended_calorific_intake

    if ["minimum_water_intake_in_litres"] in st.session_state:
        current_minimum_water_intake_in_litres = st.session_state["minimum_water_intake_in_litres"]

    else:
        if st.session_state["pregnant"] == "Yes":
            current_minimum_water_intake_in_litres = 2.5
        elif st.session_state["breastfeeding"] == "Yes":
            current_minimum_water_intake_in_litres = 3
        elif st.session_state["gender"] == "Male" and st.session_state["age"] >= 19:
            current_minimum_water_intake_in_litres = 3
        elif st.session_state["gender"] == "Female" and st.session_state["age"] >= 19:
            current_minimum_water_intake_in_litres = 2
        elif st.session_state["age"] in range(14, 19):
            current_minimum_water_intake_in_litres = 2.5
        elif st.session_state["age"] in range(9, 14):
            current_minimum_water_intake_in_litres = 2
        elif st.session_state["age"] in range(4, 9):
            current_minimum_water_intake_in_litres = 1.2
        elif st.session_state["age"] in range(1, 4):
            current_minimum_water_intake_in_litres = 1
        
        st.session_state["minimum_water_intake_in_litres"] = current_minimum_water_intake_in_litres


    if ["healthy_water_intake_in_litres"] in st.session_state:
        current_healthy_water_intake_in_litres = st.session_state["healthy_water_intake_in_litres"]

    else:
        current_healthy_water_intake_in_litres = math.ceil(current_minimum_water_intake_in_litres * 1.15 * 10) / 10
        st.session_state["healthy_water_intake_in_litres"] = current_healthy_water_intake_in_litres

    
    if ["recommended_caffeine_intake"] in st.session_state:
        current_recommended_caffeine_intake = st.session_state["recommended_caffeine_intake"]
    else:
        if st.session_state["pregnant"] == "Yes":
            current_recommended_caffeine_intake = "Not Recommended"
        else:
            if st.session_state["breastfeeding"] == "Yes":
                current_recommended_caffeine_intake = "2 Cups Black Coffee or 2 Cups Black Tea"
            else:
                current_recommended_caffeine_intake = "4 Cups Black Coffee or 4 Cups Black Tea"
       
        st.session_state["recommended_caffeine_intake"] = current_recommended_caffeine_intake


    if ["daily_protein_requirement_in_gms"] in st.session_state:
        current_daily_protein_requirement_in_gms = st.session_state["daily_protein_requirement_in_gms"]

    else:
        current_daily_protein_requirement_in_gms = st.session_state["diet_observation_values"] * st.session_state['weight']
        st.session_state["daily_protein_requirement_in_gms"] = current_daily_protein_requirement_in_gms










    


    
            

        



    




    col1 ,col2 = st.columns(2,gap="large")

    col1.header("Summary - Health Status")
    col1.write(f"Your BMI is {int(current_bmi)}")
    col1.write(f"Your BMI Prime is {int(st.session_state['bmi_prime'])}")
    col1.write(f"Your Health Category according to BankaiFit is {current_health_category}")
    col1.write(f"Your Ideal weight Range in KG {current_healthy_weight_range}")
    col1.write(f"Your Body is currently in Tendency of {current_weight_change_category}")

    col2.header("Summary - North Star")
    col2.write(f"Your Ideal weight should be (in KG) {current_healthy_weight_median}")
    col2.write(f"Required weight Change {current_required_weight_change}")
    col2.write(f"Required minimum weight Change {current_required_min_weight_change}")
    col2.write(f"Your Maintenance Calorific Intake is {current_maintainance_calorific_intake}")
    col2.write(f"Your Recommended Calorific Intake {current_recommended_calorific_intake}")
    col2.write(f"Your Minimum Water Intake In Litres {current_minimum_water_intake_in_litres}")
    col2.write(f"Your healthy Water Intake in Litres {current_healthy_water_intake_in_litres}")
    col2.write(f"Your Recommended Caffeine Intake is - {current_recommended_caffeine_intake}")
    col2.write(f"Your Daily Protein Requirement in gms is {current_daily_protein_requirement_in_gms}")




    # col1.markdown("#Summary Health Status")
    # col1.write("Your BMI is ",int(current_bmi))
    # col1.write("Your BMI Prime is ",int(st.session_state["bmi_prime"]))
    # col1.write("Your Health Category according to BankaiFit is ", current_health_category)
    # col1.write("Your Ideal weight Range in KG",current_healthy_weight_range)
    # col1.write("Your Body is currently in Tendency of ",current_weight_change_category)

    # col2.markdown("#North Star")
    # col2.write("Your Ideal weight should be (in KG)",current_healthy_weight_median)
    # col2.write("Required weight Change",current_required_weight_change)
    # col2.write("Required minimum weight Change",current_required_min_weight_change)
    # col2.write("Your Maintainance Calorific Intake is ", current_maintainance_calorific_intake)
    # col2.write("Your Recommended Calorific Intake",current_recommended_calorific_intake)
    # col2.write("Your Minimum Water Intake In Litres", current_minimum_water_intake_in_litres)
    # col2.write("Your healthy Water Intake in Litres",current_healthy_water_intake_in_litres)
    # col2.write("Your Recommended Caffeine Intake is - ", current_recommended_caffeine_intake)
    # col2.write("Your Daily Protein Requirement in gms is ",current_daily_protein_requirement_in_gms)






    



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