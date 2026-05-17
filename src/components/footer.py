import streamlit as st

def footer_home():

    st.markdown(f"""                
        <div style="margin-top: 2rem; display: flex; gap: 6px; justify-content: center; align-items: center;">
            <p style='font-weight: bold; color: white; margin: 0;'>Created with ♥️ by
                <span style="font-weight: 800; font-size: 17px; margin-left: 4px">
                    Deepanshu Tevathiya 
                </span>
            </p>

        </div>
                """, unsafe_allow_html=True)

def footer_dashboard():
    
    st.markdown(f"""                
        <div style="margin-top: 2rem; display: flex; gap: 6px; justify-content: center; align-items: center;">
            <p style='font-weight: bold; color: black; margin: 0;'>Created with ♥️ by
                <span style="font-weight: 800; font-size: 17px; margin-left: 4px">
                    Deepanshu Tevathiya 
                </span>
            </p>
        </div>
                """, unsafe_allow_html=True)