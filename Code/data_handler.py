import streamlit as st
import pandas as pd
import os
from aws_utils import get_s3_client
from io import StringIO
from datetime import datetime

DATA_FILE = "responses.csv"

def save_responses(data: dict, testing=False, followUp=False, bucket_name="streamlitsurveybucket", s3=False, backup=False):
    if testing:
        data_file = "responses_test.csv"
    elif followUp:
        data_file = "responses_followUp.csv"
    else:
        data_file = "responses.csv"
    
    df_new = pd.DataFrame([data])
    if s3:
        s3_client = get_s3_client()
        try:
            response = s3_client.get_object(Bucket=bucket_name, Key=data_file)
            df = pd.read_csv(response['Body'])
        except s3_client.exceptions.NoSuchKey:
            df = pd.DataFrame()

        if "participant_id" in data and "participant_id" in df.columns:
            old_row = df[df["participant_id"] == data["participant_id"]]
            df = df[df["participant_id"] != data["participant_id"]]
            if not old_row.empty:
                updated_row = old_row.iloc[0].to_dict()
                updated_row.update(data)
                df_new = pd.DataFrame([updated_row])
                
        df = pd.concat([df, df_new], ignore_index=True)
            
    else:
        try:
            df = pd.read_csv(data_file)
            if "participant_id" in data and "participant_id" in df.columns:
                old_row = df[df["participant_id"] == data["participant_id"]]
                df = df[df["participant_id"] != data["participant_id"]]  
                if not old_row.empty:
                    updated_row = old_row.iloc[0].to_dict()
                    updated_row.update(data)
                    df_new = pd.DataFrame([updated_row])
            df = pd.concat([df, df_new], ignore_index=True)
        except Exception:
            df = df_new


    preferred_order = [
        "prolific_id",
        "participant_id",
        "timestamp",
        "First Page Time",
        
        "Informed Agree Time",
        "Informed Disagree Time",
        
        "Presurvey Polarization1 Time",
        "Presurvey Polarization1 Response",
        "Presurvey Polarization2 Time",
        "Presurvey Polarization2 Response",
        "Presurvey Polarization3 Time",
        "Presurvey Polarization3 Response",
        "Presurvey Polarization4 Time",
        "Presurvey Polarization4 Response",
        "Presurvey Polarization5 Time",
        "Presurvey Polarization5 Response",
        "Presurvey Polarization6 Time",
        "Presurvey Polarization6 Response",
        "Presurvey Polarization7 Time",
        "climate_rating",
        "immigration_rating",
        "gunLaw_rating",
        "tax_rating",
        "election_rating",
        "aiHumanJob_rating",
        "healthMandates_rating",
        "USMiddleEast_rating",
        "wokeCulture_rating",
        "Attention Check Time",
        "Attention Check Response",
        "Attention Check AI Response",
        
        "Demo First Page Time",
        "Gender Time",
        "Gender Response",
        "Age Time",
        "Age Response",
        "Ethnic Time",
        "Ethnic Response",
        "Education Time",
        "Education Response",
        
        "Presurvey_ai0 Time",
        "Presurvey_ai1 Time",
        "Presurvey_ai1 Response",
        "Presurvey_ai2 Time",
        "Presurvey_ai2 Response",
        
        "Human_ai1 Time",
        "Human_ai2 Time",
        "Human_ai2 Response",
        "Human_ai4 Time",
        "Human_ai5 Time",
        "ai_response1",
        "Human_ai5 Response",
        "Human_ai6 Time",
        "ai_response2",
        "Human_ai6 Response",
        "Human_ai7 Time",
        "ai_response3",
        "Human_ai7 Response",        
        
        "Postsurvey1 Time",
        "Postsurvey2 Time",
        "Postsurvey2 Response",
        "Postsurvey3 Time",
        "Postsurvey3 Response",
        
        "End of Survey Time",
        
    ]
    
    for col in preferred_order:
        if col not in df.columns:
            df[col] = None
            
    df = df[preferred_order + [col for col in df.columns if col not in preferred_order]]

    if s3:
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        s3_client.put_object(
            Bucket=bucket_name,
            Key=data_file,
            Body=csv_buffer.getvalue()
        )

    else:
        df.to_csv(data_file, index=False)
        
    if backup and "participant_id" in data:
        participant_id = data.get("participant_id") or df_new.get("participant_id", ["unknown"])[0]
        backup_key = f"backup_done_{participant_id}"
        if not st.session_state.get(backup_key, False):
            single_df = pd.DataFrame([data])
            for col in preferred_order:
                if col not in single_df.columns:
                    single_df[col] = None
            single_df = single_df[preferred_order + [col for col in single_df.columns if col not in preferred_order]]
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            backup_file = f"backups/{timestamp}_{participant_id}.csv"
        
            if s3:
                single_csv = StringIO()
                single_df.to_csv(single_csv, index=False)
                s3_client.put_object(
                    Bucket=bucket_name,
                    Key=backup_file,
                    Body=single_csv.getvalue()
                )
            else:
                os.makedirs("backups", exist_ok=True)
                single_df.to_csv(backup_file, index=False)
                
            st.session_state[backup_key] = True
            
    if s3:
        response = s3_client.get_object(Bucket=bucket_name, Key=data_file)
        df_all = pd.read_csv(response['Body'])
    else:
        df_all =pd.read_csv(data_file)
        
    completed = df_all["End of Survey Time"].notna().sum()
    total = len(df_all)
    incomplete = total - completed
    
    overview_df = pd.DataFrame([
        {"Status": "Completed", "Count": completed},
        {"Status": "Incomplete", "Count": incomplete},
        {"Status": "Total participants", "Count": total}
    ])
    
    overview_buffer = StringIO()
    overview_df.to_csv(overview_buffer, index=False)
    
    if s3:
        s3_client.put_object(
            Bucket=bucket_name,
            Key="responses_overview.csv",
            Body=overview_buffer.getvalue()
        )
    else:
        overview_df.to_csv("responses_overview.csv", index=False)  
        
        
        
        
