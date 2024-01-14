import tkinter as tk
from tkinter import ttk
import urllib.request as urllib2
import json

# APIからデータを取得
resource = 'e0d8ac3b-a4f3-43ec-9d31-604fdf2c5677'
response = urllib2.urlopen(f'https://data.bodik.jp/api/3/action/datastore_search?resource_id={resource}')
data = json.loads(response.read()).get('result').get('records')

# Tkinterウィンドウの初期化
root = tk.Tk()
root.title("データテーブル")

# Treeviewウィジェットの作成
table = ttk.Treeview(root, columns=("名称", "住所", "緯度", "経度"), show='headings')
table.heading("名称", text="名称")
table.heading("住所", text="住所")
table.heading("緯度", text="緯度")
table.heading("経度", text="経度")

# データをTreeviewに追加
for record in data:
    table.insert("", "end", values=(record['名称'], record['住所'], record['緯度'], record['経度']))

# Treeviewをウィンドウに配置
table.pack(expand=True, fill="both")

# GUIを実行
root.mainloop()
