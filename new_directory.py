import os
import sys

import pygame
import requests

response = None
center = "37.620070,55.753630".split(',')
map_request = f"http://static-maps.yandex.ru/1.x/{center[0]},{center[1]}&spn=0.1,0.1&l=sat,skl"

response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)



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
                center[0] += 1
            elif event.key == pygame.K_DOWN:
                center[0] -= 1
            elif event.key == pygame.K_LEFT:
                center[1] -= 1
            elif event.key == pygame.K_RIGHT:
                center[1] += 1
            map_request = f"http://static-maps.yandex.ru/1.x/{center[0]},{center[1]}&spn=0.1,0.1&l=sat,skl"
    pygame.display.flip()
pygame.quit()


# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Удаляем за собой файл с изображением.
os.remove(map_file)