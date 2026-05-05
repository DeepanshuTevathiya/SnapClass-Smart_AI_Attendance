import streamlit as st
from src.Database.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write('Enter the details of new subject')
    sub_id = st.text_input('Subject Code', placeholder='e.g CSC102J')
    sub_name = st.text_input('Subject Name', placeholder='e.g Database Management System')
    sub_sec = st.text_input('Section', placeholder='e.g DS-A')

    if st.button('Create Subject Now', type='primary'):
        if sub_id and sub_name and sub_sec:
            try:
                create_subject(sub_id, sub_name, sub_sec, teacher_id)
                st.toast('Subject_Created_Sucessfully')
                st.rerun()
            except Exception as e:
                st.error(f'Error {str(e)}')
        else:
            st.warning('Please Fill all fields!')