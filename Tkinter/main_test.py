import tkinter as tk
from tkinter import ttk
import urllib.request as urllib2
import json

# データ検索関数
def search_data(resource, region=None):
    # APIからデータを取得
    response = urllib2.urlopen(f'https://data.bodik.jp/api/3/action/datastore_search?resource_id={resource}')
    data = json.loads(response.read()).get('result').get('records')
    
    # Treeview内のデータをクリア
    for i in table.get_children():
        table.delete(i)
        
    # データをTreeviewに追加（フィルタリング）
    for record in data:
        if region is None or region in record['住所']:
            table.insert("", "end", values=(record['名称'], record['住所'], record['緯度'], record['経度']))

# Tkinterウィンドウの初期化
root = tk.Tk()
root.title("データ検索")

# Treeviewの作成
columns = ("名称", "住所", "緯度", "経度")
table = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    table.heading(col, text=col)
table.pack()

# 地域別のボタン作成
regions = ["地域1", "地域2", "地域3"]  # 実際の地域名に置き換える
for region in regions:
    button = tk.Button(root, text=region, command=lambda r=region: search_data('0106f818-dd7f-4150-bb5e-4207243d8b52', r))
    button.pack()

# 全データ表示ボタン
all_data_button = tk.Button(root, text="全データ表示", command=lambda: search_data('0106f818-dd7f-4150-bb5e-4207243d8b52'))
all_data_button.pack()

# Tkinterメインループ
root.mainloop()