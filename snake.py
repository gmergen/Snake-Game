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
        self.body = [[xcor,ycor], [xcor + self.width,ycor], [xcor + self.width * 2,ycor]]
    def show(self, game_Display, wall_left, wall_right):
        if self.direction == "RIGHT":
            self.body.insert(0, [self.body[0][0] + self.width, self.body[0][1]])
            self.body.pop() 
            #self.xcor = xcor + self.speed
        elif self.direction == "LEFT":
            self.body.insert(0, [self.body[0][0] - self.width, self.body[0][1]])
            self.body.pop()
        elif self.direction == "UP":
            self.body.insert(0, [self.body[0][0], self.body [0][1] - self.height])
            self.body.pop()
        elif self.direction == "DOWN":
            self.body.insert(0, [self.body[0][0], self.body[0][1] + self.height])
            self.body.pop()
        for part in self.body:
            game_Display.blit(self.img, (part[0], part[1]))
        #game_Display.blit(self.img, (self.xcor, self.ycor))
        #changes direction of snake
    def move_left(self):
        if self.direction != "RIGHT":
            self.direction = "LEFT"
    def move_right(self):
        if self.direction != "LEFT":
            self.direction = "RIGHT"
    def move_down(self):
        if self.direction != "UP":
            self.direction = "DOWN"
    def move_up(self):
        if self.direction != "DOWN":
            self.direction = "UP"
    def collides_with(self, foreign_object):
        return foreign_object.xcor < self.body[0][0] + self.width \
        and foreign_object.xcor + foreign_object.width > self.body[0][0] \
        and foreign_object.ycor < self.body[0][1] + self.height \
        and foreign_object.ycor + self.height > self.body[0][1] 
    def grow(self):
        # for last body part
        x = self.body[len(self.body) - 1][0]
        y = self.body[len(self.body) - 1][1]
        # for second to last body part
        x2 = self.body[len(self.body) - 2][0]
        y2 = self.body[len(self.body) - 2][1]
        # add to snake's body for each direction
        if x < x2:
            self.body.append((x - self.width, y))
        elif x > x2:
            self.body.append((x + self.width, y))
        elif y < y2:
            self.body.append((x, y - self.height))
        elif y > y2:
            self.body.append((x, y + self.height))

