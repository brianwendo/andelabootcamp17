import urllib.request
import json

zomato_api = 'c7d979db7c4e418be68fd3b9a7d90115'


def zomato_search(query):
	api_key = zomato_api
	url = 'https://developers.zomato.com/api/v2.1/search?api_key' + api_key
	location = query
	final_url = url + "&location=" + location + "&entity_type=city=" + "&collection_id=1"
    json_obj = urllib.request.urlopen(final_url)
	data = json.load(json_obj)

	for item in data["restaurants"]:
		print(" This weeks trending restaurants in New York:",["name"],["address"],["cuisines"])