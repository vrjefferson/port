import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/me.png", width=400)

with col2:
    st.title('Victor Jefferson')
    content = ''' insert about me
    '''
    st.info(content)