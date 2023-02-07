import streamlit as st
import pandas as p

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/me.png", width=400)

with col2:
    st.title('Victor Jefferson')
    content = ''' insert about me
    '''
    st.info(content)
content = "Below you can find some of the apps I've built with Python, feel free to contact me."
st.write(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = p.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")