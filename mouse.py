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
    def change_position(self, xcor, ycor):
        self.xcor = xcor
        self.ycor = ycor