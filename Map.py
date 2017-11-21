from pico2d import *

class FirstMap:
    def __init__(self):
        self.image = load_image('NewMap.png')

    def draw(self):
        self.image.draw(400, 300)
