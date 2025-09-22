from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('hero_spritesheet.png')

frame = 0
for x in range (0,800,5):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 94, 0, 94, 80, x, 120, 282, 240)
    frame = (frame + 1) % 2
    update_canvas()
    delay(0.5)


def move_1():
    pass


def move_2():
    pass


def move_3():
    pass


def move_4():
    pass


while True:
    move_1()
    move_2()
    move_3()
    move_4()

close_canvas()