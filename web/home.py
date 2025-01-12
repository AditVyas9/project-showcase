import streamlit as st
import pandas as ps

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("web/images/photo.png")

with col2:
    st.title("Adit Vyas")
    content = """
    I am student of class 8, and a HTML & Python developer
    """
    st.info(content)

content2 = """
Below there are few apps I build. Feel free to contact me!
"""
st.write(content2)

col3, empty, col4 = st.columns([1.5, 0.5, 1.5])

df = ps.read_csv("web/data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("web/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")





with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("web/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
