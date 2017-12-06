from pico2d import *

class TEnemy:
    image = None
    def __init__(self):
        self.x, self.y = 460,305
        if TEnemy.image == None:
            TEnemy.image = load_image('Enemy3.png')


 #   def update(self, frame_time):


    def draw(self):
        self.image.draw(self.x, self.y)
    #pass
    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
