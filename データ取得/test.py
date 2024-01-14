import urllib.request as urllib2
import urllib
import json
import pprint

resource = 'e0d8ac3b-a4f3-43ec-9d31-604fdf2c5677'
response = urllib2.urlopen(f'https://data.bodik.jp/api/3/action/datastore_search?resource_id={resource}')
data = json.loads(response.read())

print(data)