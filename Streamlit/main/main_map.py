import streamlit as st
import urllib.request as urllib2
import json
import pandas as pd
import folium
import streamlit as st
from streamlit_folium import st_folium


# データ取得関数
def get_data(resource):
    response = urllib2.urlopen(f'https://data.bodik.jp/api/3/action/datastore_search?resource_id={resource}')
    data = json.loads(response.read()).get('result').get('records')
    return pd.DataFrame(data)

# Streamlitアプリのメイン関数
def main():
    st.title("南城市のデータ検索")

    search_input = st.text_input("検索", "")

    if search_input:
        if search_input == "AED":
            resource = '0106f818-dd7f-4150-bb5e-4207243d8b52'
        elif search_input in ["文化", "文化財一覧"]:
            resource = '928764f8-3c8d-4ad1-a269-9547bc788549'
        elif search_input in ["医療機関", "医療機関一覧", "医療", "病院一覧"]:
            resource = '24885c01-3fa5-4cbf-b9bf-0cf8d34b3683'
        elif search_input in ["避難場所", "避難場所一覧", "避難所", "避難所一覧", "避難"]:
            resource = 'e0d8ac3b-a4f3-43ec-9d31-604fdf2c5677'
        else:
            st.error("無効な検索キーワードです。")
            return

        data = get_data(resource)
        filter_input = st.text_input("フィルタ").lower()
        if filter_input:
            data = data[data['名称'].str.lower().str.contains(filter_input)]

        st.dataframe(data[['名称', '住所', '緯度', '経度']], 1000, 450)

        n = folium.Map(location=[26.168, 127.851], zoom_start=6)
        
        for i, row in data.iterrows():
            folium.Marker(
                [row['緯度'], row['経度']], popup=row['名称'], tooltip=row['名称']
            ).add_to(n)
        st_data = st_folium(n, width=1200, height=800)

if __name__ == "__main__":
    main()
