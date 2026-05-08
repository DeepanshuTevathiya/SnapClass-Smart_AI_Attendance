import streamlit as st
import time
from src.Database.config import supabase
from src.Database.db import enroll_student_in_subject

@st.dialog("Quick Enrollment")
def auto_enroll_dialog(subject_code):
    student_id = st.session_state.student_data["student_id"]

    response = supabase.table("subjects").select("subject_id","subject_name").eq("subject_code",subject_code).execute()
    if not response.data:
        st.error("Subject Not Found!")
        if st.button('Close'):
            st.query_params.clear()
            st.rerun()
    subject = response.data[0]

    check = supabase.table("subject_student").select("*").eq("subject_id", subject["subject_id"]).eq("student_id",student_id).execute()
    if check.data:
        st.warning("You are already enrolled!!")
        time.sleep(2)
        st.query_params.clear()
        st.rerun()
    st.markdown(f"Would you like to enroll in **{subject['subject_name']}**?")

    col1, col2 = st.columns(2)
    with col1:
        if st.button('No Thanks'):
            st.query_params.clear()
            st.rerun()
    with col2:
        if st.button("Yes Enroll Now!", width="stretch", type="primary"):
            enroll_student_in_subject(subject["subject_id"], student_id)
            st.success("Successfully Enrolled!")
            st.query_params.clear()
            time.sleep(1)
            st.rerun()
    
