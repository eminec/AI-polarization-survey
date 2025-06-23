import streamlit as st
import time
from data_handler import save_responses
import uuid


def run():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    st.title("Informed Consent")
    st.markdown("---")
    st.markdown("#### Please read the following information carefully before proceeding!")
    st.markdown('''<div style="font-size: 18px">
                <h4>Purpose and Procedure</h4>
                You are invited to participate in a research study on <strong>human-AI interaction</strong>. Your participation is <strong>completely voluntary</strong>
                and you may stop at any time without facing any penalties.<br>
                This study includes a brief <strong>Pre-Survey</strong> to determine eligibility. Not all participants will meet the criteria to proceed to the full study. 
                After the Pre-Survey, you will be asked to answer a few <strong>sociodemographic questions</strong>. Afterwards you will engage in an <strong>interactive session with an AI</strong>, followed by a <strong>Post-Survey</strong>.<br>
                While you may not directly benefit, your participation will contribute to <strong>important research on human-AI interaction</strong>.<br><br>
                <h4>Confidentiality</h4>
                All responses will be kept <strong>confidential</strong> and analyzed in aggregate form. No personal information such as name, email adresses will be collected.<br><br>
                <h4>Storage of Data</h4>
                The collected data will be <strong>anonymized</strong> and may be transferred to <strong>scientific repositories or databases</strong>.
                In this case, the data will be <strong>publicly accessible</strong> but will be processed in a way that prevents any identification of participants.<br><br>
                <h4>Right to Withdraw</h4>
                Participation is <strong>entirely voluntary</strong>. You may stop at any point without penalty or loss of benefits. Simply close the window or choose 'I Disagree' to exit the study.<br><br>
                <h4>Questions or Concerns</h4>
                If you have any questions or concerns about the study, please contact: Emine.Celik@campus.lmu.de<br><br>  
                By clicking <strong>'I Agree'</strong>, you confirm that:
                <ul>
                    <li>You are at least <strong>18 years old</strong></li>
                    <li>You have read and understood the above information</li>
                    <li>You voluntarily agree to participate in this study</li>
                </ul>
                </div>''', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([3,5,2])
    with col3:
        st.markdown('<div style="text-align: left;">', unsafe_allow_html=True)
        if st.button("I Agree", use_container_width=True):
            end_time = time.time()
            time_spent = round(end_time - st.session_state.start_time, 2)
            st.session_state.informed_agree_time = time_spent
            
            total_time = (
                st.session_state.get("first_page_time", 0)
                + st.session_state.get("informed_agree_time", 0)
            )
            
            total_time = round(total_time, 2)  

            if "participant_id" not in st.session_state:
                    st.session_state.participant_id = str(uuid.uuid4())
            st.session_state.responses.update({
                "participant_id": st.session_state.participant_id,
                "Informed Agree Time": st.session_state.get("informed_agree_time"),
                "total_time": total_time
            })
            
            save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
            
            
            st.session_state.start_time = time.time()
            st.session_state.step = "presurvey_polarization1"
            st.rerun()
        
    col1, col2, col3 = st.columns([3,5,2])
    with col3:        
        if st.button("I Disagree", use_container_width=True):
            end_time = time.time()
            time_spent = round(end_time - st.session_state.start_time, 2)
            st.session_state.informed_disagree_time = time_spent
            
            total_time = (
                st.session_state.get("first_page_time", 0)
                + st.session_state.get("informed_agree_time", 0)
                + st.session_state.get("informed_disagree_time", 0)
            )
            
            total_time = round(total_time, 2)  
            
            if "participant_id" not in st.session_state:
                st.session_state.participant_id = str(uuid.uuid4())
            st.session_state.responses.update({
                "participant_id": st.session_state.participant_id,
                "Informed Disagree Time": st.session_state.get("informed_disagree_time"),
                "total_time": total_time
            })
            
            save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
            
            st.session_state.start_time = time.time()
            st.session_state.step = "end_survey_page"
            st.rerun()
        
        

 

            

    
