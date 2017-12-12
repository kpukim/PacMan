from pico2d import *

class TEnemy:
    image = None
    def __init__(self):
        self.x, self.y, self.dir = 765,550, 1
        if TEnemy.image == None:
            TEnemy.image = load_image('Enemy3.png')


    def update(self, frame_time):
        self.y += self.dir
        if self.y <= 100:
            self.dir = 1
        elif self.y >= 500:
            self.dir = -1



    def draw(self):
        self.image.draw(self.x, self.y)


    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
