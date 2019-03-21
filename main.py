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

pygame.init()

# load object images
snake_Image = pygame.image.load("greenSquare.jpg")
mouse_Image = pygame.image.load("mouse.gif")

# load sounds
horn_sound = pygame.mixer.Sound('horn.wav')
pygame.mixer.music.load('Anaconda.wav')
pygame.mixer.music.play(-1)

# title and score font creation
title_font = pygame.font.SysFont('Arial', 40, True)
score_font = pygame.font.SysFont('Arial', 26, True)

#set window caption instead of "pygame.window"
game_Display = pygame.display.set_mode((window_Width, window_Height))
pygame.display.set_caption('Snake')

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
        mouse.change_position(wall_left, wall_right, wall_top, wall_bottom, snake)
        snake.grow()
        snake.change_score(100)
    
    
    game_Display.blit(game_Display, (0,0))
    game_Display.fill(black)
    #display PYTHON title and score board
    title_text = title_font.render('PYTHON', False, green)
    game_Display.blit(title_text, (window_Width / 2 - title_text.get_width() / 2, 5))
    score_text = score_font.render('SCORE: ' + str(snake.score), False, blue)
    game_Display.blit(score_text, (wall_left, wall_bottom + border_width))

    # draw border
    pygame.draw.rect(game_Display, red, (border_side, border_top, window_Width - border_side * 2, window_Height - border_top - border_bottom))
    pygame.draw.rect(game_Display, black, (border_side + 3, border_top + 3, window_Width - border_side * 2 - 6,
    window_Height - border_top - border_bottom - 6))

    snake.show(game_Display, wall_left, wall_right)
    mouse.show(game_Display)

     #snake + border collision properties
    if snake.body[0][0] < wall_left + snake.width - snake.width / 2:
        snake.is_alive = False
        horn_sound.play()
    elif snake.body[0][0] > wall_right - snake.width:
        snake.is_alive = False
        horn_sound.play()
    elif snake.body[0][1] < wall_top:
        snake.is_alive = False
        horn_sound.play()
    elif snake.body[0][1] > wall_bottom - snake.height:
        snake.is_alive = False
        horn_sound.play()
    # snake dies if touches self
    if snake.collides_with_self():
        snake.is_alive = False
        horn_sound.play()

    pygame.display.update()
    clock.tick(10)

# final screen load after death
show_final_screen = True
while show_final_screen:
    score_text = score_font.render('SCORE: ' + str(snake.score), False, blue)
    game_Display.blit(score_text, (window_Width / 2 - score_text.get_width() / 2, window_Height / 2))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            show_final_screen = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                show_final_screen = False
    pygame.mixer.music.stop()

pygame.quit()