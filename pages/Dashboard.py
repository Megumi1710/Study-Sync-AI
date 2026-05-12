import streamlit as st


def show_dashboard():

    # Page Title
    st.title("📊 Dashboard")

    st.subheader("Welcome back!")

    # Create 3 columns
    col1, col2, col3 = st.columns(3)

    # Metric Cards
    with col1:
        st.metric("Study Hours", "12")

    with col2:
        st.metric("Attendance", "92%")

    with col3:
        st.metric("Streak", "5 Days")

    # Divider
    st.divider()

    # Recent Activity
    st.subheader("Recent Activity")

    st.write("✅ Studied Physics for 2 hours")
    st.write("✅ Completed Math assignment")
    st.write("✅ Revised Chemistry notes")
