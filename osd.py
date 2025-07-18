import pygame
import time
import subprocess
import json
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "10,10"
os.environ['SDL_VIDEO_CENTERED'] = '0'

def get_battery():
    try:
        data = subprocess.check_output(['pisugar-power-manager', 'get battery'])
        info = json.loads(data.decode())
        return info["percent"], info["charging"]
    except:
        return 0, False

pygame.init()
screen = pygame.display.set_mode((140, 40), pygame.NOFRAME)
pygame.display.set_caption('Battery OSD')

font = pygame.font.SysFont("Arial", 32)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    percent, charging = get_battery()
    screen.fill((0, 0, 0, 0))
    color = (0, 255, 0) if percent > 30 else (255, 255, 0) if percent > 15 else (255, 0, 0)
    text = f"{percent}% {'⚡' if charging else ''}"
    label = font.render(text, 1, color)
    screen.blit(label, (10, 0))
    pygame.display.update()
    time.sleep(30)
pygame.quit()
