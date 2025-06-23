import streamlit as st
import time
from data_handler import save_responses
import uuid

def post_survey1():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    st.title("Welcome to the Post-Survey!")
    st.markdown("---")
    st.markdown('''<div style="font-size: 20px">
                Now that you've had a chance to converse with the AI,
                we'd like to get back to some of the questions we asked at the beginning of the survey.
                </div>''', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if st.button("Next"):
            end_time = time.time()
            time_spent = round(end_time - st.session_state.start_time, 2)
            
            st.session_state.postsurvey1_time = time_spent
            
            total_time = (
                st.session_state.get("first_page_time", 0)
                + st.session_state.get("informed_agree_time", 0)
                + st.session_state.get("informed_disagree_time", 0)
                + st.session_state.get("presurvey_polarization1_time", 0)
                + st.session_state.get("presurvey_polarization2_time", 0)
                + st.session_state.get("presurvey_polarization3_time", 0)
                + st.session_state.get("presurvey_polarization4_time", 0)
                + st.session_state.get("presurvey_polarization5_time", 0)
                + st.session_state.get("presurvey_polarization6_time", 0)
                + st.session_state.get("presurvey_polarization7_time", 0)
                + st.session_state.get("attention_time", 0)
                + st.session_state.get("gender_time", 0)
                + st.session_state.get("age_time", 0)
                + st.session_state.get("ethnic_time", 0)
                + st.session_state.get("education_time", 0)
                + st.session_state.get("presurvey_ai0_time", 0)
                + st.session_state.get("presurvey_ai1_time", 0)
                + st.session_state.get("presurvey_ai2_time", 0)
                + st.session_state.get("human_ai1_time", 0)
                + st.session_state.get("human_ai2_time", 0)
                + st.session_state.get("human_ai4_time", 0)
                + st.session_state.get("human_ai5_time", 0)
                + st.session_state.get("human_ai6_time", 0)
                + st.session_state.get("human_ai7_time", 0)
                + st.session_state.get("postsurvey1_time", 0)
                )
                
            total_time = round(total_time, 2)
            
            if "participant_id" not in st.session_state:
                    st.session_state.participant_id = str(uuid.uuid4())
            st.session_state.responses.update({
                "participant_id": st.session_state.participant_id,
                "Postsurvey1 Time": st.session_state.get("postsurvey1_time"),
                "total_time": total_time
                })
                    
            save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)

            st.session_state.start_time = time.time()
            st.session_state.step = "post_survey2"
            st.rerun()
        
        
def post_survey2():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
        
    if "first_visit9" not in st.session_state:
        st.session_state.first_visit9 = time.time()
    topic = st.session_state.get("highRatedTopic")
    st.title("Post-Survey")
    st.markdown("---")
    st.markdown('''<div style="font-size: 20px">
                At the beginning of the Human-AI conversation survey, you stated a strong opinion about the following statement:<br><br>
                </div>''', unsafe_allow_html=True)
    st.write("\n\n"
             "' ", f"**{topic['label']}**", " '\n\n")
    st.markdown('''<div style="font-size: 20px">
                On a scale from <strong>0% (strongly disagree) to 100% (strongly agree)</strong>, please indicate how much you agree or disagree with this statement.<br><br>
                </div>''', unsafe_allow_html=True)
    selected_value = st.slider("Select a value", min_value=0, max_value=100, step=10, format="%d%%")
    
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3,6,1])
    with col3:
    
        if selected_value == 0 and st.session_state.first_visit9:
            next_button_disabled = True        
        else:
            st.session_state.first_visit9 = False
            next_button_disabled=False
        
        if st.button("Next", disabled=next_button_disabled):
            end_time = time.time()
            time_spent = round(end_time - st.session_state.start_time, 2)
            
            st.session_state.postsurvey2_response = selected_value
            st.session_state.postsurvey2_time = time_spent
            
            total_time = (
                st.session_state.get("first_page_time", 0)
                + st.session_state.get("informed_agree_time", 0)
                + st.session_state.get("informed_disagree_time", 0)
                + st.session_state.get("presurvey_polarization1_time", 0)
                + st.session_state.get("presurvey_polarization2_time", 0)
                + st.session_state.get("presurvey_polarization3_time", 0)
                + st.session_state.get("presurvey_polarization4_time", 0)
                + st.session_state.get("presurvey_polarization5_time", 0)
                + st.session_state.get("presurvey_polarization6_time", 0)
                + st.session_state.get("presurvey_polarization7_time", 0)
                + st.session_state.get("attention_time", 0)
                + st.session_state.get("gender_time", 0)
                + st.session_state.get("age_time", 0)
                + st.session_state.get("ethnic_time", 0)
                + st.session_state.get("education_time", 0)
                + st.session_state.get("presurvey_ai0_time", 0)
                + st.session_state.get("presurvey_ai1_time", 0)
                + st.session_state.get("presurvey_ai2_time", 0)
                + st.session_state.get("human_ai1_time", 0)
                + st.session_state.get("human_ai2_time", 0)
                + st.session_state.get("human_ai4_time", 0)
                + st.session_state.get("human_ai5_time", 0)
                + st.session_state.get("human_ai6_time", 0)
                + st.session_state.get("human_ai7_time", 0)
                + st.session_state.get("postsurvey1_time", 0)
                + st.session_state.get("postsurvey2_time", 0)
                )
                
            total_time = round(total_time, 2)
            
            if "participant_id" not in st.session_state:
                    st.session_state.participant_id = str(uuid.uuid4())
            st.session_state.responses.update({
                "participant_id": st.session_state.participant_id,
                "Postsurvey2 Time": st.session_state.get("postsurvey2_time"),
                "Postsurvey2 Response": st.session_state.get("postsurvey2_response"),
                "total_time": total_time
                })
                    
            save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
            
            st.session_state.start_time = time.time()
            st.session_state.step = "post_survey3"
            st.rerun()
        
        
