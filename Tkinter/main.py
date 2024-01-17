import tkinter as tk
from tkinter import ttk
import urllib.request as urllib2
import json

# 南城市AED設置場所一覧：0106f818-dd7f-4150-bb5e-4207243d8b52 ->　取りたいデータは、名称、住所、緯度、経度である
# 南城市文化財一覧：928764f8-3c8d-4ad1-a269-9547bc788549 ->  取りたいデータは、名称、住所、緯度、経度である
# 南城市医療機関一覧：24885c01-3fa5-4cbf-b9bf-0cf8d34b3683 ->  取りたいデータは、名称、住所、緯度、経度である

def filter_data(result_table, data, filter_entry):
    filter_input = filter_entry.get().lower()
    # Treeview内のデータをクリア
    for i in result_table.get_children():
        result_table.delete(i)
    # フィルタリングされたデータをTreeviewに追加
    for recode in data:
        if filter_input in recode['名称'].lower():
            result_table.insert("", "end", values=(recode['名称'], recode['住所'], recode['緯度'], recode['経度']))

def search_data(search_entry, root):
    # ユーザーの入力を取得
    user_input = search_entry.get()
    
    if(user_input == "AED"):
        resource = '0106f818-dd7f-4150-bb5e-4207243d8b52'
        
    elif(user_input == "文化財" or user_input == "文化財一覧"):
        resource = '928764f8-3c8d-4ad1-a269-9547bc788549'
        
    elif(user_input == "医療機関" or user_input == "医療機関一覧" or user_input == "病院" or user_input == "病院一覧"):
        resource = '24885c01-3fa5-4cbf-b9bf-0cf8d34b3683'
        
    else:
        # 他の場合を追加する場合は、ここに追加する
        pass
    
    top = tk.Toplevel(root)
    top.title(f"{user_input}の検索結果")
    
    # キーワードフィルタ
    filter_frame = ttk.Frame(top)
    filter_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    filter_label = tk.Label(filter_frame, text="フィルタ:")
    filter_label.pack(side=tk.LEFT)

    filter_entry = tk.Entry(filter_frame)
    filter_entry.pack(side=tk.LEFT)

    # フィルタリング用のボタンにフィルタ関数を設定
    filter_button = ttk.Button(filter_frame, text="フィルタ適用", command=lambda: filter_data(result_table, data, filter_entry))
    filter_button.pack(side=tk.LEFT)

    result_table = ttk.Treeview(top, columns=("名称", "住所", "緯度", "経度"), show="headings")
    result_table.heading("名称", text="名称")
    result_table.heading("住所", text="住所")
    result_table.heading("緯度", text="緯度")
    result_table.heading("経度", text="経度")
    result_table.pack(expand=True, fill="both")

    # APIからデータを取得
    response = urllib2.urlopen(f'https://data.bodik.jp/api/3/action/datastore_search?resource_id={resource}')
    data = json.loads(response.read()).get('result').get('records')
    
    for recode in data:
        result_table.insert("", "end", values=(recode['名称'], recode['住所'], recode['緯度'], recode['経度']))
        
# Tkinterウィンドウの初期化
root = tk.Tk()
root.title("南城市のデータ検索")

search_frame = ttk.Frame(root)
search_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

search_label = tk.Label(search_frame, text="検索:")
search_label.pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT)

search_button = ttk.Button(search_frame, text="検索", command=lambda: search_data(search_entry, root))
search_button.pack(side=tk.LEFT)

root.mainloop()