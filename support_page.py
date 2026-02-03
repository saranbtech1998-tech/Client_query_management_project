import streamlit as st
import pandas as pd
from datetime import datetime
from db import get_connection

def support_page():
    st.header("Support Team Dashboard")

    conn = get_connection()
    df = pd.read_sql("SELECT * FROM client_queries ORDER BY query_id DESC", conn)
    conn.close()

    st.dataframe(df)

    query_id = st.number_input("Enter Query ID to Close", min_value=1)

    if st.button("Close Query"):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE client_queries
            SET status='Closed',
                query_closed_time=%s
            WHERE query_id=%s
        """, (datetime.now(), query_id))

        conn.commit()
        conn.close()

        st.success("Query closed successfully")
