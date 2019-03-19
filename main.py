import pygame
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

# load object images
snake_Image = pygame.image.load("greenSquare.jpg")
mouse_Image = pygame.image.load("mouse.gif")

pygame.init()

game_Display = pygame.display.set_mode((window_Width, window_Height))


# instantiate objects
snake = Snake(350, 250, snake_Image, 3)


#snakes = []

#snakes.append(Snake(350 + snake.width * 2, 250, snake_Image, 3))
#snakes.append(Snake(350 + snake.width, 250, snake_Image, 3))
#snakes.append(Snake(350, 250, snake_Image, 3))

mouse = Mouse(250, 100, mouse_Image)



# main game loop
while snake.is_alive:
    
   # event handling
    for event in pygame.event.get():
       #print(str(event))
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
    #snake + border collision properties
    if snake.xcor < wall_left + snake.width / 2 - 0.25:
        snake.is_alive = False
    elif snake.xcor > wall_right - snake.width * 1.5:
        snake.is_alive = False
    elif snake.ycor < wall_top + snake.height / 2 - 0.25:
        snake.is_alive = False
    elif snake.ycor > wall_bottom - snake.height * 1.5:
        snake.is_alive = False

    game_Display.blit(game_Display, (0,0))
    game_Display.fill(black)

    # draw border
    pygame.draw.rect(game_Display, white, (border_side, border_top, window_Width - border_side * 2, window_Height - border_top - border_bottom))
    pygame.draw.rect(game_Display, black, (border_side + 3, border_top + 3, window_Width - border_side * 2 - 6,
    window_Height - border_top - border_bottom - 6))

    snake.show(game_Display, wall_left, wall_right)
    mouse.show(game_Display)

    #for snake in snakes:
    #    snake.show(game_Display, wall_left, wall_right)

    
    pygame.display.update()
    clock.tick(10)



pygame.quit()