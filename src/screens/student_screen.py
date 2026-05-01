import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.Database.db import check_student_exist, create_student, student_login


def student_screen():

    style_background_dashboard()
    style_base_layout()

    student_screen_login()
    

def student_screen_login():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to home", type="secondary", shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()

    st.header("Login using face id", text_alignment="center")
    st.space()
    st.space()

    st.camera_input("Position your face in center")

    st.divider()
    footer_dashboard()
    