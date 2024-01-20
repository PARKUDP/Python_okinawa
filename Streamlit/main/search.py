import streamlit as st
import urllib.request as urllib2
import json
import pandas as pd

# ユーザーの入力を受け取る
user_input = st.text_input("検索", "")

# 検索ボタン
if st.button('検索'):
    # APIからデータを取得
    resource = 'e0d8ac3b-a4f3-43ec-9d31-604fdf2c5677'
    response = urllib2.urlopen(f'https://data.bodik.jp/api/3/action/datastore_search?resource_id={resource}')
    data = json.loads(response.read()).get('result').get('records')

    # pandas DataFrameに変換
    df = pd.DataFrame(data)
    
    # ユーザーの入力に基づいてデータをフィルタリング
    if user_input:
        filtered_df = df[df['名称'].str.contains(user_input)]
    else:
        filtered_df = df

    # データを表示（名称、住所、緯度、経度のみ）
    st.dataframe(filtered_df[['名称', '住所', '緯度', '経度']], 1000, 450)