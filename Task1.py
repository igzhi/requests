import requests
from pprint import pprint

URL = 'https://superheroapi.com/api/2619421814940190/search/Hulk'
hulk = requests.get(URL).json()
hulk1 = hulk['results']
for res in hulk1:
    if 'powerstats' in res:
        if 'Hulk' == res['name']:
            intelligence_hulk = int(res['powerstats']['intelligence'])
            print(f'Интелект Халка: {intelligence_hulk}')
            hulk1 = {'name': res['name'], 'smart': intelligence_hulk}

URL = 'https://superheroapi.com/api/2619421814940190/search/Captain America'
captain = requests.get(URL).json()
captain1 = captain['results']
for res in captain1:
    if 'powerstats' in res:
        intelligence_captain = int(res['powerstats']['intelligence'])
        print(f'Интелект Капитана Америки: {intelligence_captain}')
        captain1 = {'name': res['name'], 'smart': intelligence_captain}

URL = 'https://superheroapi.com/api/2619421814940190/search/Thanos'
thanos = requests.get(URL).json()
thanos1 = thanos['results']
for res in thanos1:
    if 'powerstats' in res:
        intelligence_thanos = int(res['powerstats']['intelligence'])
        print(f'Интелект Таноса: {intelligence_thanos}')
        thanos1 = {'name': res['name'], 'smart': intelligence_thanos}

if thanos1['smart'] < captain1['smart'] > hulk1['smart']:
    print(f"Самый умный {captain1['name']}")
elif captain1['smart'] < thanos1['smart'] > hulk1['smart']:
    print(f"Самый умный {thanos1['name']}")
else:
    print(f"Самый умный {hulk1['name']}")


