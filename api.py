import urllib.request
import json

 
zomato_api = 'c7d979db7c4e418be68fd3b9a7d90115'
 
def locu_search(query):
    api_key = zomato_api
    url = 'https://developers.zomato.com/api/v2.1/search?api_key' + api_key
    locality = query.replace(' ', '%20')
    final_url = url + "&location=" + + location + "&entity_type=city=" + "&collection_id=1"
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
   
    for item in data['restaurants']:
        print (item['name'], item['address'])