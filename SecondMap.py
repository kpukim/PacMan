from pico2d import *

class secondmap:
    def __init__(self):
        self.image = load_image('Map.png')

    def draw(self):
        self.image.draw(400, 300)
#pass