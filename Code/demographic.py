import streamlit as st
import time
from data_handler import save_responses
import uuid

def gender():
    if "responses" not in st.session_state:
        st.session_state.responses = {}         
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    st.title("Demographic Section")
    st.markdown("##### Just a few quick questions about you! #####")
    st.markdown("---")
    st.markdown('''<div style="font-size: 20px">
                What is your gender?
                </div>''', unsafe_allow_html=True)
    selected_choice = st.radio("", ["Male", "Female", "Other"], index=None)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if selected_choice is None:
            st.button("Next", disabled=True)
        else:
            if st.button("Next"):
                    end_time = time.time()
                    time_spent = round(end_time - st.session_state.start_time, 2)
                
                    st.session_state.gender_response = selected_choice
                    st.session_state.gender_time = time_spent
                    
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
                    )
                    
                    total_time = round(total_time, 2)  
                    
                    if "participant_id" not in st.session_state:
                        st.session_state.participant_id = str(uuid.uuid4())
                    st.session_state.responses.update({
                        "participant_id": st.session_state.participant_id,
                        "Gender Time": st.session_state.get("gender_time"),
                        "Gender Response": selected_choice,
                        "total_time": total_time
                    })

                    save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
                
                    st.session_state.start_time = time.time()
                    st.session_state.step = "age"
                    st.rerun()
            

def age():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    st.title("Demographic Section")
    st.markdown("---")
    #st.markdown("### How old are you? ###")
    st.markdown('''<div style="font-size: 20px">
                How old are you?
                </div>''', unsafe_allow_html=True)
    selected_age = st.radio("",
                            ["18-24 years old", "25-34 years old", "35-44 years old", "45-54 years old", "55-64 years old", "+65 years old"],
                            index=None)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if selected_age is None:
            st.button("Next", disabled=True)
        else:
            if st.button("Next"):
                    end_time = time.time()
                    time_spent = round(end_time - st.session_state.start_time, 2)
                    st.session_state.age_response = selected_age
                    st.session_state.age_time = time_spent
                    
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
                    )
                    
                    total_time = round(total_time, 2)  
                    
                    if "participant_id" not in st.session_state:
                        st.session_state.participant_id = str(uuid.uuid4())
                    st.session_state.responses.update({
                        "participant_id": st.session_state.participant_id,
                        "Age Time": st.session_state.get("age_time"),
                        "Age Response": selected_age,
                        "total_time": total_time
                    })
                
                    save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
                    
                    st.session_state.start_time = time.time()
                    st.session_state.step = "ethnic"
                    st.rerun()
            
        
def ethnic():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    st.title("Demographic Section")
    st.markdown("---")
    #st.markdown("### What is your ethnic background? ###")
    st.markdown('''<div style="font-size: 20px">
                What is your ethnic background?
                </div>''', unsafe_allow_html=True)
    selected_ethnic = st.multiselect("",
                            ["White", "Black or African American", "Asian", "Native Hawaiian or Pacific Islander", "Hispanic or Latino", "other"],
                            placeholder="Select one or more options")
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if not selected_ethnic:
            st.button("Next", disabled=True)
        else:
            if st.button("Next"):
                    end_time = time.time()
                    time_spent = round(end_time - st.session_state.start_time, 2)
                    st.session_state.ethnic_response = selected_ethnic
                    st.session_state.ethnic_time = time_spent
                    
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
                    )
                    
                    total_time = round(total_time, 2)  
                    
                    if "participant_id" not in st.session_state:
                            st.session_state.participant_id = str(uuid.uuid4())
                    st.session_state.responses.update({
                        "participant_id": st.session_state.participant_id,
                        "Ethnic Time": st.session_state.get("ethnic_time"),
                        "Ethnic Response": selected_ethnic,
                        "total_time": total_time
                    })
                
                    save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
                    
                    st.session_state.start_time = time.time()
                    st.session_state.step = "education"
                    st.rerun()
            
        
def education():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    st.title("Demographic Section")
    st.markdown("---")
    #st.markdown("### What is your highest level of education you have completed? ###")
    st.markdown('''<div style="font-size: 20px">
               What is your highest level of education you have completed?
                </div>''', unsafe_allow_html=True)
    selected_education = st.radio("",
                            ["Primary School or lower", "Secondary School", "Bachelor's Degree", "Advanced Degree (Master's, Doctorate. etc.)"],
                            index=None)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if selected_education is None:
            st.button("Next", disabled=True)
        else:
            if st.button("Next"):
                    end_time = time.time()
                    time_spent = round(end_time - st.session_state.start_time, 2)
                    st.session_state.education_response = selected_education
                    st.session_state.education_time = time_spent
                    
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
                    )
                    
                    total_time = round(total_time, 2)  
                    
                    if "participant_id" not in st.session_state:
                            st.session_state.participant_id = str(uuid.uuid4())
                    st.session_state.responses.update({
                        "participant_id": st.session_state.participant_id,
                        "Education Time": st.session_state.get("education_time"),
                        "Education Response": selected_education,
                        "total_time": total_time
                    })
                
                    save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
                    
                    st.session_state.start_time = time.time()
                    st.session_state.step = "presurvey_run"
                    st.rerun()
                    


        



    
    
