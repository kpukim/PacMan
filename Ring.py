import random

from pico2d import *

class ring:
    def __init__(self):
        self.x, self.y = 250, 300
        self.image = load_image('Money.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self, frame_time):
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

#pass