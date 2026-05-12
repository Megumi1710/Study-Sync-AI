import streamlit as st

# Import dashboard function
from pages.dashboard import show_dashboard


# App configuration
st.set_page_config(
    page_title="StudySync AI",
    page_icon="📚",
    layout="wide"
)


# Sidebar
with st.sidebar:

    st.title("📚 StudySync AI")

    page = st.radio(
        "Navigation",
        ["Dashboard"]
    )


# Page Routing
if page == "Dashboard":
    show_dashboard()
