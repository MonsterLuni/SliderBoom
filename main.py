import pygame as pg

running = True

pg.init()
pg.display.set_mode((500,500))
pg.display.set_caption('SliderBoom')

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        keys = pg.key.get_pressed()
        if event.type == pg.KEYDOWN:
            if keys[pg.K_ESCAPE]:
                running = False
            if keys[pg.K_s]:
                print("s")

pg.quit()