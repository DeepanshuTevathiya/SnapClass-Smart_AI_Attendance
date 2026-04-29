import streamlit as st
from src.ui.base_layout import style_background_dashboard,  style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()



def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type="secondary", key="loginbckbtn", shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()
    
    st.header("Login using password", text_alignment="center")
    st.space()
    st.space()

    teacher_username = st.text_input("Enter username", placeholder='@ravi sharma')
    teacher_pass = st.text_input("Enter your password", placeholder='Enter your password', type="password")

    st.divider()

    btnc1, btnc2 = st.columns(2,vertical_alignment="center")
    with btnc1:
        st.button("Login Here", type="secondary", shortcut="control+enter", icon=":material/passkey:", icon_position="left", use_container_width=True)
    
    with btnc2:
        if st.button("Register Instead", type="primary", icon=":material/passkey:", icon_position="left", use_container_width=True):
            st.session_state.teacher_login_type = "register"
            st.rerun()
            

    footer_dashboard()



def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type="secondary", key="loginbckbtn", shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()
    
    st.header("Register Your Teacher Profile")
    st.space()
    st.space()

    teacher_username = st.text_input("Enter username", placeholder='@ravi sharma')
    teacher_name = st.text_input("Enter your name", placeholder='Ravi Sharma')
    teacher_pass = st.text_input("Enter your password", placeholder='Enter your password', type="password")
    teacher_pass_confirm = st.text_input("Confirm password", placeholder="Confirm password", type="password")

    st.divider()

    btnc1, btnc2 = st.columns(2,vertical_alignment="center")
    with btnc1:
        st.button("Register Now", type="primary", shortcut="control+enter" ,icon=":material/passkey:", icon_position="left", use_container_width=True)

    with btnc2:
        if st.button("Login Instead", type="secondary", icon=":material/passkey:", icon_position="left", use_container_width=True):
            st.session_state.teacher_login_type = "login"
            st.rerun()
    
            

    footer_dashboard()