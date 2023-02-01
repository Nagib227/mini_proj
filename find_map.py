import requests


def find_map(coords, delta=1):
    pos = coords
    delta = f"{delta},{delta}"
    map_params = {
        "ll": ",".join(pos.split()),
        "spn": delta,
        "l": "map"}
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    return response.content
