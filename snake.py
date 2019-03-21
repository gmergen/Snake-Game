class Snake:
    def __init__(self, xcor, ycor, image, speed):
        self.is_alive = True
        self.direction = ""
        self.score = 0
        self.xcor = xcor
        self.ycor = ycor
        self.img = image
        self.speed = speed
        self.width = image.get_width()
        self.height = image.get_height()
        self.body = [[xcor,ycor], [xcor + self.width + 1, ycor], [xcor + self.width * 2 + 1,ycor]]
    def show(self, game_Display, wall_left, wall_right):
        if self.direction == "RIGHT":
            self.body.insert(0, [self.body[0][0] + self.width + 1, self.body[0][1]])
        elif self.direction == "LEFT":
            self.body.insert(0, [self.body[0][0] - self.width - 1, self.body[0][1]])
        elif self.direction == "UP":
            self.body.insert(0, [self.body[0][0], self.body [0][1] - self.height - 1])
        elif self.direction == "DOWN":
            self.body.insert(0, [self.body[0][0], self.body[0][1] + self.height + 1])
        self.body.pop()
        # snake change as snake moves coordinates
        self.xcor = self.body[0][0]
        self.ycor = self.body[0][1]
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
    def collides_with_self(self):
        for part in self.body[2:]:
            if self.xcor < part[0] + self.width \
                and self.xcor + self.width > part[0] \
                and self.ycor < part[1] + self.height \
                and self.ycor + self.height > part[1]: 
                return True
        return False
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
    def change_score(self, amount_to_change_by):
        self.score += amount_to_change_by 

