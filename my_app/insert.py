import json
import requests

with open('places.json') as json_data:
    places = json.load(json_data)
    results = places.get('results')
    for i in range(len(results)):
        data = {
            'place_id': results[i].get('place_id'),
            'name': results[i].get('name', ''),
            'latitude': results[i].get('latitude', 0),
            'longitude': results[i].get('longitude', 0),
            'rating': results[i].get('rating'),
            'vicinity': results[i].get('vicinity', '')
        }
        import ipdb;ipdb.set_trace()
        request = requests.post(
            'http://127.0.0.1:5000/gas_station/',
            data=data
        )
        print(request.content)