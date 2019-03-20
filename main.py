import pygame
from random import randint
from snake import Snake
from mouse import Mouse


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

# clock
clock = pygame.time.Clock()

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# load object images
snake_Image = pygame.image.load("greenSquare.jpg")
mouse_Image = pygame.image.load("mouse.gif")

pygame.init()

game_Display = pygame.display.set_mode((window_Width, window_Height))


# instantiate objects
snake = Snake(347, 255, snake_Image, 3)
mouse = Mouse(247, 105, mouse_Image)
snake.direction = "LEFT"



# main game loop
while snake.is_alive:
    
   # event handling
    for event in pygame.event.get():
       #print(str(event)) and mouse collision properties
        if event.type == pygame.QUIT:
            snake.is_alive = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.move_left()
            elif event.key == pygame.K_RIGHT:
                snake.move_right()
            elif event.key == pygame.K_UP:
                snake.move_up()
            elif event.key == pygame.K_DOWN:
                snake.move_down()
    if snake.collides_with(mouse):
        mouse.change_position(randint(wall_left + 10, wall_right - 10), randint(wall_top + 5, wall_bottom - 15))
        snake.grow() 

    game_Display.blit(game_Display, (0,0))
    game_Display.fill(black)

    # draw border
    pygame.draw.rect(game_Display, red, (border_side, border_top, window_Width - border_side * 2, window_Height - border_top - border_bottom))
    pygame.draw.rect(game_Display, black, (border_side + 3, border_top + 3, window_Width - border_side * 2 - 6,
    window_Height - border_top - border_bottom - 6))

    snake.show(game_Display, wall_left, wall_right)
    mouse.show(game_Display)

     #snake + border collision properties
    if snake.body[0][0] < wall_left + snake.width - snake.width / 2:
        snake.is_alive = False
    elif snake.body[0][0] > wall_right - snake.width:
        snake.is_alive = False
    elif snake.body[0][1] < wall_top:
        snake.is_alive = False
    elif snake.body[0][1] > wall_bottom - snake.height:
        snake.is_alive = False
    # snake dies if touches self
    if snake.collides_with_self():
        snake.is_alive = False

    pygame.display.update()
    clock.tick(10)



pygame.quit()