import streamlit as st
from src.Database.config import supabase
from src.Database.db import enroll_student_in_subject
import time

@st.dialog("Enroll in Subjects")
def enroll_subject_dialog():
    st.write("Enter the code provide by your teacher")
    join_code = st.text_input("Enter the Subject Code", placeholder="Eg. CSE501J")

    if st.button("Enroll now", type="primary", width='stretch'):
        if join_code:
            res = supabase.table("subjects").select("subject_id, subject_name, subject_code").eq("subject_code", join_code).execute()
            if res.data:
                subject = res.data[0]
                student_id = st.session_state.student_data["student_id"]

                check = supabase.table("subject_student").select("*").eq("subject_id",subject["subject_id"]).eq("student_id",student_id).execute()
                if check.data:
                    st.warning("You are already enrolled in this program")
                else:
                    enroll_student_in_subject(subject["subject_id"], student_id)
                    st.success(f"Sucessfully Enrolled in {join_code}")
                    time.sleep(1)
                    st.rerun()
        else:
            st.error("Please Enter a Subject Code!") 