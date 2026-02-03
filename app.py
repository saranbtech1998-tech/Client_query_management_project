import streamlit as st
from client_page import client_page
from support_page import support_page

# App title
st.set_page_config(page_title="Client Query Management System", layout="wide")
st.title("Client Query Management System")

# Sidebar navigation
page = st.sidebar.selectbox(
    "Select Page",
    ["Client Submission Page", "Support Team Dashboard"]
)

# Page routing
if page == "Client Submission Page":
    client_page()
else:
    support_page()
