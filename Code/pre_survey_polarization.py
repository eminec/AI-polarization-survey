import streamlit as st
import random
import time
from data_handler import save_responses
import uuid

def presurvey_1():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    st.title(" Welcome to the Pre-Survey! ")
    st.markdown("---")
    st.markdown('''<div style="font-size: 20px">
                When there is a major news story, which news website would you visit <strong>first</strong>?
                </div>''', unsafe_allow_html=True)
    selected_value = st.radio("",
                            ["New York Times", "CNN.com", "FoxNews.com", "Google News", "NBC.com", "other"],
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
                    st.session_state.presurvey_polarization1_response = selected_value
                    st.session_state.presurvey_polarization1_time = time_spent
                    
                    total_time = (
                    st.session_state.get("first_page_time", 0)
                    + st.session_state.get("informed_agree_time", 0)
                    + st.session_state.get("informed_disagree_time", 0)
                    + st.session_state.get("presurvey_polarization1_time", 0)
                    )
                    
                    total_time = round(total_time, 2) 
                    
                    if "participant_id" not in st.session_state:
                        st.session_state.participant_id = str(uuid.uuid4())
                    st.session_state.responses.update({
                        "participant_id": st.session_state.participant_id,
                        "Presurvey Polarization1 Time": st.session_state.get("presurvey_polarization1_time"),
                        "Presurvey Polarization1 Response": st.session_state.get("presurvey_polarization1_response"),
                        "total_time": total_time
                        })
                
                    save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
                    
                    st.session_state.start_time = time.time()
                    st.session_state.step = "presurvey_polarization2"
                    st.rerun()
        
def presurvey_2():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
        
    if "first_visit2" not in st.session_state:
        st.session_state.first_visit2 = time.time()
        
    st.title("Pre-Survey")
    st.markdown("---")
    st.markdown('''<div style="font-size: 20px">
                <strong>How often</strong> do you engage in conversations with people who hold <strong>different political or social views</strong>?
                </div>''', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    selected_value = st.slider("", min_value=1, max_value=7, step=1, value=1, key="slider_page1")
    st.markdown("""
    <div style="display: flex; justify-content: space-between; margin-top: -130px;">
        <span style="width: 33%; text-align: left;">Never</span>
        <span style="width: 33%; text-align: center;">Sometimes</span>
        <span style="width: 33%; text-align: right;">Very Often</span>
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
    
    if selected_value == 1 and st.session_state.first_visit2:
        next_button_disabled = True        
    else:
        st.session_state.first_visit2 = False
        next_button_disabled=False
    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if st.button("Next", disabled=next_button_disabled):
            end_time = time.time()
            time_spent = round(end_time - st.session_state.start_time, 2)
            st.session_state.presurvey_polarization2_response = selected_value
            st.session_state.presurvey_polarization2_time = time_spent
            
            total_time = (
                st.session_state.get("first_page_time", 0)
                + st.session_state.get("informed_agree_time", 0)
                + st.session_state.get("informed_disagree_time", 0)
                + st.session_state.get("presurvey_polarization1_time", 0)
                + st.session_state.get("presurvey_polarization2_time", 0)
                )
                
            total_time = round(total_time, 2) 
                
            
            if "participant_id" not in st.session_state:
                st.session_state.participant_id = str(uuid.uuid4())
            st.session_state.responses.update({
                "participant_id": st.session_state.participant_id,
                "Presurvey Polarization2 Time": st.session_state.get("presurvey_polarization2_time"),
                "Presurvey Polarization2 Response": st.session_state.get("presurvey_polarization2_response"),
                "total_time": total_time
                })
            
            save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
            
            st.session_state.start_time = time.time()
            st.session_state.step = "presurvey_polarization3"
            st.rerun()
        
def presurvey_3():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
        
    if "first_visit3" not in st.session_state:
        st.session_state.first_visit3 = time.time()
        
    st.title("Pre-Survey")
    st.markdown("---")
    st.markdown('''<div style="font-size: 20px">
                If a person with an opposing stance on a political issue makes a logical argument, <strong>how likely</strong> are you to <strong>agree</strong> with them?
                </div>''', unsafe_allow_html=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    selected_value = st.slider("", min_value=1, max_value=7, value=1, step=1, key="slider_page2")
    st.markdown("""
    <div style="display: flex; justify-content: space-between; margin-top: -130px;">
        <span style="width: 33%; text-align: left;">Very <strong>unlikely</strong></span>
        <span style="width: 33%; text-align: center;">Neutral</span>
        <span style="width: 33%; text-align: right;">Very <strong>likely</strong></span>
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
    
    if selected_value == 1 and st.session_state.first_visit3:
        next_button_disabled = True        
    else:
        st.session_state.first_visit3 = False
        next_button_disabled=False
    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if st.button("Next", disabled=next_button_disabled):
            end_time = time.time()
            time_spent = round(end_time - st.session_state.start_time, 2)
            st.session_state.presurvey_polarization3_response = selected_value
            st.session_state.presurvey_polarization3_time = time_spent
            
            total_time = (
                st.session_state.get("first_page_time", 0)
                + st.session_state.get("informed_agree_time", 0)
                + st.session_state.get("informed_disagree_time", 0)
                + st.session_state.get("presurvey_polarization1_time", 0)
                + st.session_state.get("presurvey_polarization2_time", 0)
                + st.session_state.get("presurvey_polarization3_time", 0)
                )
                
            total_time = round(total_time, 2) 
            
            if "participant_id" not in st.session_state:
                st.session_state.participant_id = str(uuid.uuid4())
            st.session_state.responses.update({
                "participant_id": st.session_state.participant_id,
                "Presurvey Polarization3 Time": st.session_state.get("presurvey_polarization3_time"),
                "Presurvey Polarization3 Response": st.session_state.get("presurvey_polarization3_response"),
                "total_time": total_time
                })
            
            save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
            
            st.session_state.start_time = time.time()
            st.session_state.step = "presurvey_polarization4"
            st.rerun()
        
        
def presurvey_4():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
        
    if "first_visit4" not in st.session_state:
        st.session_state.first_visit4 = time.time()
        
    st.title("Pre-Survey")
    st.markdown("---")
    st.markdown('''<div style="font-size: 20px">
                On a scale from <strong>1 (strongly disagree) to 7 (strongly agree)</strong>, please indicate how much your agree or disagree with the following statement:
                </div>''', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('''<div style="font-size: 20px">
                "I respect people who have different political or social views than my own."
                </div>''', unsafe_allow_html=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    selected_value = st.slider("", min_value=1, max_value=7, value=1, step=1, key="slider_page4")
    st.markdown("""
    <div style="display: flex; justify-content: space-between; margin-top: -130px;">
        <span style="width: 33%; text-align: left;"><strong>Strongly<br>Disagree</strong></span>
        <span style="width: 33%; text-align: center;"><strong>Neutral</strong></span>
        <span style="width: 33%; text-align: right;"><strong>Strongly<br>Agree</strong></span>
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
    
    if selected_value == 1 and st.session_state.first_visit4:
        next_button_disabled = True        
    else:
        st.session_state.first_visit4 = False
        next_button_disabled=False
    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if st.button("Next", disabled=next_button_disabled):
            end_time = time.time()
            time_spent = round(end_time - st.session_state.start_time, 2)
            st.session_state.presurvey_polarization4_response = selected_value
            st.session_state.presurvey_polarization4_time = time_spent
            
            total_time = (
                st.session_state.get("first_page_time", 0)
                + st.session_state.get("informed_agree_time", 0)
                + st.session_state.get("informed_disagree_time", 0)
                + st.session_state.get("presurvey_polarization1_time", 0)
                + st.session_state.get("presurvey_polarization2_time", 0)
                + st.session_state.get("presurvey_polarization3_time", 0)
                + st.session_state.get("presurvey_polarization4_time", 0)
                )
                
            total_time = round(total_time, 2) 
            
            if "participant_id" not in st.session_state:
                st.session_state.participant_id = str(uuid.uuid4())
            st.session_state.responses.update({
                "participant_id": st.session_state.participant_id,
                "Presurvey Polarization4 Time": st.session_state.get("presurvey_polarization4_time"),
                "Presurvey Polarization4 Response": st.session_state.get("presurvey_polarization4_response"),
                "total_time": total_time
                })
            
            save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
            
            st.session_state.start_time = time.time()
            st.session_state.step = "presurvey_polarization5"
            st.rerun()
        

def presurvey_5():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
        
    if "first_visit5" not in st.session_state:
        st.session_state.first_visit5 = time.time()
        
    st.title("Pre-Survey")
    st.markdown("---")
    st.markdown('''<div style="font-size: 20px">
                On a scale from <strong>1 (strongly disagree) to 7 (strongly agree)</strong>, please indicate how much your agree or disagree with the following statement:
                </div>''', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('''<div style="font-size: 20px">
                "I feel angry when others disagree with my political or social views."
                </div>''', unsafe_allow_html=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    selected_value = st.slider("", min_value=1, max_value=7, value=1, step=1, key="slider_page5")
    st.markdown("""
    <div style="display: flex; justify-content: space-between; margin-top: -130px;">
        <span style="width: 33%; text-align: left;"><strong>Strongly<br>Disagree</strong></span>
        <span style="width: 33%; text-align: center;"><strong>Neutral</strong></span>
        <span style="width: 33%; text-align: right;"><strong>Strongly<br>Agree</strong></span>
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
    
    if selected_value == 1 and st.session_state.first_visit5:
        next_button_disabled = True        
    else:
        st.session_state.first_visit5 = False
        next_button_disabled=False
    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if st.button("Next", disabled=next_button_disabled):
            end_time = time.time()
            time_spent = round(end_time - st.session_state.start_time, 2)
            st.session_state.presurvey_polarization5_response = selected_value
            st.session_state.presurvey_polarization5_time = time_spent
            
            total_time = (
                st.session_state.get("first_page_time", 0)
                + st.session_state.get("informed_agree_time", 0)
                + st.session_state.get("informed_disagree_time", 0)
                + st.session_state.get("presurvey_polarization1_time", 0)
                + st.session_state.get("presurvey_polarization2_time", 0)
                + st.session_state.get("presurvey_polarization3_time", 0)
                + st.session_state.get("presurvey_polarization4_time", 0)
                + st.session_state.get("presurvey_polarization5_time", 0)
                )
                
            total_time = round(total_time, 2) 
            
            if "participant_id" not in st.session_state:
                st.session_state.participant_id = str(uuid.uuid4())
            st.session_state.responses.update({
                "participant_id": st.session_state.participant_id,
                "Presurvey Polarization5 Time": st.session_state.get("presurvey_polarization5_time"),
                "Presurvey Polarization5 Response": st.session_state.get("presurvey_polarization5_response"),
                "total_time": total_time
                })
            
            save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
            
            st.session_state.start_time = time.time()
            st.session_state.step = "presurvey_polarization6"
            st.rerun()
        
                        
def presurvey_6():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    st.title("Pre-Survey")
    st.markdown("---")
    st.markdown('''<div style="font-size: 20px">
                What <strong>political/social issue</strong> do you think divides people <strong>the most</strong>?
                </div>''', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
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
                    st.session_state.presurvey_polarization6_response = inputUser
                    st.session_state.presurvey_polarization6_time = time_spent
                    
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
                    )
                    
                    total_time = round(total_time, 2)
                    
                    if "participant_id" not in st.session_state:
                        st.session_state.participant_id = str(uuid.uuid4())
                    st.session_state.responses.update({
                        "participant_id": st.session_state.participant_id,
                        "Presurvey Polarization6 Time": st.session_state.get("presurvey_polarization6_time"),
                        "Presurvey Polarization6 Response": st.session_state.get("presurvey_polarization6_response"),
                        "total_time": total_time
                        })
                
                    save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
                    
                    st.session_state.start_time = time.time()
                    st.session_state.step = "presurvey_polarization7"
                    st.rerun()
            
        
        
def presurvey_7():
    if "responses" not in st.session_state:
        st.session_state.responses = {}      
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
        
    if "first_visit7" not in st.session_state:
        st.session_state.first_visit7 = True
        
    st.title("Pre-Survey")
    st.markdown("---")
    st.markdown('''<div style="font-size: 20px">
                On a scale from <strong>0% (strongly disagree) to 100% (strongly agree)</strong>, please indicate how much you agree or disagree with the following statements.
                Your responses will help us understand which topics matter most to you.
                Please answer honestly.
                </div>''', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.info("ℹ️ Please make sure to move every slider at least once before proceeding, even if you want to keep the value at 50%.")
    
    st.markdown("<br>", unsafe_allow_html=True)

    selected_value1 = st.slider("Human activity is the main cause of global warming.", min_value=0, max_value=100, value=50, step=10, format="%d%%")
    selected_value2 = st.slider("The U.S. benefits from immigration and should avoid extreme border restrictions.", min_value=0, max_value=100, value=50, step=10, format="%d%%")
    selected_value3 = st.slider("Gun laws should be stricter in the U.S.", min_value=0, max_value=100, value=50, step=10, format="%d%%")
    selected_value4 = st.slider("Replacing the federal income tax with tariffs is a fair way to fund the government.", min_value=0, max_value=100, value=50, step=10, format="%d%%")
    selected_value5 = st.slider("The 2024 U.S. election results were legitimate and trustworthy.", min_value=0, max_value=100, value=50, step=10, format="%d%%")
    selected_value6 = st.slider("AI will make human jobs obsolete and that’s a dangerous path.", min_value=0, max_value=100, value=50, step=10, format="%d%%")
    selected_value7 = st.slider("Health mandates like vaccines and lockdowns are sometimes necessary and justified.", min_value=0, max_value=100, value=50, step=10, format="%d%%")
    selected_value8 = st.slider("The U.S. foreign policy contributes to peace in the Middle East.", min_value=0, max_value=100, value=50, step=10, format="%d%%")
    selected_value9 = st.slider("'Woke' culture is essential for achieving true social justice.", min_value=0, max_value=100, value=50, step=10, format="%d%%")


    
    topics = [{"label": "Human activity is the main cause of global warming.", "value": selected_value1},
              {"label": "The U.S. benefits from immigration and should avoid extreme border restrictions.", "value": selected_value2},
              {"label": "Gun laws should be stricter in the U.S.", "value": selected_value3},
              {"label": "Replacing the federal income tax with tariffs is a fair way to fund the government.", "value": selected_value4},
              {"label": "The 2024 U.S. election results were legitimate and trustworthy.", "value": selected_value5},
              {"label": "AI will make human jobs obsolete and that’s a dangerous path.", "value": selected_value6},
              {"label": "Health mandates like vaccines and lockdowns are sometimes necessary and justified.", "value": selected_value7},
              {"label": "The U.S. foreign policy contributes to peace in the Middle East.", "value": selected_value8},
              {"label": "'Woke' culture is essential for achieving true social justice.", "value": selected_value9}]

    st.session_state.topics = topics
    topics = st.session_state.get("topics")
    for topic in topics:
        topic["strength"] = abs(topic["value"] - 50)
    
    sensitive_topics = [
        "Human activity is the main cause of global warming.",
        "The U.S. benefits from immigration and should avoid extreme border restrictions.",
        "Gun laws should be stricter in the U.S.",
        "The 2024 U.S. election results were legitimate and trustworthy.",
        "Health mandates like vaccines and lockdowns are sometimes necessary and justified.",
        "'Woke' culture is essential for achieving true social justice.",
    ] 
    
    neutral = []
    sensitive_non_mainstream = []
    
    for topic in topics:
        if topic["label"] in sensitive_topics:
            if topic["value"] < 50:
                sensitive_non_mainstream.append(topic)
        else:
            if topic["value"] != 50:
                neutral.append(topic)
    
    most_extreme_topics = neutral + sensitive_non_mainstream   

    isPolarized = len(most_extreme_topics) >= 1
    st.session_state.isPolarized = isPolarized
    if isPolarized:
        st.session_state.highRatedTopic = random.choice(most_extreme_topics)
        topic = st.session_state.highRatedTopic
    else:
        st.session_state.highRatedTopic = None
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    selected_values = [
        selected_value1, selected_value2, selected_value3,
        selected_value4, selected_value5, selected_value6,
        selected_value7, selected_value8, selected_value9
    ]
    
    if all(value != 50 for value in selected_values):
        st.session_state.first_visit7 = False
    
    all_selected = all(value is not None for value in selected_values)
    
    next_button_disabled = st.session_state.first_visit7 or not all_selected     
  
    col1, col2, col3 = st.columns([3,6,1])
    with col3:
        if st.button("Next", disabled=next_button_disabled):
            end_time = time.time()
            time_spent = round(end_time - st.session_state.start_time, 2)
            st.session_state.presurvey_polarization7_time = time_spent
            st.session_state.presurvey_polarization7_1_response = selected_value1
            st.session_state.presurvey_polarization7_2_response = selected_value2
            st.session_state.presurvey_polarization7_3_response = selected_value3        
            st.session_state.presurvey_polarization7_4_response = selected_value4
            st.session_state.presurvey_polarization7_5_response = selected_value5        
            st.session_state.presurvey_polarization7_6_response = selected_value6        
            st.session_state.presurvey_polarization7_7_response = selected_value7        
            st.session_state.presurvey_polarization7_8_response = selected_value8        
            st.session_state.presurvey_polarization7_9_response = selected_value9        
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
                )
                
            total_time = round(total_time, 2)
                
            if "participant_id" not in st.session_state:
                st.session_state.participant_id = str(uuid.uuid4())
            st.session_state.responses.update({
                "participant_id": st.session_state.participant_id,
                "Presurvey Polarization7 Time": st.session_state.get("presurvey_polarization7_time"),
                "climate_rating": st.session_state.get("presurvey_polarization7_1_response"),
                "immigration_rating": st.session_state.get("presurvey_polarization7_2_response"),
                "gunLaw_rating": st.session_state.get("presurvey_polarization7_3_response"),
                "tax_rating": st.session_state.get("presurvey_polarization7_4_response"),
                "election_rating": st.session_state.get("presurvey_polarization7_5_response"),
                "aiHumanJob_rating": st.session_state.get("presurvey_polarization7_6_response"),
                "healthMandates_rating": st.session_state.get("presurvey_polarization7_7_response"),
                "USMiddleEast_rating": st.session_state.get("presurvey_polarization7_8_response"),
                "wokeCulture_rating": st.session_state.get("presurvey_polarization7_9_response"),
                "total_time": total_time
                })
            
            save_responses(st.session_state.responses, s3=True, testing=False, followUp=False, backup=False)
            
            
            st.session_state.start_time = time.time()
            if(isPolarized):
                st.session_state.step = "attention"
            else:
                st.session_state.step = "end_survey_page"

            st.rerun()
        

        

    
