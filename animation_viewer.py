from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('hero_spritesheet.png')

for x in range (0,800,5):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(0, 0, 94, 80, x, 120, 282, 240)
    update_canvas()
    delay(0.01)

close_canvas()