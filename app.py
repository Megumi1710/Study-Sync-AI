import streamlit as st 
st.set_page_config(page_title="Study Assist"
page_icon="😉😎💕"
layout="wide")
with st.sidebar:
  st.title("Study Assist Space")
page= st.radio("Navigation",["Dashboard","Study Tracker","Analytics","AI Assistance"])
if page== "Dashboard":
  st.title("Dashboard")
  st.subheader("Welcome Back!!!")
  st.columns(3)= col1, col2, col3
  with col1:
    st.metric("Study Hours", "12")
 with col2:
  st.metric("Attendence","87%")
  with col3:
    st.metric("Streak", "5 days")
    st.divider()
