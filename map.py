import requests
import pygame
from io import BytesIO
from PIL import Image


def get_img(coords):
    delta = '0.002'
    map_server = 'https://static-maps.yandex.ru/1.x/'
    params = {'ll': ','.join(coords),
              'spn': ','.join([delta, delta]),
              'l': 'map',
              'pt': f"{','.join(coords)},org"}
    response = requests.get(map_server, params=params)
    Image.open(BytesIO(response.content)).save('map.png')
    return 'map.png'


def show_map(map):
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map), (0, 0))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
