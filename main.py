import requests

TRANSIT = "transit"
DRIVING = "driving"

TRANSIT_BUS = "bus"
TRANSIT_TRAIN = "train"

def distance(origin, destination, key, mode=TRANSIT, transit_mode=TRANSIT_TRAIN):
    payload = {'origins': origin,
               'destinations': destination,
               'key': key,
               'mode': mode,
               'transit_mode': transit_mode}

    r = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json',
                     params=payload)

    data = r.json()
    
    distance_value = data["rows"][0]["elements"][0]["distance"]["value"]
    return distance_value

