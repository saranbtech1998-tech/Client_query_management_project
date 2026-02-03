import pandas as pd
from db import get_connection

df = pd.read_csv("synthetic_client_queries.csv")

# Convert date columns to datetime
df["date_raised"] = pd.to_datetime(df["date_raised"], errors="coerce")
df["date_closed"] = pd.to_datetime(df["date_closed"], errors="coerce")

conn = get_connection()
cur = conn.cursor()

for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO client_queries
        (mail_id, mobile_number, query_heading, query_description,
         status, query_created_time, query_closed_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        row["client_email"],
        row["client_mobile"],
        row["query_heading"],
        row["query_description"],
        row["status"],
        row["date_raised"],
        row["date_closed"] if pd.notna(row["date_closed"]) else None
    ))

conn.commit()
conn.close()

print("CSV data loaded successfully (empty handled)")
