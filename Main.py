import random
import json
import os

from pico2d import *

import game_framework
import Opening
import Pause

from PacMan import Character
from Map import FirstMap
from Ring import ring
from Enemy1 import FEnemy
from Enemy2 import SEnemy
from Enemy3 import TEnemy

name = "Main"

PacMan = None
Map = None
Ring = None
Enemy1 = None


def create_world():
    global PacMan, Map, Ring, Enemy1, Enemy2, Enemy3
    PacMan = Character()
    Map = FirstMap()
    Ring = ring()
    Enemy1 = FEnemy()
    Enemy2 = SEnemy()
    Enemy3 = TEnemy()


def enter():
    open_canvas()
    create_world()


def exit():
    close_canvas()


def pause():
    pass


def resume():
    pass

#pass
def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.push_state(Opening)
            else:
                PacMan.handle_event(event)
        if (event.key == (SDLK_p)):
            game_framework.push_state(Pause)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


def update(frame_time):
    PacMan.update(frame_time)
    Ring.update(frame_time)


def pausedraw():
    Map.draw()
    PacMan.draw()
    Ring.draw()
    Enemy1.draw()
    Enemy2.draw()
    Enemy3.draw()


def draw(frame_time):
    clear_canvas()
    Map.draw()
    PacMan.draw()
    Ring.draw()
    Enemy1.draw()
    Enemy2.draw()
    Enemy3.draw()
    update_canvas()