def post_survey3():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
        
    if "first_visit9" not in st.session_state:
        st.session_state.first_visit9 = time.time()
    topic = st.session_state.get("highRatedTopic")
    st.title("Post-Survey")
    st.markdown("---")
    st.markdown('''<div style="font-size: 20px">
                Did your view on this topic change after the conversation with the AI?<br>Why or why not?<br><br>
                Was there anything the AI said that made you think differently?<br><br>
                </div>''', unsafe_allow_html=True)
    
    st.markdown("<div>Please write your answer below. Press <strong>Enter</strong> to confirm.</div>", unsafe_allow_html=True)
    
    inputUser = st.text_input("")

    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if not inputUser:
            st.button("Next", disabled=True)
        else:
            if st.button("Next"):
                    end_time = time.time()
                    time_spent = round(end_time - st.session_state.start_time, 2)
                    
                    st.session_state.postsurvey3_response = inputUser
                    st.session_state.postsurvey3_time = time_spent
                    
                    total_time = (
                        st.session_state.get("first_page_time", 0)
                        + st.session_state.get("informed_agree_time", 0)
                        + st.session_state.get("informed_disagree_time", 0)
                        + st.session_state.get("presurvey_polarization1_time", 0)
                        + st.session_state.get("presurvey_polarization2_time", 0)
                        + st.session_state.get("presurvey_polarization3_time", 0)
                        + st.session_state.get("presurvey_polarization4_time", 0)
                        + st.session_state.get("presurvey_polarization5_time", 0)
                        + st.session_state.get("presurvey_polarization6_time", 0)
                        + st.session_state.get("presurvey_polarization7_time", 0)
                        + st.session_state.get("attention_time", 0)
                        + st.session_state.get("gender_time", 0)
                        + st.session_state.get("age_time", 0)
                        + st.session_state.get("ethnic_time", 0)
                        + st.session_state.get("education_time", 0)
                        + st.session_state.get("presurvey_ai0_time", 0)
                        + st.session_state.get("presurvey_ai1_time", 0)
                        + st.session_state.get("presurvey_ai2_time", 0)
                        + st.session_state.get("human_ai1_time", 0)
                        + st.session_state.get("human_ai2_time", 0)
                        + st.session_state.get("human_ai4_time", 0)
                        + st.session_state.get("human_ai5_time", 0)
                        + st.session_state.get("human_ai6_time", 0)
                        + st.session_state.get("human_ai7_time", 0)
                        + st.session_state.get("postsurvey1_time", 0)
                        + st.session_state.get("postsurvey2_time", 0)
                        + st.session_state.get("postsurvey3_time", 0)
                        )
                        
                    total_time = round(total_time, 2)
                    
                    if "participant_id" not in st.session_state:
                            st.session_state.participant_id = str(uuid.uuid4())
                    st.session_state.responses.update({
                        "participant_id": st.session_state.participant_id,
                        "Postsurvey3 Time": st.session_state.get("postsurvey3_time"),
                        "Postsurvey3 Response": st.session_state.get("postsurvey3_response"),
                        "total_time": total_time
                        })
                            
                    save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
                    
                    st.session_state.start_time = time.time()
                    st.session_state.step = "end_survey_page"
                    st.rerun()
                  


    
    
