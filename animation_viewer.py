from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('hero_spritesheet.png')

# 사격 경계 자세 이동
def move_1():
    frame = 0
    for x in range(0, 800, 5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 94, 0, 94, 80, x, 120, 282, 240)
        frame = (frame + 1) % 2
        update_canvas()
        delay(0.5)

# 점프 자세 이동
def move_2():
    frames = [0, 1, 2, 1]
    idx = 0
    for x in range(0, 800, 5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frames[idx] * 80, 100, 94, 80, x, 150, 282, 240)
        idx = (idx + 1) % len(frames)
        update_canvas()
        delay(0.1)


def move_3():
    pass


def move_4():
    pass


while True:
    #move_1()
    move_2()
    move_3()
    move_4()

close_canvas()