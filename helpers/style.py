import streamlit as st

# Local CSS
# Usage: Run local_css("helpers/style.css") to apply styles
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)