import os
import sys

from PIL import Image
from random import choice
import pygame

from find_map import find_map


cur_coords = [37.617698, 55.755864]
delta = 0.5
cur_delta = 0.9
cur_file = find_map(cur_coords)
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
            if i.key == pygame.K_PAGEUP:
                if cur_delta * delta > 0.00010986328124:
                    cur_delta *= delta
                cur_file = find_map(cur_coords, cur_delta)
                with open("map.png", "wb") as file:
                    file.write(cur_file)
            if i.key == pygame.K_PAGEDOWN:
                if cur_delta / delta < 57.7:
                    cur_delta /= delta
                cur_file = find_map(cur_coords, cur_delta)
                with open("map.png", "wb") as file:
                    file.write(cur_file)
            if i.key == pygame.K_UP:
                if cur_coords[1] + cur_delta < 84.4:
                    cur_coords[1] += cur_delta
                print(cur_coords)
                cur_file = find_map(cur_coords, cur_delta)
                with open("map.png", "wb") as file:
                    file.write(cur_file)
            if i.key == pygame.K_DOWN:
                if cur_coords[1] - cur_delta > -85.2:
                    cur_coords[1] -= cur_delta
                cur_file = find_map(cur_coords, cur_delta)
                with open("map.png", "wb") as file:
                    file.write(cur_file)
            if i.key == pygame.K_RIGHT:
                if cur_coords[0] + cur_delta < 85.2:
                    cur_coords[0] += cur_delta
                cur_file = find_map(cur_coords, cur_delta)
                with open("map.png", "wb") as file:
                    file.write(cur_file)
            if i.key == pygame.K_LEFT:
                if cur_coords[0] - cur_delta > -85.2:
                    cur_coords[0] -= cur_delta
                cur_file = find_map(cur_coords, cur_delta)
                with open("map.png", "wb") as file:
                    file.write(cur_file)
    screen.blit(pygame.image.load("map.png"), (0, 0))
    pygame.display.flip()
pygame.quit()
os.remove("map.png")
