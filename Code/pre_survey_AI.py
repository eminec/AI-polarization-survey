import streamlit as st
import time
import uuid
from data_handler import save_responses


def run():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    st.title("Welcome to the Pre-Survey on AI!")
    st.markdown("---")
    st.markdown('''<div style="font-size: 20px">
                Now that you have completed the Pre-Survey on social and political topics, along with some demographic questions, you'll be 
                asked <strong>questions about Large Language Models</strong>, like LLAMA, ChatGPT, and others.
                </div>''', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if st.button("Next"):
            end_time = time.time()
            time_spent = round(end_time - st.session_state.start_time, 2)
            
            st.session_state.presurvey_ai0_time = time_spent
            
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
                )
                
            total_time = round(total_time, 2) 
            
            if "participant_id" not in st.session_state:
                st.session_state.participant_id = str(uuid.uuid4())
                
            st.session_state.responses.update({
                "participant_id": st.session_state.participant_id,
                "Presurvey_ai0 Time": st.session_state.get("presurvey_ai0_time"),
                "total_time": total_time
                })
            
            save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
            
            st.session_state.start_time = time.time()
            st.session_state.step = "presurvey_1"
            st.rerun() 

def presurvey_1():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
        
    if "first_visit" not in st.session_state:
        st.session_state.first_visit = True
        
    st.title("Pre-Survey on AI")
    st.markdown("---")
    st.markdown('''<div style="font-size: 20px">
                <strong>How frequently</strong> do you use modern AI tools and services such as LLAMA, ChatGPT and others?
                </div>''', unsafe_allow_html=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    selected_value = st.slider("", min_value=1, max_value=7, step=1, value=1)
    st.markdown("""
    <div style="position: relative; height: 30px; margin-top: -130px; font-size: 0.65rem">
        <span style="position: absolute; left: 1%; transform: translateX(-50%); text-align: center; display: inline-block"><strong>Never</strong></span>
        <span style="position: absolute; left: 17%; transform: translateX(-50%); text-align: center; display: inline-block"><strong>Rarely</strong><br>less than once a month</span>
        <span style="position: absolute; left: 34%; transform: translateX(-50%); text-align: center; display: inline-block"><strong>Occasionally</strong><br>a few times a month</span>
        <span style="position: absolute; left: 50%; transform: translateX(-50%); text-align: center; display: inline-block"><strong>Sometimes</strong><br>about once a week</span>
        <span style="position: absolute; left: 66%; transform: translateX(-50%); text-align: center; display: inline-block"><strong>Often</strong><br>a few times a week</span>
        <span style="position: absolute; left: 83%; transform: translateX(-50%); text-align: center; display: inline-block"><strong>Very Often</strong><br>almost every day</span>
        <span style="position: absolute; left: 97%; transform: translateX(-50%); text-align: center; display: inline-block"><strong>Everyday</strong></span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="display: flex; justify-content: space-between; margin-top: -54px;">
        <span style="font-size: 0.90rem; font-weight:bold;">1</span>
        <span style="font-size: 0.85rem;">2</span>
        <span style="font-size: 0.85rem;">3</span>
        <span style="font-size: 0.90rem; font-weight:bold;">4</span>
        <span style="font-size: 0.85rem;">5</span>
        <span style="font-size: 0.85rem;">6</span>
        <span style="font-size: 0.90rem; font-weight:bold;">7</span>
    </div>
    """, unsafe_allow_html=True)

    
    st.markdown("<br>", unsafe_allow_html=True)

    if selected_value == 1 and st.session_state.first_visit:
        next_button_disabled = True        
    else:
        st.session_state.first_visit = False
        next_button_disabled=False
        
    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if st.button("Next", disabled=next_button_disabled):
            end_time = time.time()
            time_spent = round(end_time - st.session_state.start_time, 2)
                
            st.session_state.presurvey_ai1_response = selected_value
            st.session_state.presurvey_ai1_time = time_spent
            
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
                )
                
            total_time = round(total_time, 2) 
            
            if "participant_id" not in st.session_state:
                st.session_state.participant_id = str(uuid.uuid4())
                
            st.session_state.responses.update({
                "participant_id": st.session_state.participant_id,
                "Presurvey_ai1 Time": st.session_state.get("presurvey_ai1_time"),
                "Presurvey_ai1 Response": st.session_state.get("presurvey_ai1_response"),
                "total_time": total_time
                })
            
            save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
                
            st.session_state.start_time = time.time()
            st.session_state.step = "presurvey_2"
            st.rerun()
        
        
def presurvey_2():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    st.title("Pre-Survey on AI")
    st.markdown("---")
    st.markdown('''<div style="font-size: 20px">
                To what extent do you <strong>agree</strong> with the following statement:
                </div>''', unsafe_allow_html=True)
    st.markdown('''<div style="font-size: 20px">
                <strong>'I generally trust AI technologies like LLAMA.</strong>'
                </div>''', unsafe_allow_html=True)
    selected_value = st.radio("",
                            ["Strongly disagree", "Disagree", "Somewhat disagree", "Neither agree nor disagree", "Somewhat agree", "Agree", "Strongly agree"],
                            index=None)
    
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if selected_value is None:
            st.button("Next", disabled=True)
        else:
            if st.button("Next"):
                    end_time = time.time()
                    time_spent = round(end_time - st.session_state.start_time, 2)
                    
                    st.session_state.presurvey_ai2_response = selected_value
                    st.session_state.presurvey_ai2_time = time_spent
                    
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
                    )
                    
                    total_time = round(total_time, 2) 
                    
                    if "participant_id" not in st.session_state:
                        st.session_state.participant_id = str(uuid.uuid4())
                    
                    st.session_state.responses.update({
                        "participant_id": st.session_state.participant_id,
                        "Presurvey_ai2 Time": st.session_state.get("presurvey_ai2_time"),
                        "Presurvey_ai2 Response": st.session_state.get("presurvey_ai2_response"),
                        "total_time": total_time
                        })
                
                    save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
                    
                    st.session_state.start_time = time.time()
                    st.session_state.step = "human_ai1"
                    st.rerun()
             

    
    
