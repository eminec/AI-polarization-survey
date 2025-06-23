import streamlit as st
from data_handler import save_responses
import time
import uuid

def run():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    st.title("This is the End of the Survey!")
    st.markdown("---")
    st.markdown("\n\n #### Thank you for participating! #### ")
    
    isPolarized = st.session_state.get("isPolarized", False)
    if not isPolarized:
        st.markdown('''<div style="font-size: 20px">
                Based on your responses in the Pre-Survey, you do not meet the criteria to continue with the main study.<br>
                We thank you for your time and effort. 
                </div>''', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown('''<div style="font-size: 20px">
                <strong>Contact for questions:</strong><br>
                If you have any questions regarding this study, please feel free to contact <br>Emine Celik.<br>
                E-Mail: Emine.Celik@campus.lmu.de
                </div>''', unsafe_allow_html=True) 

    st.markdown("<br>", unsafe_allow_html=True)

    #only after 10-days follow up
    if isPolarized:
        #st.markdown('''<div style="font-size: 20px">
        #            The purpose of this research was to explore whether conversations with an emphatetic AI can
        #            reduce political polarization or encourage openness to other perspectives.<br>
        #            Please note that all your responses are anonymized and will only be used for academic research.<br><br>
        #            </div>''', unsafe_allow_html=True)
        st.markdown('''<div style="font-size: 20px">
                    <strong>Contact for questions:</strong><br>
                    If you have any questions regarding this study, please feel free to contact <br>Emine Celik.<br>
                    E-Mail: Emine.Celik@campus.lmu.de
                    </div>''', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([3,4,3])
    with col3:
        if st.button("Submit survey", use_container_width=True):
            
            st.success("Your responses were saved!")
            
            end_time = time.time()
            time_spent = round(end_time - st.session_state.start_time, 2)
            st.session_state.end_survey_time = time_spent
            
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
                + st.session_state.get("end_survey_time", 0)
                )
                
            total_time = round(total_time, 2)
            
            if "participant_id" not in st.session_state:
                    st.session_state.participant_id = str(uuid.uuid4())
            st.session_state.responses.update({
                "participant_id": st.session_state.participant_id,
                "End of Survey Time": st.session_state.get("end_survey_time"),
                "total_time": total_time
                })
            
            if not st.session_state.get("backup_done", False):
                save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=True)
                st.session_state["backup_done"] = True
            
    redirect_url = f"https://app.prolific.com/submissions/complete?cc=CYF4EC6G"     
    st.markdown(f'''<div style="font-size: 25px; text-align: center">
                <a href="{redirect_url}">
                Click here to return to Prolific and complete the study
                </a>
                </div>''', unsafe_allow_html=True)
                        
        


    
    
