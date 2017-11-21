import game_framework
import Main
from pico2d import *

name = "Pause"
image = None


def enter():
    global image
    image = load_image('Pause.png')
    pass


def exit():
    global image
    del(image)
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.key == (SDLK_k)):
                game_framework.pop_state()

    pass


def draw(frame_time):
 #   clear_canvas()
    image.draw(400,300)
    update_canvas()
    Main.pausedraw()
    pass

def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass




