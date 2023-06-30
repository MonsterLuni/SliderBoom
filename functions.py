import pygame as pg
import random

id = 0

def togglefullscreen(fullscreen, screen_fullscreen):
        match fullscreen:
            case False:
                pg.display.set_mode(screen_fullscreen[0])
                fullscreen = True
                pg.display.toggle_fullscreen()
            case True:
                pg.display.toggle_fullscreen()
                pg.display.set_mode((500,500))
                fullscreen = False
        surface = pg.display.get_surface()
        return fullscreen, surface

def spawnslider(sliders, surface):
    global id
    speed = pg.Vector2(random.randint(10,30) * (surface.get_width() / 1500),random.randint(10,30) * (surface.get_height() / 1500))
    rect = pg.Rect(0,0,random.randint(30,50),random.randint(30,50))
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255),255)
    sliders.append([
        id,
        rect,
        color,
        speed
     ])
    id += 1