import streamlit as st
from datetime import datetime
from db import get_connection

def client_page():
    st.header("Client Query Submission")

    email = st.text_input("Email ID")
    mobile = st.text_input("Mobile Number")
    heading = st.text_input("Query Heading")
    description = st.text_area("Query Description")

    if st.button("Submit Query"):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO client_queries
            (mail_id, mobile_number, query_heading, query_description,
             status, query_created_time)
            VALUES (%s,%s,%s,%s,'Opened',%s)
        """, (email, mobile, heading, description, datetime.now()))

        conn.commit()
        conn.close()

        st.success("Query submitted successfully")
