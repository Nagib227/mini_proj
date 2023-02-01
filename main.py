import os
import sys

from PIL import Image
from random import choice
import pygame

from find_map import find_map


########
cites = ["Москва"]
########

cur_cite = cites[0]
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
            pass
pygame.quit()
os.remove("map.png")
