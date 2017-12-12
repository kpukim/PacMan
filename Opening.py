import game_framework
from pico2d import *

import Main
import Main2


name = "Opening"
image = None


def enter():
    global image
    image = load_image('Opening.png')
    pass


def exit():
    global image
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.push_state(Main)
    pass


def draw(frame_time):
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass







def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass

