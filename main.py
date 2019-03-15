import pygame
from snake import Snake


# establish window dimensions
window_Width = 700
window_Height = 500

# game border properties
border_side = 10
border_top = 40
border_bottom = border_top
border_width = 3

# wall properties
wall_top = border_top + border_width
wall_left = border_side + border_width
wall_right = window_Width - border_side - border_width
wall_bottom = window_Height - border_bottom - border_width

#colors
black = (0,0,0)
white = (255,255,255)

# load object images
snake_Image = pygame.image.load("greenSquare.jpg")

pygame.init()

game_Display = pygame.display.set_mode((window_Width, window_Height))


# instantiate snake
snake = Snake(350, 250, snake_Image, 5)

# draw border
pygame.draw.rect(game_Display, white, (border_side, border_top, window_Width - border_side * 2, window_Height - border_top - border_bottom))
pygame.draw.rect(game_Display, black, (border_side + 3, border_top + 3, window_Width - border_side * 2 - 6,
       window_Height - border_top - border_bottom - 6))


# main game loop
while snake.is_alive:
   # event handling
   for event in pygame.event.get():
       #print(str(event))
       if event.type == pygame.QUIT:
           snake.is_alive = False
   pygame.display.update()


pygame.quit()