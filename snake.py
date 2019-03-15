class Snake:
   def __init__(self, xcor, ycor, image, speed):
       self.is_alive = True
       self.direction = 0
       self.score = 0
       self.length = 1
       self.xcor = xcor
       self.ycor = ycor
       self.img = image
       self.speed = speed
       self.width = image.get_width()
       self.height = image.get_height()
   def show(self, game_Display, wall_left, wall_right):
        game_Display.blit(self.img, (self.xcor, self.ycor))
        new_xcor = self.xcor + self.direction * self.speed
        new_ycor = self.ycor + self.direction * self.speed