import streamlit as st

st.button("削除", type="primary")
if st.button('挨拶する'):
    st.write('はじめまして')
else:
    st.write('バイバイ')