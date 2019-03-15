class Snake:
   def __init__(self, xcor, ycor, image, speed):
       self.is_alive = True
       self.direction = 0
       self.score = 0
       self.length = 1
    def show(self, gameDisplay, wall_left, wall_right):
        new_xcor = self.xcor + self.direction * self.speed
        new_ycor = self.ycor + self.direction * self.speed