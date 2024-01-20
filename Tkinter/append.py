import tkinter as tk
from tkinter import ttk
import urllib.request as urllib2
import json

deleted_records = []  # 削除されたレコードを格納するリスト
added_records = []  # 追加されたレコードを格納するリスト

def search_data():
    # ユーザーの入力を取得
    user_input = search_entry.get()

    # APIからデータを取得
    resource = 'e0d8ac3b-a4f3-43ec-9d31-604fdf2c5677'
    response = urllib2.urlopen(f'https://data.bodik.jp/api/3/action/datastore_search?resource_id={resource}')
    data = json.loads(response.read()).get('result').get('records')

    # Treeview内のデータをクリア
    for i in table.get_children():
        table.delete(i)

    # データをTreeviewに追加（フィルタリング）
    for record in data:
        if (user_input in record['名称']) and (record['名称'] not in deleted_records):
            table.insert("", "end", values=(record['名称'], record['住所'], record['緯度'], record['経度']))

    for record in added_records:
        if user_input in record['名称']:
            table.insert("", "end", values=(record['名称'], record['住所'], record['緯度'], record['経度']))


def delete_selected_data():
    selected_items = table.selection()
    for item in selected_items:
        record_name = table.item(item, 'values')[0]
        deleted_records.append(record_name)  # 削除されたレコードをリストに追加
        table.delete(item)


def add_data():
    # ユーザーの入力を取得
    add_windows = tk.Toplevel(root)
    add_windows.title("データ追加")
    
    # 新しいデータの入力フィールドを作成
    name_label = tk.Label(add_windows, text="名称")
    name_label.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    name_entry = ttk.Entry(add_windows)
    name_entry.pack(side=tk.TOP, fill=tk.X)
    
    address_label = tk.Label(add_windows, text="住所")
    address_label.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    address_entry = ttk.Entry(add_windows)
    address_entry.pack(side=tk.TOP, fill=tk.X)
    
    latitude_label = tk.Label(add_windows, text="緯度")
    latitude_label.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    latitude_entry = ttk.Entry(add_windows)
    latitude_entry.pack(side=tk.TOP, fill=tk.X)
    
    longitude_label = tk.Label(add_windows, text="経度")
    longitude_label.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    longitude_entry = ttk.Entry(add_windows)
    longitude_entry.pack(side=tk.TOP, fill=tk.X)
    
    
    # データ追加ボタンの作成
    def save():
        name = name_entry.get()
        address = address_entry.get()
        latitude = latitude_entry.get()
        longitude = longitude_entry.get()

        # 追加するデータを辞書として作成
        new_record = {'名称': name, '住所': address, '緯度': latitude, '経度': longitude}
        added_records.append(new_record)
    
        # Treeviewに新しいデータを追加
        table.insert("", "end", values=(name, address, latitude, longitude))
        
        add_windows.destroy()

    save_button = ttk.Button(add_windows, text="データ追加", command=save)
    save_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    
    # 入力フィールドをクリア
    name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    latitude_entry.delete(0, tk.END)
    longitude_entry.delete(0, tk.END)

# Tkinterウィンドウの初期化
root = tk.Tk()
root.title("南城市避難場所検索")

# 検索欄とボタンの作成
search_entry = ttk.Entry(root)
search_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
search_button = ttk.Button(root, text="検索", command=search_data)
search_button.pack(side=tk.TOP, fill=tk.X, padx=3, pady=3)

# 追加ボタンの作成
add_button = ttk.Button(root, text="追加", command=add_data)
add_button.pack(side=tk.TOP, fill=tk.X, padx=3, pady=3)

table = ttk.Treeview(root, columns=("名称", "住所", "緯度", "経度"), show='headings')
table.heading("名称", text="名称")
table.heading("住所", text="住所")
table.heading("緯度", text="緯度")
table.heading("経度", text="経度")
table.pack(expand=True, fill="both")

delete_button = ttk.Button(root, text="選択したデータを削除", command=delete_selected_data)
delete_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# GUIを実行
root.mainloop()