from pico2d import *

class FEnemy:
    image = None
    def __init__(self):
        self.x, self.y = 335,305
        if FEnemy.image == None:
            FEnemy.image = load_image('Enemy1.png')


  #  def update(self, frame_time):


    def draw(self):
        self.image.draw(self.x, self.y)
    #pass
    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
