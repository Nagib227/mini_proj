import os
import sys

import requests
from PIL import Image
from random import choice
import pygame


def find_map(cite):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": cite,
        "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        raise "http"
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    pos = toponym["Point"]["pos"]
    delta = "1,1"
    map_params = {
        "ll": ",".join(pos.split()),
        "spn": delta,
        "l": choice(["sat", "map"])}
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    return response.content


########
cites = ["Москва", "Курск", "Санкт-Питербург"]
########

cur_cite = choice(cites)
cur_file = find_map(cur_cite)
with open("map.png", "wb") as file:
    file.write(cur_file)

pygame.init()
screen = pygame.display.set_mode((600, 450))
cur_img = 0
screen.blit(pygame.image.load("map.png"), (0, 0))
pygame.display.flip()
running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.KEYDOWN:
            cite = choice(cites)
            while cur_cite == cite:
                cite = choice(cites)
            cur_cite = cite
            cur_file = find_map(cur_cite)
            with open("map.png", "wb") as file:
                file.write(cur_file)
    screen.blit(pygame.image.load("map.png"), (0, 0))
    pygame.display.flip()
pygame.quit()

os.remove("map.png")
