import requests

herolistdata = ['Hulk', 'Captain America', 'Thanos']

def getdata(herolist):
    resultdata = {}
    for hero in herolist:
        URL = f'https://superheroapi.com/api/2619421814940190/search/{hero}'
        hero_t = requests.get(URL).json()
        hero_tt = hero_t['results']
        for res in hero_tt:
            if 'powerstats' in res:
                if hero == res['name']:
                    intelligence_h = int(res['powerstats']['intelligence'])
                    print(f'Интелект {hero}: {intelligence_h}')
                    resultdata[hero] = intelligence_h

    result = max(resultdata)
    print(f'Самый умный {result}')

getdata(herolistdata)

