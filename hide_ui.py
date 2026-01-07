import streamlit as st

def hide_streamlit_ui():
    st.markdown("""
    <style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    a[href*="github.com"] {display: none !important;}
    [data-testid="stToolbar"] {display: none !important;}
    </style>
    """, unsafe_allow_html=True)
