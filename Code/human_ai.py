import streamlit as st
import requests
import time
from data_handler import save_responses
import uuid
import os
#from dotenv import load_dotenv


#load_dotenv()

#only for local testing
#API_KEY = os.getenv("API_KEY")
#API_URL = os.getenv("API_URL")

api_key = st.secrets["api_key"]
api_url = st.secrets["api_url"]

def human_ai1():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    st.title("Welcome to the Human-AI Conversation!")
    st.markdown("---")
    st.markdown('''<div style="font-size: 20px">
                You will be now participating in a <strong>conversation with an AI</strong> about a topic where you previously expressed a strong opinion.
                The topic was selected randomly.<br><br>
                The purpose of this dialogue is to see <strong>how humans and AI can engage around complicated topics</strong>.<br><br>
                Please be open and honest in your responses and remember that the AI is <strong>non-judgemental</strong>. Your participation is <strong>confidential</strong>.<br>
                Thank you for contributing to this study on human-AI interaction.
                </div>''', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if st.button("Next"):
            end_time = time.time()
            time_spent = round(end_time - st.session_state.start_time, 2)

            st.session_state.human_ai1_time = time_spent
            
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
                + st.session_state.get("gender_time", 0)
                + st.session_state.get("age_time", 0)
                + st.session_state.get("ethnic_time", 0)
                + st.session_state.get("education_time", 0)
                + st.session_state.get("presurvey_ai0_time", 0)
                + st.session_state.get("presurvey_ai1_time", 0)
                + st.session_state.get("presurvey_ai2_time", 0)
                + st.session_state.get("human_ai1_time", 0)
                )
                
            total_time = round(total_time, 2)
            
            if "participant_id" not in st.session_state:
                    st.session_state.participant_id = str(uuid.uuid4())
            st.session_state.responses.update({
                "participant_id": st.session_state.participant_id,
                "Human_ai1 Time": st.session_state.get("human_ai1_time"),
                "total_time": total_time
                })
                
            save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
            
            st.session_state.start_time = time.time()
            st.session_state.step = "human_ai_evidence"
            st.rerun()
        
        
def human_ai_evidence():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    st.title("Human-AI Conversation")
    st.markdown("---")
    topics = st.session_state.get("topics")
    
    for topic in topics:
        topic["strength"] = abs(topic["value"] - 50)
    
    topic = st.session_state.highRatedTopic
    
    st.markdown('''<div style="font-size: 20px">
                Previously, you mentioned that you have a strong opinion about:<br><br>
                </div>''', unsafe_allow_html=True)
    st.write("\n\n",
            "' ", f"**{topic['label']}**", " '\n\n"
             "\n\n")
    st.markdown('''<div style="font-size: 20px">
                Can you <strong>explain</strong> why you feel this way?<br>
                Do you have in <strong>specific evidence or events</strong> that initially led you to believe strongly in this topic?
                </div>''', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div>Please write your answer below. Press <strong>Enter</strong> to confirm.</div>", unsafe_allow_html=True)
    st.session_state.inputDetail = st.text_input("")
    inputUser = st.session_state.inputDetail
    
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if not inputUser:
            st.button("Next", disabled=True)
        else:
            if st.button("Next"):
                    end_time = time.time()
                    time_spent = round(end_time - st.session_state.start_time, 2)
                    st.session_state.human_ai2_response = inputUser
                    st.session_state.human_ai2_time = time_spent
                    
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
                        + st.session_state.get("gender_time", 0)
                        + st.session_state.get("age_time", 0)
                        + st.session_state.get("ethnic_time", 0)
                        + st.session_state.get("education_time", 0)
                        + st.session_state.get("presurvey_ai0_time", 0)
                        + st.session_state.get("presurvey_ai1_time", 0)
                        + st.session_state.get("presurvey_ai2_time", 0)
                        + st.session_state.get("human_ai1_time", 0)
                        + st.session_state.get("human_ai2_time", 0)
                    )
                    
                    total_time = round(total_time, 2)
                    
                    if "participant_id" not in st.session_state:
                        st.session_state.participant_id = str(uuid.uuid4())
                    st.session_state.responses.update({
                        "participant_id": st.session_state.participant_id,
                        "Human_ai2 Time": st.session_state.get("human_ai2_time"),
                        "Human_ai2 Response": st.session_state.get("human_ai2_response"),
                        "total_time": total_time
                        })
                    
                    save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
                    
                    st.session_state.start_time = time.time()
                    st.session_state.step = "human_ai4"
                    st.rerun()                  
        
        
