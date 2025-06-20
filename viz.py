import streamlit as st
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_patient_info(case_id):

    connection = psycopg2.connect(
        dbname='postgres',
        user=os.getenv('DB_ADMIN_NAME'),
        password=os.getenv('DB_ADMIN_PASSWORD'),
        host='clinical.cwpmisqy4ng3.us-east-1.rds.amazonaws.com',
        port=5432
    )
    
    cursor = connection.cursor()
    
    query = """
    SELECT *
    FROM information_schema.columns
    WHERE table_name = 'clinical'
    """
    
    cursor.execute(query, (case_id,))
    result = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    return result

st.title("Patient Information Viewer")

case_id = st.text_input("Enter Case ID:", "")

if st.button("Get Patient Info"):
    if case_id:
        patient_info = get_patient_info(case_id)
        
        if patient_info:
            st.write("### Patient Information")
            columns = ["1", "2", "3", "4"]
            patient_dict = dict(zip(columns, patient_info))
            
            for column, value in patient_dict.items():
                st.write(f"**{column}:** {value}")
        else:
            st.error("No patient information found for this Case ID.")
    else:
        st.warning("Please enter a Case ID.")
