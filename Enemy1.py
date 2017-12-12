from pico2d import *

class FEnemy:
    image = None
    def __init__(self):
        self.x, self.y, self.dir = 475,305, 0.5
        if FEnemy.image == None:
            FEnemy.image = load_image('Enemy1.png')


    def update(self, frame_time):
        self.x += self.dir
        if self.x >= 475:
            self.dir = -0.5

        elif self.x <= 325:
            self.dir = 0.5


    def draw(self):
        self.image.draw(self.x, self.y)


    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
