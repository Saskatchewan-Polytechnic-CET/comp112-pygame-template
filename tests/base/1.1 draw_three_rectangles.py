# https://www.geeksforgeeks.org/python/how-to-draw-rectangle-in-pygame/

import pygame
pygame.init()
surface = pygame.display.set_mode((500, 400))

# colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.draw.rect(surface, red, pygame.Rect(50, 50, 100, 80))
pygame.draw.rect(surface, green, pygame.Rect(200, 50, 100, 80), 5)
pygame.draw.rect(surface, blue, pygame.Rect(350, 50, 100, 80), 10)

pygame.display.flip()
pygame.time.wait(4000)
pygame.quit()