def human_ai4():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    topic = st.session_state.get("highRatedTopic")
    st.title("Human-AI Conversation")
    st.markdown("---")
    st.markdown('''<div style="font-size: 20px">
                You will now be participating in a conversation with an AI about your views and experiences with:<br><br>
                </div>''', unsafe_allow_html=True)
    st.write("\n\n",
             "' ", f"**{topic['label']}**", " '"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if st.button("Next"):
            end_time = time.time()
            time_spent = round(end_time - st.session_state.start_time, 2)
            
            st.session_state.human_ai4_time = time_spent
            
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
                )
                
            total_time = round(total_time, 2)
            
            if "participant_id" not in st.session_state:
                    st.session_state.participant_id = str(uuid.uuid4())
            st.session_state.responses.update({
                "participant_id": st.session_state.participant_id,
                "Human_ai4 Time": st.session_state.get("human_ai4_time"),
                "total_time": total_time
                })
                
            save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
            
            st.session_state.start_time = time.time()
            st.session_state.step = "human_ai5"
            st.rerun()
                   
        
def human_ai5():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    st.title("Human-AI Conversation")
    st.markdown("---")
    topic = st.session_state.get("highRatedTopic")
    inputUser = st.session_state.get("inputDetail")
    selected_value = st.session_state.get("selected_value_for_prompt")
    prompt = (
        f"You're speaking with someone who feels {selected_value}% agreement with the following statement:\n\n"
        f"{topic['label']}\n\n"
        "The participant explained their view as follows:\n\n"
        f"{inputUser}\n\n"
        "Now respond like a thoughtful and empathetic conversation partner in a natural and friendly tone."
        "Speak naturally, as if you're having a respectful dialogue."
        "Avoid breaking down the responses into steps and keep the conversation flowing as if two people are discussing a topic."
        "Respond from a different perspective."
        "Encourage understanding and gently offer alternative viewpoints."
        "Focus on shared values and bridge the divide."
        "Keep your response between 100-150 words. Do not include this instruction to your reply. Only return your final response.")
    
    if "ai3_generated" not in st.session_state:
        st.session_state.ai3_generated = False
    
    if not st.session_state.ai3_generated:
        #if st.button("🤖 Generate AI Response"):
        with st.spinner("Thinking..."):
            data = {
                "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 400,
                "temperature": 0.7
                }
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }
                
            response = requests.post(api_url, json=data, headers=headers)
                    
            if response.status_code == 200:
                ai_response = response.json()
                response_text = ai_response["choices"][0]["message"]["content"].strip()
                
                if response_text.startswith("1/1"):
                    response_text = response_text.split("\n", 1)[-1].strip()
                st.session_state.response_text = response_text
                st.session_state.ai3_generated = True
                st.rerun() 
            else:
                if response.status_code != 200:
                    st.write(response.status_code, response.text)
                st.error("Error")
                return None
    
    if "response_text" in st.session_state:
        st.markdown("### 🤖 AI response:\n\n")
        st.write(st.session_state.response_text)
        
    st.markdown("<br><br>", unsafe_allow_html=True)    
    st.markdown("<div>Please write your answer below. Press <strong>Enter</strong> to confirm.</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    response_user1 = st.text_input("Your opinion: ")
    st.session_state.response_user1 = response_user1
    
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if not response_user1:
            st.button("Next", disabled=True)
        else:
            if st.button("Next"):
                    end_time = time.time()
                    time_spent = round(end_time - st.session_state.start_time, 2)
                    
                    st.session_state.human_ai5_response = response_user1
                    st.session_state.human_ai5_time = time_spent
                    
                    
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
                    )
                    
                    total_time = round(total_time, 2)
                    
                    if "participant_id" not in st.session_state:
                        st.session_state.participant_id = str(uuid.uuid4())
                    st.session_state.responses.update({
                        "participant_id": st.session_state.participant_id,
                        "Human_ai5 Time": st.session_state.get("human_ai5_time"),
                        "Human_ai5 Response": st.session_state.get("human_ai5_response"),
                        "ai_response1": st.session_state.get("response_text"),
                        "total_time": total_time
                        })
                        
                    save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
                    
                    st.session_state.start_time = time.time()
                    st.session_state.step = "human_ai6"
                    st.rerun()
             
 


