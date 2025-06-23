import streamlit as st
import time
from data_handler import save_responses
import uuid
import requests
import os
#from dotenv import load_dotenv


#load_dotenv()

#only for local testing
#API_KEY = os.getenv("API_KEY")
#API_URL = os.getenv("API_URL")

api_key = st.secrets["api_key"]
api_url = st.secrets["api_url"]


def attention():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    ##st.title("Informed Consent")
    ##st.markdown("---")
    #st.markdown("#### Please read the following information carefully before proceeding!")
    task = st.markdown('''<div style="font-size: 18px">
                Before we begin we would like to learn more about your experiences with online surveys.<br>
                <strong>Why</strong> have you decided to take part in this survey?<br>
                Additionally, if you've participated in surveys before, could you share what <strong>your past experiences</strong> were like?<br>
                Please provide a <strong>few sentences</strong> to give us a clear understanding. 
                </div>''', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<div>Please write your answer below. Press <strong>Enter</strong> to confirm.</div>", unsafe_allow_html=True)
    
    inputUser = st.text_input("")
    
    
    prompt = (
        f"Task: {task}\n\n"
        f"Participant response: '{inputUser}' \n\n"
        "Your job is to strictly evaluate whether the participant is paying attention in this survey. "
        "Do NOT explain the task."
        " - If the response is too vague, off-topic, a placeholder like 'this is a test', or shows no understanding of the task, "
        "give it a low score (0-2).\n"
        "-If the response shows partial engagement, is somewhat related to the task, or reflects minimal effort, give it a mid score (3-9.\n)"
        "- If it engages with the task clearly and thoughtfully, give it a high score (8-10).\n "
        "- Do not give credit just because the sentence is gramatically correct.\n\n"
        "Respond ONLY in this format:\nScore: <number from 0 to 10>\nReason: <1-3 sentence explanation>"
        )
    

    if "attention_ai_generated" not in st.session_state:
        st.session_state.attention_ai_generated = False
    
    if not st.session_state.attention_ai_generated:
        #if st.button("🤖 Generate AI Response"):
        #with st.spinner("Thinking..."):
        data = {
            "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            "prompt": prompt
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
                
        
    #response_user_attention = st.text_input("Your opinion: ")
    #st.session_state.response_user1 = response_user_attention
    
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([3,6,1])
    with col3:            
        if not inputUser:
            st.button("Next", disabled=True)
        else:
            if st.button("Next"):
                    response_attention = requests.post(api_url, json=data, headers=headers)
                            
                    if response_attention.status_code == 200:
                        ai_response = response_attention.json()
                        print("API RESPONSE: ", ai_response)
                        response_text_attention = ai_response["choices"][0]["message"]["content"].strip()
                            
                        if response_text_attention.startswith("1/1"):
                            response_text_attention = response_text_attention.split("\n", 1)[-1].strip()
                        st.session_state.response_text_attention = response_text_attention
                        if "response_text_attention" in st.session_state:
                            print('Response about Attention rating: ' + response_text_attention)
                    else:
                        if response_attention.status_code != 200:
                            st.write(response_attention.status_code, response_attention.text)
                        st.error("Error")
                        return None
                    
                    
                    end_time = time.time()
                    time_spent = round(end_time - st.session_state.start_time, 2)
                    st.session_state.attention_response = inputUser
                    st.session_state.attention_time = time_spent
                    
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
                    )
                    
                    total_time = round(total_time, 2)
                    
                    if "participant_id" not in st.session_state:
                        st.session_state.participant_id = str(uuid.uuid4())
                    st.session_state.responses.update({
                        "participant_id": st.session_state.participant_id,
                        "Attention Check Time": st.session_state.get("attention_time"),
                        "Attention Check Response": st.session_state.get("attention_response"),
                        "Attention Check AI Response": st.session_state.get("response_text_attention"),
                        "total_time": total_time
                        })
                
                    save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
                    
                    st.session_state.start_time = time.time()
                    st.session_state.step = "gender"
                    st.rerun()
            
        
        

 

            

    
