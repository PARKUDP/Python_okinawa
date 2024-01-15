import tkinter as tk
from tkinter import ttk
import urllib.request as urllib2
import json

def search_data(search_entry, table, resource):
    # ユーザーの入力を取得
    user_input = search_entry.get()
    
    # APIからデータを取得
    response = urllib2.urlopen(f'https://data.bodik.jp/api/3/action/datastore_search?resource_id={resource}')
    data = json.loads(response.read()).get('result').get('records')
    
    # Treeview内のデータをクリア
    for i in table.get_children():
        table.delete(i)
        
    # データをTreeviewに追加（フィルタリング）
    for recode in data:
        if user_input in recode['名称']:
            table.insert("", "end", values=(recode['名称'], recode['住所'], recode['緯度'], recode['経度']))

# Tkinterウィンドウの初期化
root = tk.Tk()
root.title("データ検索")

# 検索欄とボタンの作成
#　ここで、できれば、ある地域別のボタンを押すことで、該当する地域のデータを検索できるようにしたいかも。