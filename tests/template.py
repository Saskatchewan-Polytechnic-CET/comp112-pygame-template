###################
# T E M P L A T E #
###################

# Import Python game library, time and system exit
import pygame
from pygame.locals import *
import time
from sys import exit

# Setup game
def setup(window_name,width=400,height=400):
    """Routine to initialize pygame and setup the screen"""

    # Init pygame
    pygame.init()

    # Setup the display
    screen = pygame.display.set_mode((width, height + 100), 0, 32)

    # Set game window name
    pygame.display.set_caption(window_name)

    # Customize window
    ## e.g., Set background image, title screen

    return screen

# Quit the game
def quit():
    """Quit the game and exit"""
    pygame.quit()
    exit()

# Logic for game events
def process_event(screen, event):
    """All possible actions for different game events"""

    # Quit
    if event.type == QUIT:
        quit()
    # Keyboard
    elif event.type == KEYDOWN:  
        if event.key == K_LEFT:  
            print("pressed LEFT")
        elif event.key == K_RIGHT:  
            print("pressed RIGHT")
        elif event.key == K_UP: 
            print("pressed UP")
        elif event.key == K_DOWN: 
            print("pressed DOWN")
        elif event.key == K_q: 
            game_over(screen)
    # Mouse
    elif event.type == MOUSEBUTTONDOWN:
        # Get position
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Draw red circle
        red = pygame.Color(255, 0, 0)
        circle_size = 10
        pygame.draw.circle(screen, red, (mouse_x, mouse_y), circle_size, 0)
        # Update the display
        pygame.display.flip()

# Game over function
def game_over(screen, score=0):
    """Draw a GAME OVER with score on the screen and exit"""
  
    # Create font
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # Create a text surface 
    red = pygame.Color(255, 0, 0)
    game_over_surface = my_font.render(
        f"GAME OVER: {score}", True, red)
    
    # Create a rectangular object for the text 
    game_over_rect = game_over_surface.get_rect()
    
    # Set the position of the text
    game_over_rect.midtop = (screen.get_width()/2, screen.get_height()/4)
    
    # Draw the text on screen
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # Wait 2 seconds
    time.sleep(2)
    
    # Quit the game
    quit()

# Start text
def start_game():
    """Draw HELLO on the screen"""

    # Create font
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # Create a text surface 
    blue = pygame.Color(0, 0, 255)
    hello_surface = my_font.render(
        f"HELLO", True, blue)
    
    # Create a rectangular object for the text 
    hello_rect = hello_surface.get_rect()
    
    # Set the position of the text
    hello_rect.midtop = (screen.get_width()/2, screen.get_height()/4)
    
    # Draw the text on screen
    screen.blit(hello_surface, hello_rect)
    pygame.display.flip()
    
    # Wait 2 seconds
    time.sleep(2)

    # Clear text by redrawing nothing
    black = (0, 0, 0)
    screen.fill(black)

# Program entry point
if __name__ == "__main__":

    # Create the game window
    screen = setup("Game name")

    # Set frames per second
    fps = 30

    # Track time
    CLOCK = pygame.time.Clock()

    # Show start text
    start_game()

    # Main loop
    while(True):

        # Event logic
        for event in pygame.event.get():
            process_event(screen, event)

        # Update window
        pygame.display.update()
        CLOCK.tick(fps)