def human_ai6():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    response_text = st.session_state.get("response_text")
    response_user1 = st.session_state.get("response_user1")
    selected_value = st.session_state.get("selected_value_for_prompt")
    st.title("Human-AI Conversation")
    st.markdown("---")
    #st.write("🤖 AI response:\n\n")
    topic = st.session_state.get("highRatedTopic")
    inputUser = st.session_state.get("inputDetail")
    prompt = (
        f"You're speaking with someone who feels {selected_value}% agreement with the following statement:\n\n"
        f"{topic['label']}\n\n"
        "The participant explained their view as follows:\n\n"
        f"{response_user1}\n\n"
        "Now respond like a thoughtful and empathetic conversation partner in a natural and friendly tone."
        "Speak naturally, as if you're having a respectful dialogue."
        "Avoid breaking down the responses into steps and keep the conversation flowing as if two people are discussing a topic."
        "Respond from a different perspective."
        "Encourage understanding and gently offer alternative viewpoints."
        "Focus on shared values and bridge the divide."
        "Keep your response between 100-150 words. Do not include this instruction to your reply. Only return your final response.")
    
    if "ai4_generated" not in st.session_state:
            st.session_state.ai4_generated = False
    
    if not st.session_state.ai4_generated:
        if st.button("🤖 Press the button to generate AI response"):
            with st.spinner("Thinking..."):
                data = {
                    "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 400,
                    "temperature": 0.7
                    }
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                }
                
                st.session_state.response_user1 = ""
                response = requests.post(api_url, json=data, headers=headers)
                    
                if response.status_code == 200:
                    ai_response = response.json()
                    response_text2 = ai_response["choices"][0]["message"]["content"].strip()
                    
                    if response_text2.startswith("1/1"):
                        response_text2 = response_text2.split("\n", 1)[-1].strip()
                    st.session_state.response_text2 = response_text2
                    st.session_state.ai4_generated = True
                    st.rerun() 
                    st.write(response_text2)
                else:
                    st.error("Error1")
                    return None
    
    if "response_text2" in st.session_state:
        st.markdown("### 🤖 AI response:\n\n")
        st.write(st.session_state.response_text2)
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown("<div>Please write your answer below. Press <strong>Enter</strong> to confirm.</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
        
    response_user2 = st.text_input("Your opinion: ", key="response_user2")
    
    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if not response_user2:
            st.button("Next", disabled=True)
        else:
            if st.button("Next"):
                    end_time = time.time()
                    time_spent = round(end_time - st.session_state.start_time, 2)
                    
                    st.session_state.human_ai6_response = response_user2
                    st.session_state.human_ai6_time = time_spent
                    
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
                    )
                    
                    total_time = round(total_time, 2)
                    
                    if "participant_id" not in st.session_state:
                        st.session_state.participant_id = str(uuid.uuid4())
                    st.session_state.responses.update({
                        "participant_id": st.session_state.participant_id,
                        "Human_ai6 Time": st.session_state.get("human_ai6_time"),
                        "Human_ai6 Response": st.session_state.get("human_ai6_response"),
                        "ai_response2": st.session_state.get("response_text2"),
                        "total_time": total_time
                        })
                        
                    save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
                    
                    st.session_state.start_time = time.time()
                    st.session_state.step = "human_ai7"
                    st.rerun() 
               
    
