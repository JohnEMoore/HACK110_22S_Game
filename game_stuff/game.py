"""The start of bad-megaman"""

import pygame
from player import Player


pygame.init()

display = pygame.display.set_mode((600, 600))

while True:

    display.fill((123, 175, 212))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # elif i.type == pygame.KEYDOWN:
        #     if i.key == pygame.K_LEFT:
        #         play.rect.move_ip(-10, 0)
        #     elif i.key == pygame.K_RIGHT:
        #         play.rect.move_ip(10, 0)
        #     elif i.key == pygame.K_UP:
        #         play.rect.move_ip(0, 10)
    
    player: Player = Player(200, 200, 128, 128)

    player.draw(display)

    pygame.display.update()