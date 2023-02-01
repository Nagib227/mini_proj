import requests


def find_map(coords, delta=1):
    delta = f"{delta},{delta}"
    map_params = {
        "ll": ",".join([str(coords[0]), str(coords[1])]),
        "spn": delta,
        "l": "map"}
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    return response.content
