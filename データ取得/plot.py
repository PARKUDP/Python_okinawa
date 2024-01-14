import urllib.request as urllib2
import json
from prettytable import PrettyTable

resource = 'e0d8ac3b-a4f3-43ec-9d31-604fdf2c5677'
response = urllib2.urlopen(f'https://data.bodik.jp/api/3/action/datastore_search?resource_id={resource}')
data = json.loads(response.read()).get('result').get('records')

table = PrettyTable()
table.field_names = ["名称", "住所", "緯度", "経度"]

for i in range(len(data)):
    name = data[i]['名称']
    address = data[i]['住所']
    la = data[i]['緯度']
    lo = data[i]['経度']
    table.add_row([name, address, la, lo])

print(table)