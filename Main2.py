import random
import json
import os

from pico2d import *

import game_framework
import Opening
import Pause
name = "Main2"

from PacMan import Character
from SecondMap import secondmap
from Ring import ring
from Ring1 import ring1
from Ring2 import ring2
from Ring3 import ring3
from Ring4 import ring4
from Ring5 import ring5
from Ring6 import ring6

from Enemy1 import FEnemy
from Enemy2 import SEnemy
from Enemy3 import TEnemy



PacMan = None
SecondMap = None
Ring = None
Ring1 = None
Enemy1 = None


def create_world():
    global Coin, Coin1, Coin2, Coin3, Coin4, Coin5, Coin6,PacMan, SecondMap, Ring , Enemy1, Enemy2, Enemy3, Ring1


    PacMan = Character()
    SecondMap = secondmap()

    Coin =  [ring() for i in range(1)]
    Coin1 = [ring1() for i in range(1)]
    Coin2 = [ring2() for i in range(1)]
    Coin3 = [ring3() for i in range(1)]
    Coin4 = [ring4() for i in range(1)]
    Coin5 = [ring5() for i in range(1)]
    Coin6 = [ring6() for i in range(1)]

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
#//////////////////////////////////////////////////////////////////////////


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
    Enemy1.update(frame_time)
    Enemy2.update(frame_time)
    Enemy3.update(frame_time)

#Collision
    for coin in Coin:
        if collide(PacMan, coin):
            Coin.remove(coin)
    for coin1 in Coin1:
        if collide(PacMan, coin1):
            Coin1.remove(coin1)
    for coin2 in Coin2:
        if collide(PacMan, coin2):
            Coin2.remove(coin2)
    for coin3 in Coin3:
        if collide(PacMan, coin3):
            Coin3.remove(coin3)
    for coin4 in Coin4:
        if collide(PacMan, coin4):
            Coin4.remove(coin4)
    for coin5 in Coin5:
        if collide(PacMan, coin5):
            Coin5.remove(coin5)
    for coin6 in Coin6:
        if collide(PacMan, coin6):
            Coin6.remove(coin6)

def pausedraw():
    SecondMap.draw()
    PacMan.draw()
    Enemy1.draw()
    Enemy2.draw()
    Enemy3.draw()

def draw(frame_time):
    clear_canvas()
    SecondMap.draw()
    PacMan.draw()



    update_canvas()

