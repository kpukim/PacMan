from pico2d import *

class SEnemy:
    image = None
    def __init__(self):
        self.x, self.y, self.dir = 130,420, 1

        if SEnemy.image == None:
            SEnemy.image = load_image('Enemy2.png')



    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self, frame_time):
        self.x += self.dir
        if self.x <= 130:
            self.dir =1
        if self.x >= 600:
            self.dir =-1


    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
