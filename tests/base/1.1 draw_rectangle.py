# https://www.geeksforgeeks.org/python/how-to-draw-rectangle-in-pygame/

import pygame
pygame.init()  
surface = pygame.display.set_mode((400, 300))  # window
color = (255, 192, 203)  

pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))  
pygame.display.flip() 
pygame.time.wait(3000)  # Pause for 3 seconds
pygame.quit()  