def human_ai7():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    response_text2 = st.session_state.get("response_text2")
    response_user2 = st.session_state.get("response_user2")
    selected_value = st.session_state.get("selected_value_for_prompt")
    st.title("Human-AI Conversation")
    st.markdown("---")
    #st.write("🤖 AI response:\n\n")
    topic = st.session_state.get("highRatedTopic")
    inputUser = st.session_state.get("inputDetail")
    prompt = (
        f"You're speaking with someone who feels {selected_value}% agreement with the following statement:\n\n"
        f"{topic['label']}\n\n"
        "The participant explained their view as follows:\n\n"
        f"{response_user2}\n\n"
        "Now respond like a thoughtful and empathetic conversation partner in a natural and friendly tone."
        "Speak naturally, as if you're having a respectful dialogue."
        "Avoid breaking down the responses into steps and keep the conversation flowing as if two people are discussing a topic."
        "Respond from a different perspective."
        "Encourage understanding and gently offer alternative viewpoints."
        "Focus on shared values and bridge the divide."
        "As you conclude the conversation, offer advice, a recommendation or a potential solution to move forward."
        "Keep your response between 100-150 words. Do not include this instruction to your reply. Only return your final response.")
    
        
    if "ai5_generated" not in st.session_state:
        st.session_state.ai5_generated = False
    
    if not st.session_state.ai5_generated:
        if st.button("🤖 Press the button to generate AI response"):
            with st.spinner("Thinking..."):
                data = {
                    "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 400,
                    "temperature": 0.7
                    }
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                }
        
        #st.session_state.response_user2 = ""
                response = requests.post(api_url, json=data, headers=headers)
        #st.write(response)
                if response.status_code == 200:
                    ai_response = response.json()
                    response_text3 = ai_response["choices"][0]["message"]["content"].strip()
                    
                    if response_text2.startswith("1/1"):
                        response_text2 = response_text2.split("\n", 1)[-1].strip()
                        
                    st.session_state.response_text3 = response_text3
                    st.session_state.ai5_generated = True
                    st.rerun() 
                    st.write(response_text3)
                else:
                    st.error(f"API returned: {response.status_code}: {response.text}")
                    #return None
            
    if "response_text3" in st.session_state:
        st.markdown("### 🤖 AI response:\n\n")
        st.write(st.session_state.response_text3)
        
    st.markdown("<br><br>", unsafe_allow_html=True)    
    st.markdown("<div>Please write your answer below. Press <strong>Enter</strong> to confirm.</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    response_user3 = st.text_input("Your opinion: ", key="response_user3")
    
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if not response_user3:
            st.button("Next", disabled=True)
        else:
            if st.button("Next"):
                    end_time = time.time()
                    time_spent = round(end_time - st.session_state.start_time, 2)
                    
                    st.session_state.human_ai7_response = response_user3
                    st.session_state.human_ai7_time = time_spent
                    
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
                    )
                    
                    total_time = round(total_time, 2)
                    
                    if "participant_id" not in st.session_state:
                        st.session_state.participant_id = str(uuid.uuid4())
                    st.session_state.responses.update({
                        "participant_id": st.session_state.participant_id,
                        "Human_ai7 Time": st.session_state.get("human_ai7_time"),
                        "Human_ai7 Response": st.session_state.get("human_ai7_response"),
                        "ai_response3": st.session_state.get("response_text3"),
                        "total_time": total_time
                        })
                        
                    save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
                    
                    st.session_state.start_time = time.time()
                    st.session_state.step = "post_survey1"
                    st.rerun()
            
