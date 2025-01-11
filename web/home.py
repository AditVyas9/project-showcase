import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("web/images/photo.png")

with col2:
    st.title("Adit Vyas")
    content = """
    I am student of class 8, and a HTML & Python developer
    """
    st.write(content)