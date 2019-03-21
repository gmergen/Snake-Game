from snake import Snake
from random import randint

class Mouse:
    def __init__ (self, xcor, ycor, image):
        self.is_alive = True
        self.xcor = xcor
        self.ycor = ycor
        self.img = image
        self.width = image.get_width()
        self.height = image.get_height()
    def show(self, game_Display): 
        game_Display.blit(self.img, (self.xcor, self.ycor))
    def change_position(self,wall_left, wall_right, wall_top, wall_bottom, snake):
        self.xcor = randint(wall_left + 10, wall_right - 10) 
        self.ycor = randint(wall_top + 10, wall_bottom - snake.height)
        while self.appears_on(snake):
            print("hey")
            self.xcor = randint(wall_left + 10, wall_right - 10)
            self.ycor = randint(wall_top + 10, wall_bottom - snake.height)
    def appears_on(self, snake):
        for part in snake.body[0:]:
            if self.xcor < part[0] + self.width \
                and self.xcor + self.width > part[0] \
                and self.ycor < part[1] + self.height \
                and self.ycor + self.height > part[1]:
                return True
        return False