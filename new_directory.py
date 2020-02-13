import os
import sys

import pygame
import requests

response = None
center = "37.620070,55.753630".split(',')
map_request = f"http://static-maps.yandex.ru/1.x/?ll={center[0]},{center[1]}&spn=0.1,0.1&l=sat,skl"

response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.

def dvig():
    global map_request
    return map_request


map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)


# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                center[0] = str(float(center[0][0:2]) + 1 + float(center[0][2:]))
                dvig()
            elif event.key == pygame.K_DOWN:

                center[0] = str(float(center[0][0:2]) - 1 + float(center[0][2:]))
                dvig()
            elif event.key == pygame.K_LEFT:
                center[1] = str(float(center[1][0:2]) + 1 + float(center[1][2:]))
                dvig()
            elif event.key == pygame.K_RIGHT:
                center[1] = str(float(center[1][0:2]) + 1 + float(center[1][2:]))
                dvig()
            # map_request = f"http://static-maps.yandex.ru/1.x/?ll={center[0]},{center[1]}&spn=0.1,0.1&l=sat,skl"
    pygame.display.flip()
pygame.quit()



# Удаляем за собой файл с изображением.
os.remove(map_file)