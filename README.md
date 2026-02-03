# Client Query Management System #

# Project Overview
This project is a Client Query Management System built using Python, PostgreSQL, and Streamlit.  
It allows clients to raise support queries and enables the support team to track and close them through an interactive dashboard.


# Tech Stack
Python
PostgreSQL
Streamlit
Pandas
psycopg2



# Project Structure
client_querie_Project/
│
├── app.py # Main Streamlit controller
├── db.py # Database connection
├── load_csv.py # CSV to DB loader (Extract–Transform–Load)
├── client_page.py # Client submission page
├── support_page.py # Support team dashboard
├── synthetic_client_queries.csv
├── requirements.txt
└── README.md

# Database Schema

Table Name: `client_queries`

CREATE TABLE Client_queries (
    query_id SERIAL PRIMARY KEY,
    mail_id VARCHAR(100),
    mobile_number VARCHAR(15),
    query_heading VARCHAR(200),
    query_description TEXT,
    status VARCHAR(10),
    query_created_time TIMESTAMP,
    query_closed_time TIMESTAMP
);


# ETL Process (CSV Loading)

 GUVI provided a synthetic CSV file
 CSV data is read using Pandas
 Column names are mapped to database schema
 Missing values are handled (empty → NULL)
 Cleaned data is inserted into PostgreSQL using cursor-based SQL


# Streamlit Application #

# Client Submission Page
 Allows clients to raise new queries
 Stores data in database with status "Opened"

# Support Team Dashboard
 Displays all queries
 Allows support team to close queries
 Updates status and closed timestamp


#  How to Run the Project
bash
streamlit run app.py

# 1. Install dependencies
bash
pip install -r requirements.txt
