from pico2d import *

class SEnemy:
    image = None
    def __init__(self):
        self.x, self.y = 400,305
        if SEnemy.image == None:
            SEnemy.image = load_image('Enemy2.png')


#   def update(self, frame_time):


    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
