import pygame as pg
import functions
import random

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((500,500))
surface = pg.display.get_surface()
player_pos = pg.Vector2(surface.get_width()/2,surface.get_height()/2)
screen_fullscreen = pg.display.get_desktop_sizes()
dt = 0
fullscreen = False
sliders = []
pg.display.set_caption('SliderBoom')

def game(running):
    global dt, fullscreen, screen_fullscreen, surface, player_pos, sliders
    while running:
        dt = clock.tick(60) / 1000
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            keys = pg.key.get_pressed()
            if event.type == pg.KEYDOWN:
                if keys[pg.K_ESCAPE]:
                    running = False
                if keys[pg.K_e]:
                    print("spawned")
                    functions.spawnslider(sliders, surface)
                if keys[pg.K_F11]:
                    fullscreen, surface = functions.togglefullscreen(fullscreen, screen_fullscreen)
                    player_pos = pg.Vector2(surface.get_width()/2,surface.get_height()/2)
        if keys[pg.K_w]:
            player_pos.y -= 5
        if keys[pg.K_a]:
            player_pos.x -= 5
        if keys[pg.K_s]:
            player_pos.y += 5
        if keys[pg.K_d]:
            player_pos.x += 5
        screen.fill((0,0,0,255))

        pg.draw.circle(screen,(255,0,0,255),player_pos,1)

        for slider in sliders:
            collide = slider[1].collidepoint(player_pos)
            color = (255, 0, 0) if collide else (slider[2])
            pg.draw.rect(screen,color,slider[1])
            slider[1].x += slider[3].x
            slider[1].y += slider[3].y
            if slider[1].x > surface.get_width() or slider[1].y > surface.get_height():
                slider[1].left = 0
                slider[1].top = 0
                slider[3] = pg.Vector2(random.randint(10,30) * (surface.get_width() / 1500),random.randint(10,30) * (surface.get_height() / 1500))
            if collide:
                running = False
        pg.display.flip()

game(True)

pg.quit()