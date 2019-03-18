class Snake:
    def __init__(self, xcor, ycor, image, speed):
        self.is_alive = True
        self.direction = ""
        self.score = 0
        self.length = 3
        self.xcor = xcor
        self.ycor = ycor
        self.img = image
        self.speed = speed
        self.width = image.get_width()
        self.height = image.get_height()
    def show(self, game_Display, wall_left, wall_right):
        if self.direction == "RIGHT":
            self.xcor = self.xcor + self.speed
        elif self.direction == "LEFT":
            self.xcor = self.xcor - self.speed
        elif self.direction == "UP":
            self.ycor = self.ycor - self.speed 
        elif self.direction == "DOWN":
            self.ycor = self.ycor + self.speed
        game_Display.blit(self.img, (self.xcor, self.ycor))
    def move_left(self):
        self.direction = "LEFT"
    def move_right(self):
        self.direction = "RIGHT"
    def move_down(self):
        self.direction = "DOWN"
    def move_up(self):
        self.direction = "UP"