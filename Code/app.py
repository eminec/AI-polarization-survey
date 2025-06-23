import streamlit as st
from data_handler import save_responses
import time
import uuid
from urllib.parse import parse_qs
import os
import pandas as pd
from datetime import datetime

#Prolific PID
query_params = st.query_params
prolific_id = st.query_params.get("PROLIFIC_PID", "NO_PROLIFIC_ID")

if not prolific_id:
    prolific_id = "NO_PROLIFIC_ID"
    
st.session_state["prolific_id"] = prolific_id

#initial state
if 'step' not in st.session_state:
        st.session_state.step = "intro"

#Introduction page
if st.session_state.step == "intro":
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
      
    st.title("Welcome to this survey!")
    st.markdown("---")
    st.markdown("#### Thank you for your interest in participating in this research study! \n\n")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('''<div style="font-size: 18px">In this study, you will engage in a <strong>brief conversation with an AI chatbot</strong> and
                answer some questions about your opinions and experiences.
                <br>The entire study should take around 15 minutes to complete.
                <br>Your responses will help us understand how people <strong>interact with AI</strong> and
                how these interactions may <strong>influence their views on important societal topics</strong>.</div>''', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([3,6,1])
    with col3: 
        if st.button("Next"):
            end_time = time.time()
            time_spent = round(end_time - st.session_state.start_time, 2)
            st.session_state.first_page_time = time_spent
                    
            total_time = st.session_state.get("first_page_time", 0)
                    
            total_time = round(total_time, 2)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if "participant_id" not in st.session_state:
                    st.session_state.participant_id = str(uuid.uuid4())
            st.session_state.responses.update({
                "prolific_id": st.session_state.get("prolific_id"),
                "participant_id": st.session_state.participant_id,
                "timestamp": current_time,
                "First Page Time": st.session_state.get("first_page_time"),
                "total_time": total_time
            })
                    
            save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)

            st.session_state.start_time = time.time()
            st.session_state.step = "informed_consent_page"
            st.rerun()    
        
    
elif st.session_state.step == "informed_consent_page":
    import informed_consent as informed_consent
    informed_consent.run()
    
elif st.session_state.step == "gender":
    import demographic as demographic
    demographic.gender()
    
elif st.session_state.step == "age":
    import demographic as demographic
    demographic.age()
    
elif st.session_state.step == "ethnic":
    import demographic as demographic
    demographic.ethnic()
    
elif st.session_state.step == "education":
    import demographic as demographic
    demographic.education()
    
elif st.session_state.step == "end_survey_page":
    import end_of_survey as end_of_survey
    end_of_survey.run()

elif st.session_state.step == "presurvey_run":
    import pre_survey_AI as pre_survey_AI
    pre_survey_AI.run()

elif st.session_state.step == "presurvey_1":
    import pre_survey_AI as pre_survey_AI
    pre_survey_AI.presurvey_1()
    
elif st.session_state.step == "presurvey_2":
    import pre_survey_AI as pre_survey_AI
    pre_survey_AI.presurvey_2()
    
elif st.session_state.step == "presurvey_polarization1":
    import pre_survey_polarization as pre_survey_polarization
    pre_survey_polarization.presurvey_1()
    
elif st.session_state.step == "presurvey_polarization2":
    import pre_survey_polarization as pre_survey_polarization
    pre_survey_polarization.presurvey_2()
    
elif st.session_state.step == "presurvey_polarization3":
    import pre_survey_polarization as pre_survey_polarization
    pre_survey_polarization.presurvey_3()
    
elif st.session_state.step == "presurvey_polarization4":
    import pre_survey_polarization as pre_survey_polarization
    pre_survey_polarization.presurvey_4()
    
elif st.session_state.step == "presurvey_polarization5":
    import pre_survey_polarization as pre_survey_polarization
    pre_survey_polarization.presurvey_5()
    
elif st.session_state.step == "presurvey_polarization6":
    import pre_survey_polarization as pre_survey_polarization
    pre_survey_polarization.presurvey_6()
    
elif st.session_state.step == "presurvey_polarization7":
    import pre_survey_polarization as pre_survey_polarization
    pre_survey_polarization.presurvey_7()
    
elif st.session_state.step == "attention":
    import attention as attention
    attention.attention()
    
elif st.session_state.step == "human_ai1":
    import human_ai as human_ai
    human_ai.human_ai1()
    
elif st.session_state.step == "human_ai4":
    import human_ai as human_ai
    human_ai.human_ai4()
    
elif st.session_state.step == "human_ai_evidence":
    import human_ai as human_ai
    human_ai.human_ai_evidence()
    
elif st.session_state.step == "human_ai5":
    import human_ai as human_ai
    human_ai.human_ai5()
    
elif st.session_state.step == "human_ai6":
    import human_ai as human_ai
    human_ai.human_ai6()
    
elif st.session_state.step == "human_ai7":
    import human_ai as human_ai
    human_ai.human_ai7()
    
elif st.session_state.step == "post_survey1":
    import post_survey as post_survey
    post_survey.post_survey1()

elif st.session_state.step == "post_survey2":
    import post_survey as post_survey
    post_survey.post_survey2()
    
elif st.session_state.step == "post_survey3":
    import post_survey as post_survey
    post_survey.post_survey3()     
    
    
