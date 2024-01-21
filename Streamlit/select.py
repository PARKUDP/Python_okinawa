import streamlit as st

option = st.selectbox(
    '次の中で好きなものを選んでください',
    ('りんご', 'スイカ', 'バナナ'))

st.write('あなたが選んだもの:', option)