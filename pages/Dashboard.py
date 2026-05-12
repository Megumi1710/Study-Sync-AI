import streamlit as st
import pandas as pd

def show_Dashboard():

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
# Chart Section
st.subheader("📈 Study Analytics")

# Sample Data
data = {
    "Subject": ["Math", "Physics", "Chemistry", "English"],
    "Hours": [2, 3, 1, 2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set Subject as index
df = df.set_index("Subject")

# Display Bar Chart
st.bar_chart(df)
