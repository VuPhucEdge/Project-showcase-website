import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Edge')
    content = """
    Hi, I am Edge! T am a Python programmer
    """
    st.info(content)
