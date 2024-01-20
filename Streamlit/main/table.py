import urllib.request as urllib2
import json
import streamlit as st 
import pandas as pd

# APIからデータを取得
resource = 'e0d8ac3b-a4f3-43ec-9d31-604fdf2c5677'
response = urllib2.urlopen(f'https://data.bodik.jp/api/3/action/datastore_search?resource_id={resource}')
datas = json.loads(response.read()).get('result').get('records')

# pandas DataFrameに変換
df = pd.DataFrame(datas)

# タイトル及びデータを表示
st.title("南城市避難場所")
st.dataframe(df[['名称', '住所', '緯度', '経度']])